"""Converts text to speech that is spoken out loud."""
import azure.cognitiveservices.speech as speechsdk
import configparser

from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

class TextToSpeech():
    def text_to_speech(self, user_input:str):
        """Speaks a given user_input string.
        
            Args:
                user_input: The string to be converted to speech.

            Result:
                Speech from a string is spoken out loud via device's speakers.
                Error information is printed out if unable to perform TTS.
        """
        config = configparser.ConfigParser()
        config.read('config/config.ini')

        speech_key = config.get('azure_speech', 'key')
        service_region = config.get('azure_speech', 'service_region')
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

        audio_config = AudioOutputConfig(use_default_speaker=True)
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
        ssml_file = "azure/speech_settings/en_US/Guy.xml"
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
