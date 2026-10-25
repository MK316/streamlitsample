import streamlit as st
import streamlit.components.v1 as components
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
# Title
# --------------------------------------------------
st.title("🔊 Multilingual TTS")

st.write(
    "Generate speech using Streamlit, "
    "or try the browser-based HTML version."
)

# --------------------------------------------------
# Tabs
# --------------------------------------------------
tab1, tab2 = st.tabs([
    "🐍 Streamlit TTS",
    "🌐 HTML TTS"
])

# ==================================================
# TAB 1: Streamlit + gTTS
# ==================================================
with tab1:

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

    text = st.text_area(
        "Enter text",
        placeholder="Type something you want to hear...",
        height=150
    )

    if st.button(
        "🔊 Generate Speech",
        type="primary",
        use_container_width=True
    ):

        if not text.strip():
            st.warning("Please enter some text first.")

        else:
            try:
                selected = languages[language_name]

                tts = gTTS(
                    text=text,
                    lang=selected["lang"],
                    tld=selected["tld"]
                )

                audio_file = BytesIO()
                tts.write_to_fp(audio_file)
                audio_file.seek(0)

                st.audio(
                    audio_file,
                    format="audio/mp3"
                )

                st.download_button(
                    "⬇️ Download MP3",
                    data=audio_file.getvalue(),
                    file_name="tts_audio.mp3",
                    mime="audio/mpeg",
                    use_container_width=True
                )

            except Exception:
                st.error("Could not generate audio.")

# ==================================================
# TAB 2: HTML version
# ==================================================
with tab2:

    st.subheader("Browser-based TTS")

    st.caption(
        "This version uses HTML, JavaScript, "
        "and the browser Web Speech API."
    )

    with open("tts.html", "r", encoding="utf-8") as file:
        html_code = file.read()

    components.html(
        html_code,
        height=750,
        scrolling=True
    )
