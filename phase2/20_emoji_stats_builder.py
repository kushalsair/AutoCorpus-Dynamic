def normalize_emojis_column(val):
    if isinstance(val, list):
        return val
    if isinstance(val, str):
        try:
            x = json.loads(val)
            if isinstance(x, list):
                return x
        except:
            pass
    return []

df["emojis"] = df["emojis"].apply(normalize_emojis_column)

emoji_counts = Counter()
word_counts = Counter()
emoji_word_counts = Counter()

for _, row in df.iterrows():
    words = set(tokenize_text(row["text_clean"]))
    emojis = set(row["emojis"])

    for w in words:
        word_counts[w] += 1
    for e in emojis:
        emoji_counts[e] += 1
    for e in emojis:
        for w in words:
            emoji_word_counts[(e, w)] += 1

num_docs = len(df)
