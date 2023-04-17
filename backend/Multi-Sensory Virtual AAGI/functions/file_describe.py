import os
from moviepy.editor import *
from transformers import pipeline
import openai
from dotenv import load_dotenv
import os
import imageio

# load the environment variables from the .env file
load_dotenv()

# get the value of the OPENAI_API_KEY environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

def file_describe_function(file_path):
    file_extension = os.path.splitext(file_path)[1]
    if file_extension in ('.jpg', '.jpeg', '.png', '.gif', '.bmp'):
        print('Image Uploaded')
        file_description = image_to_text(file_path)[0]['generated_text']
        return file_description
    elif file_extension in ('.mp4', '.avi', '.wmv', '.mov', '.flv'):
        print('Video Uploaded')
        file_path_without_extension = os.path.splitext(file_path)[0]
        video = VideoFileClip(file_path)
        audio = video.audio
        try:
            audio.write_audiofile(file_path_without_extension + "audio_extracted.mp3")
            audio_file= open(file_path_without_extension + "audio_extracted.mp3", "rb")
            transcript = "Audio Transcript of the video is:\n"
            print("waiting for audio transcription")
            transcript = transcript + openai.Audio.transcribe("whisper-1", audio_file).text
        except Exception as e:
            transcript = "No audio"

        # Extract one frame per second from the video and process it
        transcript = transcript + "\nDescription of one frame of each second in the video is:\n"
        frames_per_second = 1
        fps = video.fps
        count = 0
        for i, frame in enumerate(video.iter_frames()):
            if i % (fps // frames_per_second) == 0:
                print(count)
                count = count + 1
                frame_path = f"{file_path_without_extension}_frame{i}.png"
                imageio.imwrite(frame_path, frame)
                file_description = image_to_text(frame_path)[0]['generated_text']
                transcript += file_description + "\n"
        return transcript
    elif file_extension in ('.mp3', '.wav', '.wma', '.aac'):
        print('Audio Uploaded')
        audio_file= open(file_path, "rb")
        print("waiting for audio transcription")
        transcript = openai.Audio.transcribe("whisper-1", audio_file).text
        return transcript
    else:
        print('Unknown file type')
        return ""