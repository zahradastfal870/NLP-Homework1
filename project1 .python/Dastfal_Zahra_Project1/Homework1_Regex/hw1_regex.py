import re

text = """
ZIP codes: 12345, 12345-6789, 12345 6789
Words: hello Hello don't State-of-the-art
Numbers: -12, +1,234, 3.14, 1.23e-4
Email spellings: email, e-mail, e mail, EMAIL
Interjections: go gooo goooo!
Is this a question?
"Is this quoted?"
"""

patterns = {
    "US_ZIP_codes": r"\b\d{5}(?:[- ]\d{4})?\b",
    "non_capital_words": r"\b(?![A-Z])[A-Za-z]+(?:[-'][A-Za-z]+)*\b",
    "numbers": r"[+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?",
    "email_variations": r"(?i)\be(?:[ -–])?mail\b",
    "go_interjection": r"\bgo+\b[!.,?]?",
    "lines_ending_with_question_mark": r'^.*\?\s*["\)”’\]]*\s*$'
}

for name, pattern in patterns.items():
    flags = re.MULTILINE if "lines" in name else 0
    matches = re.findall(pattern, text, flags=flags)
    cleaned = [m.strip() for m in matches]
    print(f"{name}: {cleaned}")

