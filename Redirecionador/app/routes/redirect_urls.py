from flask import Blueprint, jsonify, redirect

from app.models.url import URL
from app.services.increment_hits_service import increment_hits


redirect_url_bp = Blueprint("redirect_urls", __name__)

@redirect_url_bp.route('/<short_code>', methods=['GET'])
def redirecionar(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first_or_404()

    increment_hits(url_entry=url_entry)
    
    return redirect(url_entry.original_url)

@redirect_url_bp.route('/stats/<short_code>', methods=['GET'])
def stats(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first_or_404()
    return jsonify({"hits": url_entry.hits})