from sqlalchemy.orm import Session
from .. import models
from fastapi import status, HTTPException

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request, db: Session):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id ==id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with the id {id} is not available")
    return blog

def destroy(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id ==id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with the id {id} is not available")
    db.delete(blog)
    db.commit()
    return {'detail': 'done'}

def update(id, request, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id ==id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with the id {id} is not available")
    blog.update({'title': request.title, 'body': request.body }, synchronize_session= False)
    db.commit()
    return f'Blog {id} updated'

    
