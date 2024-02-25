import fitz  # Import PyMuPDF
import ollama

def read_pdf(file_path):
    # Open the PDF file
    with fitz.open(file_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def split_into_chunks(text, chunk_size):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(current_chunk) >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
    # Add the last chunk if it contains any words
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

file_path = "./002-GINGER-THE-GIRAFFE-Free-Childrens-Book-By-Monkey-Pen.pdf"
long_string = read_pdf(file_path)
chunk_size = 500
chunks = split_into_chunks(long_string, chunk_size)
model = "nomic-embed-text"
print(f"long_string: {long_string}")
print(f"Number of chunks: {len(chunks)}")
for i, chunk in enumerate(chunks, start=1):
    response = ollama.embeddings(model, prompt=chunk)
    print(f"Chunk {i} response:", response)

