with open("/content/emoji_semantics.json", "w", encoding="utf-8") as f:
    json.dump(emoji_semantics, f, indent=2, ensure_ascii=False)

print("Saved emoji_semantics.json")
