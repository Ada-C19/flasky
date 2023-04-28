from flask import Blueprint, jsonify, abort, make_response, request
from app.models.cat import Cat
from app import db

bp = Blueprint("cats", __name__, url_prefix="/cats")

@bp.route("", methods=["GET"])
def handle_cats():
  cats = Cat.query.all()
  cats_list = []
  for cat in cats:
    cats_list.append(cat.make_cat_dict())
  
  return jsonify(cats_list), 200

@bp.route("", methods=["POST"])
def create_cat():
  request_body=request.get_json()

  new_cat = Cat(
    name=request_body["name"],
    color=request_body["color"],
    personality=request_body["personality"]
    )

  db.session.add(new_cat)
  db.session.commit()

  return make_response(f"Book {new_cat.name} successfully created", 201)