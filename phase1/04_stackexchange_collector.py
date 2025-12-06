def fetch_answers_for_question(question_id, site="scifi", last_answer_id=None):
    """
    Fetch answers for the specific StackExchange question.
    Includes rate-limit handling and API key.
    """
    url = f"https://api.stackexchange.com/2.3/questions/{question_id}/answers"

    params = {
        "order": "asc",
        "sort": "creation",
        "site": site,
        "filter": "withbody",
        "pagesize": 50,
        "key": "rl_dANTE2EoTjd8rDagwGUfseAgq"   # optional but helps avoid rate limits
    }

    resp = requests.get(url, params=params)

    # Handle rate limiting (429)
    if resp.status_code == 429:
        print("[WARN] API Error 429: Too many requests")

        # If backoff is provided, follow it
        try:
            data = resp.json()
            if "backoff" in data:
                wait_time = data["backoff"]
                print(f"[INFO] Respecting backoff: waiting {wait_time} seconds")
                time.sleep(wait_time)
        except:
            pass

        # Return no answers for this cycle
        return [], last_answer_id

    if resp.status_code != 200:
        print("[WARN] API Error:", resp.status_code)
        return [], last_answer_id

    data = resp.json()

    # Respect server-provided backoff
    if "backoff" in data:
        wait_time = data["backoff"]
        print(f"[INFO] API requested backoff: waiting {wait_time} seconds")
        time.sleep(wait_time)

    items = data.get("items", [])

    new_answers = []
    newest_id = last_answer_id

    for ans in items:
        aid = ans["answer_id"]
        body = ans.get("body_markdown", "") or ans.get("body", "")
        ts = ans.get("creation_date")

        if last_answer_id and aid <= last_answer_id:
            continue

        new_answers.append({
            "id": aid,
            "timestamp": epoch_to_time(ts),
            "raw_text": body
        })

        if newest_id is None or aid > newest_id:
            newest_id = aid

    return new_answers, newest_id
