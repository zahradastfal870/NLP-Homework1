"""
Q5 - Tokenization (Persian)
- Naive (space-based) tokenization
- Manual corrected tokens
- Tool-based tokenization using Hazm (Persian NLP)
- Comparison of tool output vs manual tokens

How to run:
    python -m pip install hazm
    python H1.Q5.py
"""

import re

# -----------------------------
# 1) Paragraph (Persian)
# -----------------------------
TEXT = (
    "شبکه‌های اجتماعی نقش مهمی در انتشار اطلاعات دارند. "
    "کاربران گاهی بدون بررسی صحت مطالب، اخبار را سریع منتشر می‌کنند. "
    "این رفتار می‌تواند باعث گسترش اطلاعات نادرست شود."
)

# -----------------------------
# 2) Naive tokenization (space-based)
# -----------------------------
naive_tokens = TEXT.split()

# -----------------------------
# 3) Manual corrected tokens (your corrected version)
# -----------------------------
manual_tokens = [
    "شبکه", "های", "اجتماعی", "نقش", "مهمی", "در", "انتشار", "اطلاعات", "دارند", ".",
    "کاربران", "گاهی", "بدون", "بررسی", "صحت", "مطالب", "،", "اخبار", "را",
    "سریع", "منتشر", "می", "کنند", ".",
    "این", "رفتار", "می", "تواند", "باعث", "گسترش", "اطلاعات", "نادرست", "شود", "."
]

# -----------------------------
# 4) Tool-based tokenization using Hazm
# -----------------------------
def hazm_tokenize(text: str):
    try:
        from hazm import Normalizer, word_tokenize
    except ImportError:
        raise ImportError("Hazm is not installed. Install it with: python -m pip install hazm")

    normalizer = Normalizer()
    normalized = normalizer.normalize(text)
    tokens = word_tokenize(normalized)

    # Ensure punctuation is separated (in case it sticks)
    cleaned = []
    for t in tokens:
        parts = re.findall(r"\w+|[^\w\s]", t, flags=re.UNICODE)
        cleaned.extend(parts if parts else [t])

    # Remove standalone Persian half-space token (ZWNJ) if it appears
    cleaned = [t for t in cleaned if t != "\u200c"]

    return cleaned

# -----------------------------
# 5) Comparison helper
# -----------------------------
def compare_tokens(manual, tool):
    manual_set = set(manual)
    tool_set = set(tool)

    only_in_manual = [t for t in manual if t not in tool_set]
    only_in_tool = [t for t in tool if t not in manual_set]

    diffs = []
    for i in range(min(len(manual), len(tool))):
        if manual[i] != tool[i]:
            diffs.append((i, manual[i], tool[i]))
            if len(diffs) >= 15:
                break

    return only_in_manual, only_in_tool, diffs

# -----------------------------
# 6) Main
# -----------------------------
def main():
    print("=== Q5 Tokenization (Persian) ===\n")
    print("Paragraph:\n", TEXT, "\n")

    print("1) Naive space-based tokens:")
    print(naive_tokens, "\n")

    print("2) Manual corrected tokens:")
    print(manual_tokens, "\n")

    print("3) Tool-based tokens (Hazm):")
    tool_tokens = hazm_tokenize(TEXT)
    print(tool_tokens, "\n")

    only_manual, only_tool, diffs = compare_tokens(manual_tokens, tool_tokens)

    print("4) Comparison (tool vs manual)")
    print("- Tokens only in MANUAL (ordered):")
    print(only_manual if only_manual else "None", "\n")

    print("- Tokens only in TOOL (ordered):")
    print(only_tool if only_tool else "None", "\n")

    print("- First positional mismatches (index, manual, tool):")
    print(diffs if diffs else "No mismatches in aligned positions (up to min length).", "\n")

    print("Done.")

if __name__ == "__main__":
    main()
