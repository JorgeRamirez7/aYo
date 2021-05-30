import azure.cognitiveservices.speech as speechsdk
import configparser
import logging
import yaml

from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

from utils.import_dialogue import ImportDialogue

class TextToSpeech():
    """Converts text to speech that is spoken out loud."""

    def text_to_speech(self, user_input:str):
        """Speaks a given user_input string.
        
            Args:
                user_input: The string to be converted to speech.

            Result:
                Speech from a string is spoken out loud via device's speakers.
                Error information is printed out if unable to perform TTS.
        """
        azure_config = configparser.ConfigParser()
        azure_config.read('config/config.ini')

        speech_key = azure_config.get('azure_speech', 'key')
        service_region = azure_config.get('azure_speech', 'service_region')
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat["Riff24Khz16BitMonoPcm"])

        audio_config = AudioOutputConfig(use_default_speaker=True)
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        ssml_file = self.get_voice_settings()
        if ssml_file is None:
            logging.warning("TTS Failed - no supported gender found in ayo.ini")
            print("ayo output: {}".format(user_input))
            return None

        ssml_string = open(ssml_file, "r").read()
        result = synthesizer.speak_ssml_async(ssml_string.format(user_input)).get()

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("TTS: {}".format(user_input))

        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))

            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))

    def get_voice_settings(self):
        """Gets the default voice settings for the specified gender in ayo.ini."""
        ayo_config = configparser.ConfigParser()
        ayo_config.read('config/ayo.ini')

        ayo_localization = ayo_config.get('general', 'localization')
        ayo_voice_gender = ayo_config.get('general', 'voice')
        ayo_voices = ImportDialogue().import_dialogue("default-voices.yaml")
        voice_to_use = None

        if ayo_voice_gender == "male":
            voice_to_use = ayo_voices["male"]

        elif ayo_voice_gender == "female":
            voice_to_use = ayo_voices["female"]

        elif ayo_voice_gender == "nonbinary":
            voice_to_use = ayo_voices["nonbinary"]

        else:
            return None

        voice_settings = "azure/speech_settings/{0}/{1}".format(ayo_localization, voice_to_use)
            
        return voice_settings
