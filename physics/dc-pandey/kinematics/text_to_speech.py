from pathlib import Path
from pydub import AudioSegment
from openai import OpenAI

client = OpenAI()

with open("transcription.txt", "r") as file:
    input_text = file.read()

# Split the input text into chunks of 4096 characters
max_length = 4096
chunks = [input_text[i:i+max_length]
          for i in range(0, len(input_text), max_length)]

audio_files = []
for i, chunk in enumerate(chunks):
    response = client.audio.speech.create(
        model="tts-1",
        voice="shimmer",
        input=chunk,
    )

    # Save the audio file
    speech_file_path = Path(__file__).parent / f"speech_{i}.mp3"
    with open(speech_file_path, "wb") as file:
        file.write(response.content)
    audio_files.append(speech_file_path)

# Concatenate the audio files
combined = AudioSegment.empty()
for audio_file in audio_files:
    sound = AudioSegment.from_file(audio_file, format="mp3")
    combined += sound

# Save the combined audio file
combined.export("combined_speech.mp3", format="mp3")
