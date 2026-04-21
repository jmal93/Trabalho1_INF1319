from app.extensions import db
from app.models.url import URL


def increment_hits(url_entry: URL) -> None:
    url_entry.hits += 1
    db.session.commit()