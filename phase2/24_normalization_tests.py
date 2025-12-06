Sample_text = "That episode was fr 😭😭"
Sample_emojis = ["😭", "😭"]

norm_text, emoji_info = normalize_text_with_lexicons(Sample_text, Sample_emojis)

print("Original:", Sample_text)
print("Normalized:", norm_text)
print("Emoji semantics:")
print(json.dumps(emoji_info, indent=2, ensure_ascii=False))
