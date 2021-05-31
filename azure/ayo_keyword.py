from pathlib import Path

import azure.cognitiveservices.speech as speechsdk

from azure.microphone_input import MicrophoneInput

class AyoKeyword():
    def ayo_keyword(self):
        """runs keyword spotting locally, with direct access to the result audio"""

        # Creates an instance of a keyword recognition model. Update this to
        # point to the location of your keyword recognition model.
        model = speechsdk.KeywordRecognitionModel(str(Path("azure/keyword_tables/hey_yo_basic.table")))

        # The phrase your keyword recognition model triggers on.
        keyword = "hey yo"

        # Create a local keyword recognizer with the default microphone device for input.
        keyword_recognizer = speechsdk.KeywordRecognizer()

        done = False

        def recognized_cb(evt):
            # Only a keyword phrase is recognized. The result cannot be 'NoMatch'
            # and there is no timeout. The recognizer runs until a keyword phrase
            # is detected or recognition is canceled (by stop_recognition_async()
            # or due to the end of an input file or stream).
            result = evt.result
            if result.reason == speechsdk.ResultReason.RecognizedKeyword:
                print("RECOGNIZED KEYWORD: {}".format(result.text))
                stop_future = keyword_recognizer.stop_recognition_async()
                stopped = stop_future.get()
                return True
                
            nonlocal done
            done = True

        def canceled_cb(evt):
            result = evt.result
            if result.reason == speechsdk.ResultReason.Canceled:
                print('CANCELED: {}'.format(result.cancellation_details.reason))
            nonlocal done
            done = True

        # Connect callbacks to the events fired by the keyword recognizer.
        keyword_recognizer.recognized.connect(recognized_cb)
        keyword_recognizer.canceled.connect(canceled_cb)

        # Start keyword recognition.
        result_future = keyword_recognizer.recognize_once_async(model)
        print('Say something starting with "{}" followed by whatever you want...'.format(keyword))
        result = result_future.get()
        return None
