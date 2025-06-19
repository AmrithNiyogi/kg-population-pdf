import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from langchain_community.document_loaders.pdf import PyPDFLoader
# import langchain.document_loaders.PyPDFLoader

nltk.download("punkt")

def preprocess_text(text):
    text = re.sub(r"\s+", " ", text)
    sentences = sent_tokenize(text)
    cleaned = []
    for sent in sentences:
        tokens = word_tokenize(sent)
        filtered = [w for w in tokens if w.isalnum()]
        cleaned.append(" ".join(filtered))
    return "\n".join(cleaned)


def extract_text_from_pdf(path):
    loader = PyPDFLoader(path)
    docs = loader.load()
    # print(f"[extract_text_from_pdf] {docs}")
    return preprocess_text(" ".join([doc.page_content for doc in docs]))