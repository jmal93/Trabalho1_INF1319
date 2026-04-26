from typing import Any

from app.extensions import db
from app.models.url import URL
from app.utils.code_generator import generate_short_code

def create_short_url(original_url: str, owner_id: str) -> URL:
    short_code: str = _generate_unique_code()

    new_url = URL(
        original_url=original_url,
        short_code=short_code,
        owner_id=owner_id
    )

    db.session.add(new_url)
    db.session.commit()
    return new_url

def get_url_by_short_code(short_code: str) -> URL | None:
    return URL.query.filter_by(short_code=short_code).first()

def _generate_unique_code():
    while True:
        code = generate_short_code()
        exists = get_url_by_short_code(short_code=code)
        if not exists:
            return code

def delete_url(short_code: str) -> bool:
    url = get_url_by_short_code(short_code=short_code)

    if not url:
        return False

    db.session.delete(url)
    db.session.commit()
    
    return True