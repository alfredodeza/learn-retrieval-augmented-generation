"""Pre-download the Sentence Transformer model used by the notebooks."""

from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"


def main() -> None:
    """Download the embedding model used throughout the examples."""
    SentenceTransformer(MODEL_NAME)
    print(f"Downloaded Sentence Transformer model: {MODEL_NAME}")


if __name__ == "__main__":
    main()