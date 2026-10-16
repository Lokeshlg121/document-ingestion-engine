
from functools import lru_cache
from pathlib import Path

from sentence_transformers import SentenceTransformer

from document_ingestion.config.settings import (
    EMBEDDING_ALLOW_DOWNLOAD,
    EMBEDDING_MODE,
    EMBEDDING_MODEL_ID,
    EMBEDDING_MODEL_PATH,
    EMBEDDING_OFFLINE,
)


@lru_cache(maxsize=1)
def load_embedding_model() -> SentenceTransformer:
    """Load and cache a Sentence Transformers embedding model."""

    if EMBEDDING_MODE == "local":
        if not EMBEDDING_MODEL_PATH:
            raise ValueError(
                "EMBEDDING_MODEL_PATH is required when "
                "EMBEDDING_MODE=local."
            )

        model_location = Path(EMBEDDING_MODEL_PATH)

        if not model_location.is_dir():
            raise FileNotFoundError(
                f"Embedding model directory not found: {model_location}"
            )

        return SentenceTransformer(
            str(model_location),
            device="cpu",
            local_files_only=True,
        )

    if EMBEDDING_MODE == "hub":
        if not EMBEDDING_MODEL_ID:
            raise ValueError(
                "EMBEDDING_MODEL_ID is required when "
                "EMBEDDING_MODE=hub."
            )

        if EMBEDDING_OFFLINE and EMBEDDING_ALLOW_DOWNLOAD:
            raise ValueError(
                "Offline mode and model downloads cannot both be enabled."
            )

        if EMBEDDING_OFFLINE or not EMBEDDING_ALLOW_DOWNLOAD:
            return SentenceTransformer(
                EMBEDDING_MODEL_ID,
                device="cpu",
                local_files_only=True,
            )

        return SentenceTransformer(
            EMBEDDING_MODEL_ID,
            device="cpu",
        )

    if EMBEDDING_MODE == "api":
        raise NotImplementedError(
            "Remote API mode will be implemented separately."
        )

    raise ValueError(
        f"Unsupported EMBEDDING_MODE: {EMBEDDING_MODE!r}. "
        "Choose 'local', 'hub', or 'api'."
    )



def embed_texts(texts: list[str]) -> list[list[float]]:
    """Convert text strings into embedding vectors."""

    if not texts:
        return []

    if any(not text.strip() for text in texts):
        raise ValueError("Input texts must not contain empty strings.")

    model = load_embedding_model()

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    return embeddings.tolist()
