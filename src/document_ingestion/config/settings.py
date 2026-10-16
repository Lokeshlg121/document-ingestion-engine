
import os
from pathlib import Path

from dotenv import load_dotenv


# Find the project root automatically.
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Load configuration from the project's .env file.
load_dotenv(PROJECT_ROOT / ".env")


def get_env_bool(name: str, default: bool) -> bool:
    """Read a Boolean environment variable."""
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


# Supported modes: local, hub, api.
EMBEDDING_MODE = os.getenv(
    "EMBEDDING_MODE",
    "local",
).strip().lower()

# Model identifier on Hugging Face or the configured provider.
EMBEDDING_MODEL_ID = os.getenv(
    "EMBEDDING_MODEL_ID",
    "Qwen/Qwen3-Embedding-0.6B",
).strip()

# Optional path to model files already stored on disk.
EMBEDDING_MODEL_PATH = os.getenv(
    "EMBEDDING_MODEL_PATH",
    "",
).strip()

# Whether remote model downloads are permitted.
EMBEDDING_ALLOW_DOWNLOAD = get_env_bool(
    "EMBEDDING_ALLOW_DOWNLOAD",
    False,
)

# Whether the model must operate without network access.
EMBEDDING_OFFLINE = get_env_bool(
    "EMBEDDING_OFFLINE",
    True,
)
