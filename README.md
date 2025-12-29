# python-fastapi-playground

### What are Path Parameters ?
- Path Parameters are request parameters that have been attached to the URL.
- Path parameters are usually defined as a way to find information based on location.

### What are Query Parameters ?
- Query Parameters are request parameters that have beeen attached after a `?`.
- Query parameters have `name=value` pairs
- Example :
    - 127.0.0.1:8000/books/?category=math

### What is Pydantics ?
- Python library that is used for data modeling, data parsing and has efficient error handling.
- Pydantics is commonly used as a resource for data validation and how to handle data coming to our FastAPI application.

### What are Status Codes ?
- An HTTP status code is used to help the client (the user or system submitting data to the server) to understand what happened on the server side application.
- Status codes are international standatds on how a Client/Server should handle the result of a request.
- It allows evryone who sends a request to know if their submission was successful or not.
#### Status Codes :
1. `1xx` --> Information Response : Request Processing
2. `2xx` --> Success : Request Successfully complete
3. `3xx` --> Redirection : Further action must be complete
4. `4xx` --> Client Errors : An error was caused by the client
5. `5xx` --> Server Errors : An error occured ont he server

#### 2xx Successful Status Codes :
1. `200:OK` - Standard Response for a successful request. Commonly used for successful Get requests when data is being returned.
2. `201:Created` - The request has been successful, creating a new resource. Used when a POST creates an entity.
3. `204:No Content` - The request has been successful, did not create an entity noe return anything. Commonly used with PUT requests.

#### 4xx Error Status codes :
1. `400:Bad Request` - Cannot process request due to client error. Commonly used for invalid request methods.
2. `401:Unauthorized` - Client does not have valid authentication for target resource.
3. `404:Not found` - The client requested resource cannot be found.
4. `422:Unprocessable Entity` - Semantic errors in Client request

#### 5xx Server Status codes
1. `501: Internal Server Error` - Generic Error Message, when an unexpected issue on the server happened.

### SQLAlchemy
- SQLAlchemy is a popular Python SQL toolkit and ORM (Object Relational Mapper) used to interact with relational databases (PostgreSQL, MySQL, SQLite, Oracle, SQL Server, etc.) in a clean, Pythonic way.
- With SQLAlchemy 
    - Connect to databases
    - Write SQL queries using Python
    - Map database tables to Python classes (ORM)
    - Handle transactions, sessions, and relationships