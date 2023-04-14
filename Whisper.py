import whisper;
model = whisper.load_model("base")
result = model.transcribe("Flotsam.mp3")
print(result["text"])