import asyncio

from fastapi import FastAPI, Depends, BackgroundTasks, WebSocket
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from . import schemas, crud, tasks
from app.db.session import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/batches/{batch_key}',  response_model=schemas.Batch)
def get_batch(batch_key: str, db: Session = Depends(get_db)):
    return crud.get_batch_by_key(db=db, key=batch_key)


@app.websocket("/batches/{batch_key}/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    batch_key: str,
    db: Session = Depends(get_db)
):
    await websocket.accept()
    while True:
        await asyncio.sleep(2)
        batch = crud.get_batch_by_key(db=db, key=batch_key)
        db.refresh(batch)
        await websocket.send_json(jsonable_encoder(batch))
        if batch.status == 'finished':
            await websocket.close()
            return True


@app.post('/batches/',  response_model=schemas.BatchCreateOut)
def create_batch(
    batch: schemas.BatchCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    db_batch = crud.create_batch(db=db, batch=batch)
    background_tasks.add_task(tasks.process_films, db, db_batch)
    return db_batch
