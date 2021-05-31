import azure.cognitiveservices.speech as speechsdk
import configparser
import logging

from pathlib import Path
from playsound import playsound

class MicrophoneInput():
    """Handles input from a user's microphone; speech to text"""

    """Configuration settings."""
    config = configparser.ConfigParser()
    config.read('config/config.ini')

    speech_key = config.get('azure_speech', 'key')
    service_region = config.get('azure_speech', 'service_region')
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    def get_voice_input(self):
        result = self.speech_recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            result_text = str(result.text).replace('.', '')
            result_text = str(result_text).replace(',', '')
            print("Recognized: {}".format(result_text))
            return result_text

        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
            return None

        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

            warning_sfx = Path("data/warning_azure_api_missing.mp3")
            playsound(str(warning_sfx))
            logging.critical("Please ensure that a proper key and service region is provided for Azure within config/ayo.ini.")

            return None
