from flasgger import swag_from
from flask import Blueprint, jsonify, request

from app.models.url import URL
from app.services.shortener_service import create_short_url, get_url_by_short_code

short_urls_bp = Blueprint("short_urls", __name__)

@short_urls_bp.route('/api/v3/short-urls', methods=['POST'])
@swag_from('encurtar.yml')
def encurtar():
  data = request.get_json() or {}
  original_url = data.get("url")
  owner_id = data.get("owner-id")

  if not original_url or not owner_id:
      return jsonify({"error": "Campos 'url' e 'owner-id' são obrigatórios"}), 400

  new_url = create_short_url(original_url, owner_id)

  return jsonify({
      "short_url": f"http://localhost:5000/{new_url.short_code}"
  }), 201


@short_urls_bp.route('/api/v3/short-urls/<short_code>', methods=['GET'])
@swag_from('get_short_url.yml')
def get_short_url(short_code):
  url_data = get_url_by_short_code(short_code)

  if not url_data:
      return jsonify({"error": "URL não encontrada"}), 404

  return jsonify({
      "original_url": url_data.original_url,
      "short_code": url_data.short_code,
      "owner_id": url_data.owner_id,
      "created_at": url_data.created_at.isoformat() if url_data.created_at else None,
      "hits": url_data.hits
  }), 200

@short_urls_bp.route('/api/v3/short-urls', methods=['GET'])
@swag_from('get_all_short_urls.yml')
def get_all_short_urls():
  pagination = URL.query.paginate(page=1, per_page=10, error_out=False)
  all_short_urls = pagination.items

  result = []
  for url in all_short_urls:
    result.append(
      {
        "original_url": url.original_url,
        "short_url": url.short_code,
        "owner_id": url.owner_id,
        "created_at": url.created_at.isoformat() if url.created_at else None,
        "hits": url.hits
      }
    )

  return result