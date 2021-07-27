import os

s1: str | None = os.environ.get(
    "FOO"
)  # Fail Slow returns None when environment variable is missing or typo
s: str = os.environ[
    "FOO"
]  # Fail fast blow right away by raising key error if env var missing or typo
