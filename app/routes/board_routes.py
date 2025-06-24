from flask import Blueprint, request, jsonify
from ..db import db
from .helper_routes import validate_model
from app.models.board import Board
from app.models.card import Card

boards_bp = Blueprint("boards", __name__, url_prefix="/boards")

@boards_bp.post("")
def create_board():
    data = request.get_json()

    new_board = Board(
        title=data["title"],
        owner=data["owner"]
    )

    db.session.add(new_board)
    db.session.commit()

    return jsonify(new_board.to_dict()), 201

@boards_bp.get("")
def get_all_boards():
    boards = db.session.execute(db.select(Board)).scalars().all()
    return [board.to_dict() for board in boards], 200

@boards_bp.get("/<board_id>")
def get_board(board_id):
    board = validate_model(Board, board_id)
    return board.to_dict(), 200

@boards_bp.post("/<board_id>/cards")
def create_card_for_board(board_id):
    board = validate_model(Board, board_id)
    data = request.get_json()

    new_card = Card(
        message=data["message"],
        board_id=board.id
    )

    db.session.add(new_card)
    db.session.commit()

    return new_card.to_dict(), 201

@boards_bp.get("/<board_id>/cards")
def get_cards_for_board(board_id):
    board = validate_model(Board, board_id)
    cards = [card.to_dict() for card in board.cards]

    return {
        "id": board.id,
        "title": board.title,
        "owner": board.owner,
        "cards": cards
    }, 200
