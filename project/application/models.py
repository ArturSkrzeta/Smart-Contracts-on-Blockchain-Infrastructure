from application import db # as if from __init__ import db

class Block(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String, nullable=False)
    previous_hash = db.Column(db.String, nullable=False)
    contract = db.Column(db.String,nullable=False)
    contracts_so_far_hashed = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.contracts_so_far_hashed}'
