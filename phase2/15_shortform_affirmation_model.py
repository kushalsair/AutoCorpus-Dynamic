affirmation_seed_words = [
    "true", "really", "honestly", "legit", "facts", "exactly",
    "yeah", "yep", "correct", "right", "indeed", "actually"
]

seed_vecs = []
if w2v:
    for w in affirmation_seed_words:
        if w in w2v:
            seed_vecs.append(w2v[w])

affirmation_centroid = np.mean(seed_vecs, axis=0) if seed_vecs else None
affirmation_centroid is not None
