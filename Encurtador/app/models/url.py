from sqlalchemy import func
from app.extensions import db

class URL(db.Model):
    __tablename__ = "urls"

    id = db.Column(db.Integer, primary_key=True)
    original_url: str = db.Column(db.String(500), nullable=False)
    short_code: str = db.Column(db.String(10), unique=True, nullable=False)
    owner_id: str = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    hits = db.Column(db.Integer, default=0)

    def __init__(self, original_url: str, short_code: str, owner_id: str) -> None:
        self.original_url: str = original_url
        self.short_code: str = short_code
        self.owner_id: str = owner_id