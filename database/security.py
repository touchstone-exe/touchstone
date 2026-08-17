import hashlib
import json


def generate_proof_card_hash(data: dict) -> str:
    """
    Generate a SHA-256 hash for Proof Card data.
    """

    canonical_data = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
    )

    return hashlib.sha256(
        canonical_data.encode("utf-8")
    ).hexdigest()