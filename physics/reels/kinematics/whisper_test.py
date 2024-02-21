import whisper


model = whisper.load_model("base")
result = model.transcribe("hello.m4a")

print(result["text"])
