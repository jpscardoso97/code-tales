import azure.cognitiveservices.speech as speechsdk
import os

from data_layer.storage import upload_blob
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

script_dir = os.path.dirname(os.path.abspath(__file__))
static_folder = os.path.join(script_dir, '../static')

def generate_audio_story(story_id, story):
    # Creates an instance of a speech config with specified subscription key and service region.
    speech_key = os.getenv('SPEECH_KEY')
    service_region = os.getenv("SVC_REG")

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3)
    
    # Note: the voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"

    filename=f"{static_folder}/{story_id}.mp3"

    # Specify the output audio format and filename
    file_config = speechsdk.audio.AudioOutputConfig(filename=filename)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)

    result = speech_synthesizer.speak_text_async(story).get()
    
    # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized for story_id {story_id}")
        upload_blob(filename, f"story-{story_id}.mp3")

        return result
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))