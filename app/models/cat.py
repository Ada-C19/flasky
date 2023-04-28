from app import db

class Cat(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String)
  color = db.Column(db.String)
  personality = db.Column(db.String)

  def make_cat_dict(self):
    return dict(
        id=self.id,
        name=self.name,
        color=self.color,
        personality=self.personality
    )