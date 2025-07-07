from flask import Blueprint, request, abort, make_response, Response, jsonify
from app.models.card import Card
from ..db import db
from .helper_routes import validate_model
bp = Blueprint("cards_bp", __name__, url_prefix="/cards")


@bp.put("/<card_id>")
def update_card(card_id):
    card = validate_model(Card, card_id)
    request_body = request.get_json()

    card.message = request_body.get("message", card.message)
    card.likes_count = request_body.get("likes_count", card.likes_count)

    db.session.commit()
    return Response(status=204, mimetype="application/json")

@bp.patch("/<card_id>/like")
def like_card(card_id):
    card = validate_model(Card, card_id)
    card.likes_count += 1
    db.session.commit()
    return {"card": card.to_dict()}, 200

@bp.delete("/<card_id>")
def delete_card(card_id):
    card = validate_model(Card, card_id)
    db.session.delete(card)
    db.session.commit()
    return Response(status=204, mimetype="application/json")