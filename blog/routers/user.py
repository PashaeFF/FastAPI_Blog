from fastapi import APIRouter ,Depends, status, HTTPException
from .. import schemas, models
from ..hashing import Hash
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix = '/user',
    tags = ['Users']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user(id: int, db:Session = Depends(get_db)):
    return user.show(id, db)