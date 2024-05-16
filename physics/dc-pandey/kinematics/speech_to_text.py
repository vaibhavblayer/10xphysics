from openai import OpenAI
client = OpenAI()

audio_file = open(
    "It's better to be alone than wish you were [NlYr7LJsqi0].mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text"
)
print(transcription)
with open("transcription.txt", "w") as file:
    file.write(transcription)
