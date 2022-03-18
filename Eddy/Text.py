import re

def split(text):
    text = text.lower()
    text = re.sub(r"[^a-zß-ÿ\d\s.!?'-]", "", text)
    text = re.sub(r"[!?]|\.+", " .", text)
    text = re.sub(r"([^.])$", r"\1 .", text)
    return text.split()

def combine(words):
    text = " ".join(words)
    text = re.sub(r" \.", ".", text)
    text = re.sub(r"(^|[.?!] )[a-zß-ÿ]", lambda match: match.group(0).upper(), text)
    return text