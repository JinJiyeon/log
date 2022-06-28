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





