import pypandoc
import nltk
from nltk.tokenize import sent_tokenize

# Download the necessary NLTK models (if not already downloaded)
nltk.download('punkt')

def chunk_text(text, max_length=2000):
    """
    Chunk text into segments of a specified maximum length.

    :param text: The long string of text to be chunked.
    :param max_length: The maximum length of each chunk.
    :return: A list of text chunks.
    """
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []

    for sentence in sentences:
        if len(' '.join(current_chunk) + ' ' + sentence) <= max_length:
            current_chunk.append(sentence)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

pypandoc_compatible = [
    "biblatex", "bibtex", "commonmark", "commonmark_x", "creole", "csljson", 
    "csv", "docbook", "docx", "dokuwiki", "endnotexml", "epub", "fb2", "gfm", 
    "haddock", "html", "ipynb", "jats", "jira", "json", "latex", "man", 
    "markdown", "markdown_github", "markdown_mmd", "markdown_phpextra", 
    "markdown_strict", "mediawiki", "muse", "native", "odt", "opml", "org", 
    "ris", "rst", "rtf", "t2t", "textile", "tikiwiki", "tsv", "twiki", "vimwiki"
]

def read_normal_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"


def get_chunks(file_path: str):
    file_end = file_path.split(".")[-1]
    if (file_end in pypandoc_compatible):
        text: str = pypandoc.convert_file(file_path, 'rst')
    else:
        text: str = read_normal_file(file_path)
    text = text.replace("\r","")
    chunks = chunk_text(text)
    return chunks

if __name__ == "__main__":
    chunks = get_chunks("documents/t.txt")
    print(len(chunks[0]), len(chunks))