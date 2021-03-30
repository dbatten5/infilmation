from typing import Any

import asyncio

from fastapi import APIRouter, Depends, BackgroundTasks, WebSocket
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas, crud, tasks
from app.models import Batch
from app.api.deps import get_db

router = APIRouter()


@router.post('/',  response_model=schemas.BatchCreateOut)
def create_batch(
    batch: schemas.BatchCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
) -> Any:
    db_batch = crud.create_batch(db=db, batch=batch)
    background_tasks.add_task(tasks.process_films, db, db_batch)
    return db_batch


@router.get('/{key}',  response_model=schemas.Batch)
def get_batch(key: str, db: Session = Depends(get_db)) -> Any:
    return crud.get_batch_by_key(db=db, key=key)


@router.websocket("/{key}/ws")
async def websocket_endpoint(
    key: str,
    websocket: WebSocket,
    db: Session = Depends(get_db)
) -> Any:
    await websocket.accept()
    while True:
        await asyncio.sleep(2)
        batch = crud.get_batch_by_key(db=db, key=key)
        db.refresh(batch)
        await websocket.send_json(jsonable_encoder(batch))
        if batch.status == 'finished':
            await websocket.close()
            return True
