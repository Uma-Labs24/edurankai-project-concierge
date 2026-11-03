from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable

@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    source: str
    text: str

def normalize_text(text: str) -> str:
    return re.sub(r"\\s+", " ", text).strip()

def chunk_text(text: str, source: str, chunk_words: int = 110, overlap_words: int = 20) -> list[Chunk]:
    if chunk_words <= 0:
        raise ValueError("chunk_words must be greater than zero")
    if overlap_words < 0 or overlap_words >= chunk_words:
        raise ValueError("overlap_words must be >= 0 and < chunk_words")
    words = normalize_text(text).split()
    chunks = []
    step = chunk_words - overlap_words
    for start in range(0, len(words), step):
        part = words[start:start + chunk_words]
        if not part: break
        chunks.append(Chunk(f"{Path(source).stem}-{len(chunks)+1:04d}", source, " ".join(part)))
        if start + chunk_words >= len(words): break
    return chunks

def load_documents(folder: str | Path) -> list[tuple[str,str]]:
    folder = Path(folder)
    if not folder.exists():
        raise FileNotFoundError(f"Document folder not found: {folder}")
    docs = []
    for path in sorted(folder.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".txt",".md"}:
            body = path.read_text(encoding="utf-8")
            if normalize_text(body):
                docs.append((str(path.relative_to(folder)), body))
    return docs

def make_chunks(documents: Iterable[tuple[str,str]], chunk_words=110, overlap_words=20) -> list[Chunk]:
    return [c for source, body in documents for c in chunk_text(body, source, chunk_words, overlap_words)]
