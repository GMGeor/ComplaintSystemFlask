from sqlalchemy import func

from models.enums import ComplaintState

from db import db


class ComplaintModel(db.Model):
    __tablename__ = 'complaints'

    id = db.Column(db.Integer, primery_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_on = db.Column(db.Datetime, server_default=func.now)
    status = db.Column(db.Enum(ComplaintState), nullable=False, default=ComplaintState.pending)
    complainer_id = db.Column(db.Integer, db.ForeignKey("complainers.id"), nullable=False)
    complainer = db.relationship("ComplainerUserModel")