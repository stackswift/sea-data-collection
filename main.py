import streamlit as st
import speech_recognition as sr

def speech_to_text(audio_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_file) as source:
        # Record audio data
        audio_data = recognizer.record(source)

        # Convert speech to text
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Unable to recognize speech"
        except sr.RequestError as e:
            return f"Error: {str(e)}"

def main():
    st.title("Speech to Text Converter")

    st.header("Upload Audio File")

    # File upload
    audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3"])

    if audio_file:
        # Convert speech to text
        text = speech_to_text(audio_file)

        # Display the converted text
        st.subheader("Converted Text:")
        st.write(text)

if __name__ == "__main__":
    main()

