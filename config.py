from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

APP_NAME = "Industrial AI Engineer"
APP_VERSION = "0.1.0"

DATA_DIR = BASE_DIR / "data"
INTERNAL_DATA_DIR = DATA_DIR / "internal"
EXTERNAL_RESEARCH_DIR = DATA_DIR / "external_research"
EXCHANGE_DIR = DATA_DIR / "exchange"

DIGITAL_TWINS_DIR = BASE_DIR / "digital_twins" / "library"
REPORTS_DIR = BASE_DIR / "reports"

LOCAL_LLM_PROVIDER = "ollama"
LOCAL_LLM_MODEL = "qwen2.5:7b"

OLLAMA_BASE_URL = "http://localhost:11434"

DEBUG = True