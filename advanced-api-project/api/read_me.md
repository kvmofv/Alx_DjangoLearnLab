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