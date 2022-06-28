from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


# create database tables
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# APIs
@app.get("/cars/")
def read_cars(db: Session = Depends(get_db)):
    db_cars = crud.get_cars(db)
    return db_cars


@app.get("/cars/{id}")
def read_car(id:int, db: Session = Depends(get_db)):
    db_car = crud.get_car_by_id(db, car_id=id)
    # car 가 있으면 보여줌
    if db_car:
        return db_car
    # 없으면 not found error
    return HTTPException(status_code=400, detail=f"Car with id {id} is not found")


@app.post("/cars/")
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = crud.get_car_by_number(db, car_number=car.number)
    # car 가 이미 있으면 error
    if db_car:
        return HTTPException(status_code=400, detail=f"Already exist")
    return crud.create_car(db, car=car)









@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


