def pmi(e, w):
    c_e = emoji_counts[e]
    c_w = word_counts[w]
    c_ew = emoji_word_counts[(e, w)]
    if c_ew == 0:
        return 0
    p_e = c_e / num_docs
    p_w = c_w / num_docs
    p_ew = c_ew / num_docs
    return np.log2(p_ew / (p_e * p_w)) if p_e > 0 and p_w > 0 else 0

emoji_semantics = {}

for e in emoji_counts:
    rows = []
    for (emj, w), c in emoji_word_counts.items():
        if emj != e:
            continue
        score = pmi(e, w)
        rows.append((w, c, score))

    rows = sorted(rows, key=lambda x: x[2], reverse=True)
    emoji_semantics[e] = [
        {"word": w, "count": c, "pmi": round(score, 3)}
        for (w, c, score) in rows[:10]
    ]

emoji_semantics
