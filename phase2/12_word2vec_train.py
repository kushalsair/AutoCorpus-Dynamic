if len(sentences) > 0:
    model = Word2Vec(
        sentences,
        vector_size=100,
        window=5,
        min_count=2,
        workers=4,
        sg=1
    )
    w2v = model.wv
    print("Embedding vocab size:", len(w2v))
else:
    w2v = None
    print("WARNING: No sentences available for Word2Vec.")
