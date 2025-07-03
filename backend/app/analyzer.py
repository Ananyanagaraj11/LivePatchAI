import hashlib
import random

def analyze_commit(repo: str, pusher: str, commit_msg: str) -> dict:
    """
    Simulates an intelligent analysis of a GitHub commit.
    """

    # Generate short commit ID from the message
    commit_hash = hashlib.sha256(commit_msg.encode()).hexdigest()[:10]

    # Categorize commit type based on keywords
    lower_msg = commit_msg.lower()
    categories = {
        "bugfix": ["fix", "bug", "resolve", "patch"],
        "feature": ["add", "implement", "new", "create"],
        "refactor": ["refactor", "clean", "optimize"],
        "docs": ["doc", "readme", "comment"],
        "testing": ["test", "ci", "coverage"],
        "infra": ["docker", "pipeline", "deploy", "yaml"]
    }

    matched_tags = []
    for tag, keywords in categories.items():
        if any(kw in lower_msg for kw in keywords):
            matched_tags.append(tag)

    if not matched_tags:
        matched_tags.append("general")

    # Simulated score (later can be AI-based)
    score = random.randint(70, 100)

    return {
        "commit_id": commit_hash,
        "repo": repo,
        "pusher": pusher,
        "message": commit_msg,
        "tags": matched_tags,
        "score": score,
        "status": "analyzed"
    }
