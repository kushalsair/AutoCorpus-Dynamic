from numpy.linalg import norm

def cosine(a, b):
    if a is None or b is None:
        return 0.0
    return float(np.dot(a, b) / (norm(a) * norm(b))) if (norm(a) > 0 and norm(b) > 0) else 0.0

shortform_lexicon = {}

for tok, freq in shortform_candidates:
    if not w2v or tok not in w2v:
        continue

    v = w2v[tok]
    aff_score = cosine(v, affirmation_centroid) if affirmation_centroid is not None else 0.0

    # classification
    semantic_type = "affirmation_like" if aff_score >= 0.35 else "other"

    # best expansion
    best_expansion = None
    best_sim = 0.0

    if tok in built_in_short_forms:
        phrase = built_in_short_forms[tok]
        pvec = phrase_embedding(phrase)
        if pvec is not None:
            best_expansion = phrase
            best_sim = cosine(v, pvec)

    shortform_lexicon[tok] = {
        "freq": freq,
        "semantic_type": semantic_type,
        "affirmation_score": round(aff_score, 3),
        "expansion": best_expansion,
        "expansion_similarity": round(best_sim, 3),
        "example_contexts": contexts[tok][:5]
    }

shortform_lexicon
