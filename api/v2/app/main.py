from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import schemas, crud
from app.db.session import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/batches/', response_model=schemas.Batch)
def create_batch(batch: schemas.BatchCreate, db: Session = Depends(get_db)):
    return crud.create_batch(db=db, batch=batch)
