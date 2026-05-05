import streamlit as st
import tempfile
import os
 
from speech_to_text import audio_to_text
from translator import translate_text
from text_to_speech import text_to_audio
 
st.set_page_config(page_title="Audio Translator", layout="centered")
 
st.title("🎙️ AI Audio Language Translator")
 
st.write("Upload an audio file and convert it into another language")
 
# language options
languages = {
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}
 
uploaded_file = st.file_uploader("Upload Audio File", type=["mp3", "wav"])
 
selected_lang = st.selectbox("Select Target Language", list(languages.keys()))
 
if uploaded_file:
    # Get correct file extension (.mp3 or .wav)
    suffix = "." + uploaded_file.name.split(".")[-1]
 
    # Save uploaded file to temp path with proper extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_audio_path = tmp_file.name
 
    st.success("Audio uploaded successfully!")
 
    if st.button("Translate Audio"):
        with st.spinner("Processing... please wait"):
 
            # Step 1: Speech to Text
            st.subheader(" Extracted Text")
            text = audio_to_text(temp_audio_path)
            if not text or text.strip() == "":
                st.error("Could not extract text from audio. Please check your audio file.")
            else:
                st.write(text)
 
                # Step 2: Translation
                st.subheader(" Translated Text")
                translated_text = translate_text(text, languages[selected_lang])
                st.write(translated_text)
 
                # Step 3: Text to Speech
                output_audio = text_to_audio(translated_text, lang=languages[selected_lang])
 
                st.subheader(" Translated Audio")
                st.audio(output_audio)
 
        # Cleanup temp file
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)
 
