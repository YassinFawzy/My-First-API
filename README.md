# Using the Library API

## Endpoints

- **GET /books**: Retrieve a list of all books in the library.
- **POST /books**: Create a new book and add it to the library.
- **GET /books/int🆔**: Retrieve information about a specific book by its ID.
- **PUT /books/int🆔**: Update information for a specific book.
- **DELETE /books/int🆔**: Delete a book from the library by its ID.

## Making Requests

To interact with the API, follow these steps:

1. Open Postman or your preferred API testing tool.

2. Create requests using the following URLs and HTTP methods:

   - **GET All Books**: Retrieve a list of all books in the library.
     - Endpoint: `GET http://34.163.16.189:5000/books`
     - Description: This will retrieve a list of all books in the library.

   - **Create a New Book**: Create a new book and add it to the library.
     - Endpoint: `POST http://34.163.16.189:5000/books`
     - Description: Set the request body to JSON or form data with the `author` and `title` fields to create a new book.

   - **GET a Single Book**: Retrieve information about a specific book by replacing `int:id` with the ID of the book you want to retrieve.
     - Endpoint: `GET http://34.163.16.189:5000/books/int:id`
     - Description: Replace `int:id` with the ID of the book you want to retrieve.

   - **Update a Book**: Update information for a specific book by replacing `int:id` with the book's ID. Set the request body with the `author` and `title` fields to update the book's information.
     - Endpoint: `PUT http://34.163.16.189:5000/books/int:id`
     - Description: Replace `int:id` with the ID of the book you want to update.

   - **Delete a Book**: Delete a book from the library by replacing `int:id` with the book's ID.
     - Endpoint: `DELETE http://34.163.16.189:5000/books/int:id`
     - Description: Replace `int:id` with the ID of the book you want to delete.
