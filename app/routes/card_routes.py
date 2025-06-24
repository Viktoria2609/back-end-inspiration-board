from flask import Blueprint, request, abort, make_response, Response, jsonify
from app.models.card import Card
from ..db import db
from .helper_routes import validate_model, helper_model_from_dict, helper_get_sorted_query

bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

@bp.post("")
def create_card():
    request_body = request.get_json()
    return helper_model_from_dict(Card, request_body)

@bp.get("")
def get_all_cards():
    sort_param = request.args.get("sort")
    query = helper_get_sorted_query(Card, sort_param)
    cards = db.session.execute(query).scalars()
    card_list = [card.to_dict() for card in cards]
    return card_list

@bp.get("/<card_id>")
def get_one_card(card_id):
    card = validate_model(Card, card_id)
    return {"card": card.to_dict()}

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