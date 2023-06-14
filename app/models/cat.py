from app import db

class Cat(db.Model):
    id = db.Column(
            db.Integer, 
            primary_key=True, 
            autoincrement=True)
    name = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    personality = db.Column(db.String, nullable=False)
    pet_count = db.Column(db.Integer, nullable=False, default=0)
    caretaker_id = db.Column(db.Integer, db.ForeignKey("caretaker.id"))
    caretaker = db.relationship("Caretaker", back_populates="cats")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "personality": self.personality,
            "pet_count": self.pet_count
        }
    
    @classmethod
    def from_dict(cls, data_dict):
        new_cat = cls(
            name = data_dict["name"],
            color = data_dict["color"],
            personality = data_dict["personality"]
        )

        if "pet_count" in data_dict:
            new_cat.pet_count = data_dict["pet_count"]

        return new_cat