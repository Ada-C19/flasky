from app import db


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    personality = db.Column(db.String)
    caretaker = db.relationship("Caretaker", back_populates="cats")
    caretaker_id = db.Column(db.Integer, db.ForeignKey("caretaker.id"))

    @classmethod
    def from_dict(cls, data_dict, caretaker):
        return cls(
            name=data_dict["name"],
            color=data_dict["color"],
            personality=data_dict["personality"],
            caretaker=caretaker

        )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            color=self.color,
            personality=self.personality
        )        
    
