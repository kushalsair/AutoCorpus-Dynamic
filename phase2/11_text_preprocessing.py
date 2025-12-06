def clean_html(text):
    return BeautifulSoup(text, "html.parser").get_text(" ")

def tokenize_text(text):
    if not isinstance(text, str):
        return []
    return re.findall(r"[a-zA-Z']+", text.lower())
