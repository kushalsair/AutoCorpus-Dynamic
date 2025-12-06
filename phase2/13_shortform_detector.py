short_counts = Counter()
contexts = defaultdict(list)

for tokens in sentences:
    for i, tok in enumerate(tokens):
        if len(tok) <= 4 and tok.isalpha():
            short_counts[tok] += 1
            # local context window
            left = max(0, i-3)
            right = min(len(tokens), i+4)
            ctx = " ".join(tokens[left:right])
            contexts[tok].append(ctx)

print("Top 20 short-ish tokens:")
short_counts.most_common(20)
