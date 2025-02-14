from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.get("/items/", response_model=List[schemas.Item], summary="Получить список всех товаров")
def get_items(db: Session = Depends(get_db)):
    return crud.get_items(db)


@router.post("/items/", response_model=schemas.Item, summary="Добавить новый товар")
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, **item.dict())


@router.delete("/delete/{item_id}/", summary="Удалить товар")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_item(db=db, item_id=item_id)
