import streamlit as st
from gtts import gTTS
from io import BytesIO

# --------------------------------------------------
# Page setup
# --------------------------------------------------
st.set_page_config(
    page_title="Multilingual TTS",
    page_icon="🔊",
    layout="centered"
)

# --------------------------------------------------
# Simple styling
# --------------------------------------------------
st.markdown("""
<style>
    .block-container {
        max-width: 700px;
        padding-top: 3rem;
    }

    .main-title {
        text-align: center;
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.markdown(
    '<div class="main-title">🔊 Multilingual TTS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Type a sentence, choose a language, and listen to it.'
    '</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# Language options
# Each item contains:
# language code + Google domain
# --------------------------------------------------
languages = {
    "🇺🇸 English — American": {"lang": "en", "tld": "com"},
    "🇬🇧 English — British": {"lang": "en", "tld": "co.uk"},
    "🇰🇷 Korean": {"lang": "ko", "tld": "com"},
    "🇯🇵 Japanese": {"lang": "ja", "tld": "com"},
    "🇨🇳 Chinese": {"lang": "zh-CN", "tld": "com"},
    "🇫🇷 French": {"lang": "fr", "tld": "fr"},
    "🇪🇸 Spanish": {"lang": "es", "tld": "es"},
    "🇩🇪 German": {"lang": "de", "tld": "de"},
    "🇻🇳 Vietnamese": {"lang": "vi", "tld": "com"}
}

language_name = st.selectbox(
    "Choose a language",
    list(languages.keys())
)

# Get language settings
selected_language = languages[language_name]

# --------------------------------------------------
# Text input
# --------------------------------------------------
text = st.text_area(
    "Enter text",
    placeholder="Type something you want to hear...",
    height=150
)

# --------------------------------------------------
# Generate speech
# --------------------------------------------------
if st.button(
    "🔊 Generate Speech",
    type="primary",
    use_container_width=True
):

    if not text.strip():
        st.warning("Please enter some text first.")

    else:
        try:
            # Create speech
            tts = gTTS(
                text=text,
                lang=selected_language["lang"],
                tld=selected_language["tld"]
            )

            # Save audio in memory
            audio_file = BytesIO()
            tts.write_to_fp(audio_file)
            audio_file.seek(0)

            # Display result
            st.success("Audio generated successfully!")

            st.audio(
                audio_file,
                format="audio/mp3"
            )

            # Download button
            st.download_button(
                label="⬇️ Download MP3",
                data=audio_file.getvalue(),
                file_name="tts_audio.mp3",
                mime="audio/mpeg",
                use_container_width=True
            )

        except Exception:
            st.error(
                "Could not generate audio. "
                "Please check your internet connection and try again."
            )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.divider()

st.caption(
    "Built with Python, Streamlit, and Google Text-to-Speech (gTTS)."
)
