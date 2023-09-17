Using the API

Endpoints:
GET /books: Retrieve a list of all books in the library.
POST /books: Create a new book and add it to the library.
GET /books/int:id: Retrieve information about a specific book by its ID.
PUT /books/int:id: Update information for a specific book.
DELETE /books/int:id: Delete a book from the library by its ID.

Making Requests:
Open Postman or your preferred API testing tool.
Create requests using the following URLs and HTTP methods:

GET All Books: GET http://34.163.16.189:5000/books
This will retrieve a list of all books in the library.

Create a New Book: POST http://34.163.16.189:5000/books
Set the request body to JSON or form data with the author and title fields to create a new book.

GET a Single Book: GET http://34.163.16.189:5000/books/<int:id>
Replace <int:id> with the ID of the book you want to retrieve.

Update a Book: PUT http://34.163.16.189:5000/books/<int:id>
Replace <int:id> with the ID of the book you want to update. Set the request body with the author and title fields to update the book's information.

Delete a Book: DELETE http://34.163.16.189:5000/books/<int:id>
Replace <int:id> with the ID of the book you want to delete.
