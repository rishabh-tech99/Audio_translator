import whisper
 
# Load model once at startup (base model is good balance of speed & accuracy)
model = whisper.load_model("base")
 
def audio_to_text(audio_file):
    # fp16=False → CPU pe bhi properly kaam karta hai, no warnings
    result = model.transcribe(audio_file, fp16=False)
    return result["text"]
 
