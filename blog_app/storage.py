import json
from pathlib import Path
from uuid import uuid4

BASE_DIR = Path(__file__).resolve().parent
ARTICLES_DIR = BASE_DIR / "articles"
ARTICLES_DIR.mkdir(exist_ok=True)


def list_articles():
    """Return a list of all articles sorted by published date descending."""
    articles = []
    for path in ARTICLES_DIR.glob("*.json"):
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            articles.append(data)
    articles.sort(key=lambda a: a.get("published", ""), reverse=True)
    return articles


def get_article(article_id):
    """Return a single article dict by id, or None if not found."""
    path = ARTICLES_DIR / f"{article_id}.json"
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def create_article(title, content, published):
    """Create a new article and return its id."""
    article_id = str(uuid4())
    article = {
        "id": article_id,
        "title": title,
        "content": content,
        "published": published,
    }
    path = ARTICLES_DIR / f"{article_id}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(article, f, ensure_ascii=False, indent=2)
    return article_id


def update_article(article_id, title, content, published):
    """Overwrite an existing article file."""
    path = ARTICLES_DIR / f"{article_id}.json"
    if not path.exists():
        return False

    article = {
        "id": article_id,
        "title": title,
        "content": content,
        "published": published,
    }
    with path.open("w", encoding="utf-8") as f:
        json.dump(article, f, ensure_ascii=False, indent=2)
    return True


def delete_article(article_id):
    """Delete an article file."""
    path = ARTICLES_DIR / f"{article_id}.json"
    if path.exists():
        path.unlink()
        return True
    return False

