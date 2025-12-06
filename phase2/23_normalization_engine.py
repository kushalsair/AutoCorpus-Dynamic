def normalize_text_with_lexicons(text, emojis_in_text):
    tokens = tokenize_text(text)
    norm_tokens = []

    for t in tokens:
        # 1. If model learned meaning from corpus
        if t in shortform_lexicon and shortform_lexicon[t]["expansion"]:
            norm_tokens.extend(tokenize_text(shortform_lexicon[t]["expansion"]))
        # 2. If not in corpus but in built-in lexicon
        elif t in built_in_short_forms:
            norm_tokens.extend(tokenize_text(built_in_short_forms[t]))
        else:
            norm_tokens.append(t)

    # Emoji meaning extraction
    emoji_info = {}
    for e in emojis_in_text:
        if e in emoji_semantics and emoji_semantics[e]:
            emoji_info[e] = emoji_semantics[e][:5]
        elif e in built_in_emoji_meanings:
            emoji_info[e] = built_in_emoji_meanings[e]
        else:
            emoji_info[e] = []

    return " ".join(norm_tokens), emoji_info
