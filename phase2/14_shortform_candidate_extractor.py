short_counts = Counter()
contexts = defaultdict(list)

for tokens in sentences:
    for i, tok in enumerate(tokens):
        if len(tok) <= 4 and tok.isalpha():
            short_counts[tok] += 1
            ctx_window = tokens[max(0, i-3): min(len(tokens), i+4)]
            contexts[tok].append(" ".join(ctx_window))

stopwords = set("""
the and for you your are was were with this that have has not but from when what they them then than
into over here there just like very more some any much many most been did doing done such its
""".split())

shortform_candidates = [
    (tok, freq) for tok, freq in short_counts.items()
    if freq >= 3 and tok not in stopwords
]

shortform_candidates[:20]
