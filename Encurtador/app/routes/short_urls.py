from flask import Blueprint, request, jsonify
from app.services.shortener_service import create_short_url, get_url_by_short_code

short_urls_bp = Blueprint("short_urls", __name__)

@short_urls_bp.route('/api/v3/short-urls', methods=['POST'])
def encurtar():
    """
    Cria um novo link encurtado
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            url:
              type: string
              example: "https://google.com"
            owner-id:
              type: string
              example: "roger"
    responses:
      201:
        description: Link criado com sucesso
      400:
        description: Dados inválidos
    """
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
def get_short_url(short_code):
    """
    Obtém os dados de um link encurtado através do seu código
    ---
    parameters:
      - name: short_code
        in: path
        type: string
        required: true
        description: O código curto da URL (ex AbCdEf)
    responses:
      200:
        description: Detalhes encontrados
      404:
        description: URL não encontrada
    """
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