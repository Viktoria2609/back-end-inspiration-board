import pytest
from app import create_app
from app.db import db
import os

@pytest.fixture()
def app():
    os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:" 
    app = create_app({"TESTING": True})
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()
