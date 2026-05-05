from gtts import gTTS
 
def text_to_audio(text, lang="en", filename="output.mp3"):
    # lang parameter pass hoga translated language ke liye
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename
 
