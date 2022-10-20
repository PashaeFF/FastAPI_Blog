from typing import List
from fastapi import APIRouter ,Depends, status, Response, HTTPException

from blog.oauth2 import get_current_user
from .. import schemas, models
from ..database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix = '/blog',
    tags = ['Blogs']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    return blog.create(request, db)
   

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id,  response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.show(id, db)
    

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id, request, db)