import azure.cognitiveservices.speech as speechsdk
import configparser
import logging
import yaml

from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from pathlib import Path
from playsound import playsound

from utils.import_dialogue import ImportDialogue

class TextToSpeech():
    """Converts text to speech that is spoken out loud."""

    "Configuration settings."
    azure_config = configparser.ConfigParser()
    azure_config.read(Path("config/config.ini"))

    ayo_config = configparser.ConfigParser()
    ayo_config.read(Path("config/ayo.ini"))

    try:
        speech_key = azure_config.get('azure_speech', 'key')
        service_region = azure_config.get('azure_speech', 'service_region')
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat["Riff24Khz16BitMonoPcm"])
        audio_config = AudioOutputConfig(use_default_speaker=True)
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    except:
        logging.critical("There is no 'azure_speech' value in config/config.ini")
        playsound(str(Path("data/warning_azure_api_missing.mp3")))

    

    """Gets the default voice settings for the specified gender in ayo.ini."""
    ayo_localization = ayo_config.get('general', 'localization')
    ayo_voice_gender = ayo_config.get('general', 'voice')
    ayo_voices = ImportDialogue().import_dialogue("default-voices.yaml")

    if ayo_voice_gender == "male":
        voice_to_use = ayo_voices["male"]
    elif ayo_voice_gender == "female":
        voice_to_use = ayo_voices["female"]
    elif ayo_voice_gender == "nonbinary":
        voice_to_use = ayo_voices["nonbinary"]
    else:
        logging.critical("No supported gender found in ayo.ini")
    voice_settings_ssml= "azure/speech_settings/{0}/{1}".format(ayo_localization, voice_to_use)
    voice_settings = Path(voice_settings_ssml)

    def text_to_speech(self, user_input:str):
        """Speaks a given user_input string.
        
            Args:
                user_input: The string to be converted to speech.

            Result:
                Speech from a string is spoken out loud via device's speakers.
                Error information is printed out if unable to perform TTS.
        """
        

        
        if self.voice_settings is None:
            logging.warning("TTS Failed - no supported gender found in ayo.ini")
            print("ayo output: {}".format(user_input))
            return None

        ssml_string = open(self.voice_settings, "r").read()
        result = self.synthesizer.speak_ssml_async(ssml_string.format(user_input)).get()

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("TTS: {}".format(user_input))

        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))

            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))

            print("\nayo output: {}".format(user_input))
            warning_sfx = Path("data/warning_azure_api_missing.mp3")
            playsound(str(warning_sfx))
            logging.critical("Please ensure that a proper key and service region is provided for Azure within config/ayo.ini.")
