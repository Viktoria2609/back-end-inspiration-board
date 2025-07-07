from flask import Blueprint, request, jsonify
from ..db import db
from app.models.board import Board
from app.models.card import Card
from .helper_routes import validate_model, validate_board_data, validate_card_data


bp = Blueprint("boards_bp", __name__, url_prefix="/boards")

@bp.post("")
def create_board():
    data = request.get_json()
    validate_board_data(data)

    new_board = Board(
        title=data["title"],
        owner=data["owner"]
    )

    db.session.add(new_board)
    db.session.commit()

    return jsonify(new_board.to_dict()), 201

@bp.get("")
def get_all_boards():
    boards = db.session.execute(db.select(Board)).scalars().all()
    return [board.to_dict() for board in boards], 200

@bp.get("/<board_id>")
def get_board(board_id):
    board = validate_model(Board, board_id)
    return board.to_dict(), 200

@bp.post("/<board_id>/cards")
def create_card_for_board(board_id):
    board = validate_model(Board, board_id)
    data = request.get_json()
    validate_card_data(data)

    new_card = Card(
        message=data["message"],
        board_id=board.id
    )

    db.session.add(new_card)
    db.session.commit()

    return new_card.to_dict(), 201

@bp.get("/<board_id>/cards")
def get_cards_for_board(board_id):
    board = validate_model(Board, board_id)
    cards = [card.to_dict() for card in board.cards]

    return {
        "id": board.id,
        "title": board.title,
        "owner": board.owner,
        "cards": cards
    }, 200

@bp.delete("/<board_id>")
def delete_board(board_id):
    board = validate_model(Board, board_id)

    db.session.delete(board)
    db.session.commit()

    return "", 204