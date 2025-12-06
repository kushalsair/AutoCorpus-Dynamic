import os

LAST_ID_PATH = "/content/last_seen_id.txt"

def load_last_seen_id():
    if os.path.exists(LAST_ID_PATH):
        with open(LAST_ID_PATH, "r") as f:
            v = f.read().strip()
            return int(v) if v else None
    return None

def save_last_seen_id(answer_id):
    with open(LAST_ID_PATH, "w") as f:
        f.write(str(answer_id))
