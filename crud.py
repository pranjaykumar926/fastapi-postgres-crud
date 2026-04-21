from sqlalchemy.orm import Session
import models
import schemas

# CREATE
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        author=book.author
    )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


# READ ALL
def get_books(db: Session):
    return db.query(models.Book).all()


# READ ONE
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()


# UPDATE
def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()

    if db_book:
        db_book.title = book.title
        db_book.author = book.author

        db.commit()
        db.refresh(db_book)

    return db_book


# DELETE
def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()

    if db_book:
        db.delete(db_book)
        db.commit()

    return db_book