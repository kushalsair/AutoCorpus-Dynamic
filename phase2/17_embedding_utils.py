def phrase_embedding(phrase):
    tokens = tokenize_text(phrase)
    vecs = [w2v[w] for w in tokens if w in w2v]
    if not vecs:
        return None
    return np.mean(vecs, axis=0)
