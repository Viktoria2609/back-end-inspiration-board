from ..db import db
from flask import abort, make_response

def validate_model(cls, model_id):

    try:
        model_id = int(model_id)
    except:
        response = { "message": f"{cls.__name__} {model_id} invalid" }
        abort(make_response(response, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {"message": f"{cls.__name__} {model_id} not found"}
        abort(make_response(response, 404))

    return model

def validate_board_data(data):
    if not data.get("title") or not data.get("owner"):
        response = {"details": "Invalid board data. 'title' and 'owner' are required."}
        abort(make_response(response, 400))

def validate_card_data(data):
    message = data.get("message")
    if not message or len(message) > 40:
        response = {"details": "Invalid card message. Must be 1–40 characters."}
        abort(make_response(response, 400))

