from flask import Blueprint, jsonify, abort, make_response, request
from app.models.cat import Cat
from app import db

bp = Blueprint("cats", __name__, url_prefix="/cats")

# GET ALL ENDPOINT
@bp.route("", methods=["GET"])
def handle_cats():
  cats = Cat.query.all()
  cats_list = []
  for cat in cats:
    cats_list.append(cat.make_cat_dict())
  
  return jsonify(cats_list), 200

# CREATE ENDPOINT
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

  return make_response(f"Cat {new_cat.name} successfully created", 201)

# GET ONE ENDPOINT
@bp.route("/<id>", methods=["GET"])
def handle_cat(id):
    cat = validate_cat(id)

    return jsonify(cat.make_cat_dict()), 200

# UPDATE ONE ENDPOINT
@bp.route("/<id>", methods=["PUT"])
def update_cat(id):
    cat = validate_cat(id)
    request_body = request.get_json()

    cat.color = request_body["color"]
    cat.personality = request_body["personality"]
    cat.name = request_body["name"]
    
    db.session.commit()

    return make_response(f"Cat {cat.name} successfully updated", 200)


# DELETE ONE ENDPOINT
@bp.route("/<id>", methods=["DELETE"])
def delete_cat(id):
  cat = validate_cat(id)

  db.session.delete(cat)
  db.session.commit()

  return make_response(f"Cat {cat.name} successfully deleted", 200)

# HELPER FUNCTIONS
def validate_cat(id):
  try:
      id = int(id)
  except:
    abort(make_response({"message": f"{id} was invalid"}, 400))

  cat = Cat.query.get(id)
  
  if not cat:
    abort(make_response({"message": f"Cat with id {id} was not found"}, 404))

  return cat
