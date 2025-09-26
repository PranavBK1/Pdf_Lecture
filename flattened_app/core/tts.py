import pyttsx3
from gtts import gTTS

def text_to_speech(text: str, out_path: str, engine: str = "gtts"):
    """
    Generate speech from text. Options: 'gtts' (Google TTS), 'pyttsx3' (offline).
    """
    if engine == "pyttsx3":
        tts_engine = pyttsx3.init()
        tts_engine.save_to_file(text, out_path)
        tts_engine.runAndWait()
    else:  # default gTTS
        tts = gTTS(text)
        tts.save(out_path)
