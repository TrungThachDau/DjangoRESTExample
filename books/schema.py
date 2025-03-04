
import graphene
from graphene_django import DjangoObjectType
from books.models import Book, TypeBook

class TypeBookType(DjangoObjectType):
    class Meta:
        model = TypeBook
        fields = ('id', 'name')

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'pub_date','type')

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_types = graphene.List(TypeBookType)
    book_by_name = graphene.List(BookType, name=graphene.String(required=True))
    book_by_id = graphene.Field(BookType, id=graphene.Int(required=True))
    def resolve_all_books(self, info):
        try:
            books = Book.objects.all()
            return books
        except Exception as e:
            return e

    def resolve_book_by_name(self,info, name):
        return Book.objects.all().filter(title=name)

    def resolve_book_by_id(self,info,id):
        try:
            book = Book.objects.get(id=id)
            return book
        except Exception as e:
            return e

class BookInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    author = graphene.String(required=False)
    price = graphene.Decimal(required=False)
    publisher = graphene.String(required=False)
    pub_date = graphene.Date(required=False)
    type_id = graphene.Int(required=False)


class CreateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    def mutate(root, info, book_data=None):
        book = Book.objects.create(**book_data)
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    def mutate(root, info, id, book_data=None):
        book = Book.objects.get(id=id)
        for key, value in book_data.items():
            setattr(book, key, value)
        book.save()

        return UpdateBook(book=book)

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    book = graphene.Field(BookType)

    def mutate(root, info, id):
        book = Book.objects.get(id=id)
        book.delete()
        return DeleteBook(book=None)
class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)