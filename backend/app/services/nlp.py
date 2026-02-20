from deep_translator import GoogleTranslator
from langdetect import detect

SUPPORTED_LANGUAGES = {"en", "hi", "ta", "te", "bn", "mr", "gu", "kn", "ml", "pa", "ur"}


def detect_language(text: str) -> str:
    try:
        lang = detect(text)
    except Exception:
        return "en"
    return lang if lang in SUPPORTED_LANGUAGES else "en"


def translate_text(text: str, source: str, target: str) -> str:
    if source == target:
        return text
    try:
        return GoogleTranslator(source=source, target=target).translate(text)
    except Exception:
        return text
