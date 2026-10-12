
import os
from pathlib import Path
from dotenv import load_dotenv


# Project root: document-ingestion-engine/
PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")


def get_env_bool(name: str, default: bool) -> bool:
    """Read a boolean environment variable safely."""
    value = os.getenv(name)

    if value is None:
        return default

    normalized = value.strip().lower()

    if normalized in {"true", "1", "yes", "on"}:
        return True

    if normalized in {"false", "0", "no", "off"}:
        return False

    raise ValueError(
        f"{name} must be true or false, got: {value!r}"
    )


# Model configuration
DEFAULT_MODEL_ID = "Qwen/Qwen3-Embedding-0.6B"

EMBEDDING_MODEL_ID = os.getenv(
    "EMBEDDING_MODEL_ID",
    DEFAULT_MODEL_ID,
).strip()

EMBEDDING_MODEL_PATH = os.getenv(
    "EMBEDDING_MODEL_PATH",
    "",
).strip()

EMBEDDING_OFFLINE = get_env_bool(
    "EMBEDDING_OFFLINE",
    True,
)
