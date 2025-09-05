from .errors import EmptyText, TextTooShort, TextTooLong

MIN_LEN = 5
MAX_LEN = 500

def _ensure_not_empty(text: str) -> None:
    if not text.strip():
        raise EmptyText()

def _ensure_length_limits(text: str) -> None:
    length = len(text)
    if length < MIN_LEN:
        raise TextTooShort(MIN_LEN, length)
    if length > MAX_LEN:
        raise TextTooLong(MAX_LEN, length)

def load_and_validate_text(raw: str) -> str:
    if raw is None:
        raise EmptyText()
    text = raw.strip()
    _ensure_not_empty(text)
    _ensure_length_limits(text)
    return text
