QUESTION_ID = 301338
SITE = "scifi"
CORPUS_PATH = "/content/scifi_dynamic_corpus.jsonl"
CHECK_INTERVAL = 40

# --- Load last seen ID from previous session ---
last_seen_id = load_last_seen_id()

print("\n[STARTING AUTO-CORPUS]")
print(f"Monitoring Question ID: {QUESTION_ID}")
print(f"Loaded last_seen_id = {last_seen_id}")
print("Corpus path:", CORPUS_PATH)
print("State path:", LAST_ID_PATH, "\n")

while True:
    answers, new_last_seen = fetch_answers_for_question(
        QUESTION_ID,
        site=SITE,
        last_answer_id=last_seen_id
    )

    if answers:
        print(f"[{datetime.now()}] Found {len(answers)} new answers!")

        processed = []
        for a in answers:
            processed.append({
                "id": a["id"],
                "timestamp": a["timestamp"],
                "text_clean": clean_text(a["raw_text"]),
                "emojis": extract_emojis(a["raw_text"])
            })

        append_to_corpus(CORPUS_PATH, processed)
        save_last_seen_id(new_last_seen)

        print("[INFO] Updated corpus + saved last_seen_id\n")

        last_seen_id = new_last_seen

    else:
        print(f"[{datetime.now()}] No new answers. Waiting...\n")

    time.sleep(CHECK_INTERVAL)
