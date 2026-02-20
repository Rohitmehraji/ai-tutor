from .nlp import translate_text


def tutor_reply(message_en: str) -> str:
    message = message_en.lower()
    if "algebra" in message:
        return "Start by isolating variables step by step. Want me to solve one with you?"
    if "photosynthesis" in message:
        return "Plants use sunlight, water, and carbon dioxide to create glucose and oxygen."
    if "doubt" in message or "confused" in message:
        return "I can help right now. Tell me which step is confusing and I'll break it down."
    return "Great question. Here's a quick explanation and then a practice prompt to reinforce it."


def resolve_doubt(user_message: str, source_lang: str, target_lang: str) -> tuple[str, str]:
    message_en = translate_text(user_message, source_lang, "en") if source_lang != "en" else user_message
    reply_en = tutor_reply(message_en)
    localized_reply = translate_text(reply_en, "en", target_lang)
    return message_en, localized_reply
