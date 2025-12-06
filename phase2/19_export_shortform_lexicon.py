with open("/content/shortform_lexicon.json", "w", encoding="utf-8") as f:
    json.dump(shortform_lexicon, f, indent=2, ensure_ascii=False)

print("Saved shortform_lexicon.json")
