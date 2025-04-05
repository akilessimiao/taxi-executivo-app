from flask import Blueprint, request

bp = Blueprint('webhook', __name__)

@bp.route('/webhook', methods=['POST'])
def receber_webhook():
    dados = request.json
    print("Webhook recebido:", dados)
    return {"status": "ok"}, 200
