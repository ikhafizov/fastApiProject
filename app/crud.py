from sqlalchemy.orm import Session
from app import models


def get_items(db: Session):
    return db.query(models.Item).all()


def create_item(db: Session, name: str, description: str, price: float):
    db_item = models.Item(name=name, description=description, price=price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item
