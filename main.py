from sqlmodel import SQLModel, Field, create_engine, Session, Relationship, select

engine = create_engine("sqlite:///orm.db")


class Author(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, max_length=50)
    email: str = Field(nullable=False, max_length=50)

    books: list["Book"] = Relationship(back_populates="author")


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(nullable=False, max_length=100)
    content: str
    author_id: int = Field(foreign_key="author.id")

    author: Author = Relationship(back_populates="books")


SQLModel.metadata.create_all(engine)

####CREATE TABLE'S WITH MODEL INFO AND ADD DATA TO IT####
# with Session(engine) as session:
#     author1 = Author(name='Alice',email='alice@example.com')
#     author2 = Author(name='Bob',email='bob@example.com')
#     book1=Book(title='Alice´s First Book',content='This is the content of Alice´s First Book.',author=author1)
#     book2=Book(title='Alice´s Second Book',content='This is the content of Alice´s Second Book.',author=author1)
#     book3=Book(title='Bob´s First Book',content='This is the content of Bob´s First Book.',author=author2)
#
#     session.add_all([author1,author2,book1,book2,book3])
#     session.commit()

####FIRST WAY####
# with Session(engine) as session:
#     statement=select(Book)
#     result = session.exec(statement)
#     for book in result:
#         print(book.title)

####RESUMED WAY####
# with Session(engine) as session:
#     statement=select(Book)
#     results = session.exec(statement).all()
#     print(results)

####ULTRA MEGA RESUMED WAY####
# with Session(engine) as session:
#     results = session.exec(select(Book)).all()
#     print(results)

####SELECT BY BOOK TITLE####
# with Session(engine) as session:
#     statement=select(Book).where(Book.title=="Alice´s First Book")
#     books = session.exec(statement).all()
#     for book in books:
#         print(book.title)

####SEARCH BOOKS BY AUTHOR AND SHOW BOOK/AUTHOR NAME####
# with Session(engine) as session:
#     statement = select(Book, Author).join(Author)
#     books_with_authors = session.exec(statement).all()
#
#     for book, author in books_with_authors:
#         print(f"Book: {book.title}, Author: {author.name}")

####UPDATE BOOK TITLE
# with Session(engine) as session:
#     book_to_update = session.exec(
#         select(Book).where(Book.title == "Alice´s First Book")
#     ).first()
#     if book_to_update:
#         book_to_update.title = "Alice´s Updated First Book"
#         session.add(book_to_update)
#         session.commit()
#         session.refresh(book_to_update)
#         print(f"Updated book: {book_to_update.title}")

####DELETE BOOK####
# with Session(engine) as session:
#     book_to_delete = session.exec(
#         select(Book).where(Book.title == "Alice´s Updated First Book")
#     ).first()
#     if book_to_delete:
#         session.delete(book_to_delete)
#         session.commit()
