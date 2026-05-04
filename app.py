import streamlit as st
import tempfile
import os

from speech_to_text import audio_to_text
from translator import translate_text
from text_to_speech import text_to_audio

st.set_page_config(page_title="Audio Translator", layout="centered")

st.title("🎤 AI Audio Language Translator")

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
    # save temp file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_audio_path = tmp_file.name

    st.success("Audio uploaded successfully!")

    if st.button("Translate Audio"):
        with st.spinner("Processing..."):

            # Step 1: Speech to Text
            text = audio_to_text(temp_audio_path)
            st.subheader("📝 Extracted Text")
            st.write(text)

            # Step 2: Translation
            translated_text = translate_text(text, languages[selected_lang])
            st.subheader("🌐 Translated Text")
            st.write(translated_text)

            # Step 3: Text to Speech
            output_audio = text_to_audio(translated_text)

            st.subheader("🔊 Translated Audio")
            st.audio(output_audio)

        # cleanup temp file
        os.remove(temp_audio_path)