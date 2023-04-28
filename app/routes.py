from flask import Blueprint, jsonify, abort, make_response


# class Cat:
#     def __init__(self, id, name, color, personality):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.personality = personality

#     def make_cat_dict(self):
#         return dict(
#             id=self.id,
#             name=self.name,
#             color=self.color,
#             personality=self.personality,
#         )


# cats = [
#     Cat(1, "Pepper", "black", "spicy"),
#     Cat(2, "Constance", "black", "cold and distant"),
#     Cat(3, "Rhubarb", "white & gray", "extra spicy"),
#     Cat(4, "Kiki", "gray", "tender and sweet"),
# ]

bp = Blueprint("cats", __name__, url_prefix="/cats")


def validate_cat(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"{id} was invalid"}, 400))

    for cat in cats:
        if cat.id == id:
            return cat
    return abort(make_response({"message": f"Cat with id {id} was not found"}, 404))


@bp.route("/<id>", methods=["GET"])
def handle_cat(id):
    cat = validate_cat(id)

    return cat.make_cat_dict()


# @bp.route("", methods=["GET"])
# def handle_cats():
#     result_list = []

#     for cat in cats:
#         result_list.append(cat.make_cat_dict())

#     # result_list = [make_cat_dict(cat) for cat in cats]

#     return jsonify(result_list)
