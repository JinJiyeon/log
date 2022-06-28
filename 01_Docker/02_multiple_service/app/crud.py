from sqlalchemy.orm import Session

from . import models, schemas


def get_cars(db: Session):
    return db.query(models.Car).all()


def get_car_by_id(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()


def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(**car.dict())
    # db_car = models.Car(name=car.name, number=car.number)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_car_by_number(db: Session, car_number: str):
    return db.query(models.Car).filter(models.Car.number == car_number).first()

