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

def create_model_from_dict(cls, data):
    try:
        new_instance = cls.from_dict(data)

    except KeyError as error:
        response = { "details": "Invalid data"}
        abort(make_response(response, 400))

    db.session.add(new_instance)
    db.session.commit()

    model_name = cls.__name__.lower() 
    
    return {model_name: new_instance.to_dict()}, 201

