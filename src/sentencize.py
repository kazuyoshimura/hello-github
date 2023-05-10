import re

def sentencize(text):
    # 文章を分割するための正規表現
    pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"
    sentences = re.split(pattern, text)
    return sentences