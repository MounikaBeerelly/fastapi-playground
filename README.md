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

### Installation of SQLite3 Terminal in Windows :
1. Open `https://www.sqlite.org/index.html`
2. Click on Download
3. Go to **Precompiled Binaries for Windows**
4. Click on `sqlite-tools-win-x86-3510100.zip
(4.08 MiB)`

### What is a JSON Web Token ?
- JSON web token is a self-contained way to securely transmit data and information between two parties using a JSON object.
- JSON web tokens can be trusted because each JWT can be digitally signed, which in return allows the server to know if the JWT has been changed at all.
- JWT should be used when dealing with authorization.
- JWT is a great way fro information to be exchanges between the server and client.

#### JSON Web token structure :
- A JSON web token is created of three seperate parts seperated by dots (.) which include :
    - Header : (a)
    - Payload : (b)
    - Signature : (c)
        - `aaaaaaaa.bbbbbbbb.cccccccc`
- **JWT Header**
    - A JWT header usually consists of two parts :
        - (alg) the algorithm for signing
        - "typ" the specific type of token
            ```
                {
                    "alg" : "HS256",
                    "typ" : "JWT"
                }
            ```
    - The JWT header is then encoded using Base64 to create the first part of the JWT (a)
- **JWT Payload**
    - A JWT payload consists of the data. The payloads data contains claims, and there are three different types of claims.
        - Registered
        - Public
        - Private
            ```
                {
                    "sub" : "1234567890",
                    "name" : "John doe",
                    "given_name" : "John",
                    "family_name" : "Doe",
                    "email" : "john@gmail.com",
                    "admin" : true
                }
            ```
    - The JWT payload is then encoded using Base64 to create the second part of the JWT (b)
- **JWT Signature**
    - A JWT Signature is created by using the algorithm in the header to hash out the encoded header, encoded payload with a secret.
    - The secret can be anything, but is saved somewhere on the server that the client does not have access to
            ```
               HMACSHA256(
                base64UrlEncode(header) + "." +
                base64UrlEncode(payload),
                secret)
            ```
    - The Signature is the third and final part of a JWT (c).
    
### What is POSTGRESQL :
- Production ready database
- Open source Relational database management system
- Secure
- Requires a server
- Scalable

#### How to install PostgreSQL ?
1. Go to `https://www.postgresql.org/`
2. Open `Download` tab
3. Click on `Windows`
4. Click on `Download the Installer`
5. Download the latest version

### What is MYSQL ?
- Open source Relational databse management system.
- requires a server
- production ready
- scalable
- secure
#### How to install MySQL ?
- Go to `https://www.mysql.com/`
- Open `Developer Zone` tab
- Click on `Downloads -> MySQL Community Server`
- Download mysql

### What is Alembic ?
- Alembic is a lightweight database migration tool for when using SQL alchemy.
- Migration tools allow us to plan, transfer and upgrade resources within our database.
- Alembic allows you to change a SQLAlchemy database table after it has already been created.
- Currently SQL Alchemy will only create new database tables for us, not enhance any.

#### How does Alembic work?
- Alembic provides the creation and invocation of change management scripts.
- This allows you to be able to create migration environments and be able to change data however you like.

#### Setup Alembic into the project :
- Install Alembic using `pip install alembic`
- initialize alembic environment : `alembic init alembic`

#### Alembic commands :
| Alembic Command | Details |
|----------------- | ------- |
|alembic init `<folder name>` | Initializes a new, generic environment |
| alembic revision -m <message> | Creates a new version of the environment |
| alembic upgrade <revision #> | Run on upgrade migration to our database |
| alembic downgrade -1 | Run our downgrade migration to our database |

#### Alembic Revisions :
- Alembic revision is how we create a new alembic file where we can add some type of database upgrade.
- When we run : `alembic revision -m "create phone number col on users table"`
- Creates a new file where we can write the upgrade code.
- Each new version will have a Revision Id

#### Alembic Upgrade ?
- Alembic upgrade is how we actually run the migration
```
    def upgrade() -> None :
        op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
```
- Enhances our database to now have a new column within our users tables called `phone_number`.
- Previous data in the database will not change.
- To run the upgrade migration : `alembic upgrade <revision id>`

#### Alembic Downgrade ?
- Alembic downgrade is how we revert a migration
```
    def downgrade() -> None :
        op.drop_column('users', 'phone_number')
```
- Reverts our database to remove the last migration change.
- Previous data within database does not change unless it was on the column `phone_number` because we deleted it.
- To run the downgrade migration : `alembic downgrade -1`