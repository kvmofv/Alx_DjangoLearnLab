the project contains api APP
api APP has two models Book and Author
It has also serializers

for views:
we have 5 different views:
BookListView for listing all books, all users has access
BookDetailview for listing book details, all users has access
BookCreateView for creating a book, access for authenticated users only and also has acustom validation for user input title field.
BookUpdateView for updating a book, access for authenticated users only abd aso has access validaton for user input; title field.
BookDeleteView for deleting a book, access for authenticated users only abd aso has access validaton for user input; title field.

for filtering:
BookListView has filterset_fields that include all Book model fields to filter by.(GET /api/books/?author=Orwell or
GET /api/books/?publication_year=2020
)
BookListView has search_fields that provide for users searching by title and author's name.(GET /api/books/?search=george
)
BookListView has ordering_fields that provide users with ordering by title and publication year. (GET /api/books/?ordering=publication_year
)