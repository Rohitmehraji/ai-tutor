import base64


def speech_to_text_simulated(text_payload: str) -> str:
    return text_payload.strip()


def text_to_speech_simulated(text: str, language: str) -> str:
    fake_audio = f"AUDIO({language}):{text}".encode("utf-8")
    return base64.b64encode(fake_audio).decode("utf-8")
