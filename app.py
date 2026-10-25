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
    "🐳 Streamlit TTS",
    "🌐 HTML TTS"
])

# ==================================================
# TAB 1: Streamlit + gTTS
# ==================================================
with tab1:

    languages = {
        "🇺🇸 English — American": {
            "lang": "en",
            "tld": "com",
            "sample": (
                "Welcome! This is my TTS application for my future students. "
                "I hope you enjoy this application."
            )
        },

        "🇬🇧 English — British": {
            "lang": "en",
            "tld": "co.uk",
            "sample": (
                "Welcome! This is my TTS application for my future students. "
                "I hope you enjoy this application."
            )
        },

        "🇰🇷 Korean": {
            "lang": "ko",
            "tld": "com",
            "sample": (
                "환영합니다! 이것은 제가 미래의 학생들을 위해 만든 "
                "TTS 애플리케이션입니다. 이 애플리케이션을 즐겁게 사용하시길 바랍니다."
            )
        },

        "🇯🇵 Japanese": {
            "lang": "ja",
            "tld": "com",
            "sample": (
                "ようこそ！これは私が将来の生徒たちのために作った "
                "TTSアプリケーションです。このアプリを楽しんでいただければ嬉しいです。"
            )
        },

        "🇨🇳 Chinese": {
            "lang": "zh-CN",
            "tld": "com",
            "sample": (
                "欢迎！这是我为未来的学生制作的TTS应用程序。"
                "希望你喜欢这个应用程序。"
            )
        },

        "🇫🇷 French": {
            "lang": "fr",
            "tld": "fr",
            "sample": (
                "Bienvenue ! Voici mon application de synthèse vocale "
                "pour mes futurs élèves. J'espère que vous apprécierez cette application."
            )
        },

        "🇪🇸 Spanish": {
            "lang": "es",
            "tld": "es",
            "sample": (
                "¡Bienvenidos! Esta es mi aplicación de texto a voz "
                "para mis futuros estudiantes. Espero que disfruten de esta aplicación."
            )
        },

        "🇩🇪 German": {
            "lang": "de",
            "tld": "de",
            "sample": (
                "Willkommen! Dies ist meine TTS-Anwendung für meine zukünftigen Schüler. "
                "Ich hoffe, dass Ihnen diese Anwendung gefällt."
            )
        },

        "🇻🇳 Vietnamese": {
            "lang": "vi",
            "tld": "com",
            "sample": (
                "Chào mừng! Đây là ứng dụng chuyển văn bản thành giọng nói "
                "mà tôi tạo cho các học sinh tương lai của mình. "
                "Tôi hy vọng các bạn sẽ thích ứng dụng này."
            )
        }
    }

    language_name = st.selectbox(
        "Choose a language",
        list(languages.keys())
    )

    selected = languages[language_name]

    text = st.text_area(
        "Enter text",
        value=selected["sample"],
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
                tts = gTTS(
                    text=text,
                    lang=selected["lang"],
                    tld=selected["tld"]
                )

                audio_file = BytesIO()
                tts.write_to_fp(audio_file)
                audio_file.seek(0)

                st.success("Audio generated successfully!")

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
