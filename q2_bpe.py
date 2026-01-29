from collections import Counter, defaultdict

# Toy corpus from class
corpus = (
    "low low low low low lowest lowest "
    "newer newer newer newer newer newer "
    "wider wider wider new new"
)

# Add end-of-word marker and split into characters
def prepare_corpus(text):
    words = text.split()
    return [list(word) + ["_"] for word in words]

def get_bigrams(corpus):
    bigrams = Counter()
    for word in corpus:
        for i in range(len(word) - 1):
            bigrams[(word[i], word[i+1])] += 1
    return bigrams

def merge_pair(pair, corpus):
    a, b = pair
    new_corpus = []
    for word in corpus:
        new_word = []
        i = 0
        while i < len(word):
            if i < len(word) - 1 and word[i] == a and word[i+1] == b:
                new_word.append(a + b)
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        new_corpus.append(new_word)
    return new_corpus

# Run BPE
corpus_chars = prepare_corpus(corpus)
vocab = set(ch for word in corpus_chars for ch in word)

num_merges = 10
merges = []

for step in range(num_merges):
    bigrams = get_bigrams(corpus_chars)
    if not bigrams:
        break
    top_pair = bigrams.most_common(1)[0][0]
    merges.append(top_pair)

    corpus_chars = merge_pair(top_pair, corpus_chars)
    vocab.add("".join(top_pair))

    print(
        f"Step {step+1}: merge {top_pair} "
        f"→ vocabulary size = {len(vocab)}"
    )
