from gtts import gTTS

def text_to_audio(text, filename="output.mp3"):
    tts = gTTS(text=text)
    tts.save(filename)
    return filename