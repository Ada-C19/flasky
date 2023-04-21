from flask import Blueprint, jsonify

class Cat:
    def __init__(self, id, name, color, personality):
        self.id = id
        self.name = name
        self.color = color
        self.personality = personality
        
cats = [
    Cat(1, "Pepper", "black", "spicy"),
    Cat(2, "Constance", "black", "cold and distant"),
    Cat(3, "Rhubarb", "white & gray", "extra spicy"),
    Cat(4, "Kiki", "gray", "tender and sweet"),
]

bp = Blueprint("cats", __name__, url_prefix="/cats")

@bp.route("", methods=["GET"])
def handle_cats():
    result_list = []

    for cat in cats:
        result_list.append(dict(
            id=cat.id,
            name=cat.name,
            color=cat.color,
            personality=cat.personality,
        ))

    # result_list = [make_cat_dict(cat) for cat in cats]

    return jsonify(result_list)

# def make_cat_dict(cat):
#      return dict(
#                 id=cat.id,
#                 name=cat.name,
#                 color=cat.color,
#                 personality=cat.personality,
#             )
