from gtts import gTTS
import streamlit as st

# Streamlit UI
st.title("Text-to-Speech Converter")
st.write("Enter the text below, and I'll convert it to speech for you!")

# Text input field
user_input = st.text_area("Enter your text here:")

# Language selection
language = st.selectbox(
    "Select Language",
    options=["English", "Spanish", "French", "German", "Hindi"],
    index=0
)

# Mapping languages to language codes
language_codes = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi"
}
language_code = language_codes[language]

# Button to generate speech
if st.button("Convert to Speech"):
    if not user_input.strip():
        st.error("Please enter some text!")
    else:
        # Generate speech using gTTS
        tts = gTTS(text=user_input, lang=language_code, slow=False)
        audio_file = "output.mp3"
        tts.save(audio_file)

        # Display success message
        st.success("Speech generated successfully!")

        # Play the audio in the app
        with open(audio_file, "rb") as audio:
            st.audio(audio.read(), format="audio/mp3")
