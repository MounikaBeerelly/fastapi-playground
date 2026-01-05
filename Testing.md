### What is Testing ?
- It is a way for us to make sure our application is working as intended.
- Part of the SDLC that aims to identify
    - Bugs
    - Errors
    - Defects
- 3 different ways of testing
    - Manual Testing
    - Unit Testing
    - Integration Testing

#### Unit Testing :
- Unit testing involves testing individual components or units of software in isolation from the rest of the application.
- It validates that each unit of the software performs as designed.
- So each unit is testable part of the application.
- Developers write unit tests during the development phase.
- These tests are automated and executed by some type of testing framework (Pytest).
- And it has the benefit to identify bugs early in the development process.

#### Integration testing.
- Integration testing focuses on testing the interactions between different units or components of the piece of software.
- The scope for integration testing is a bit broader than unit testing, as we are testing multiple units together.
- This helps identify problems for the entire solution.
- So for example, we call an API endpoint and make sure that the correct solution is returned.

### Pytest :
- It is a popular testing framework for Python.
- It's known for simplicity, scalability, and ability to handle both unit and integration tests.
- Some reasons to why you should use Pytest.
    - It's simple and flexible - native assertions
    - It has fixtures - which is known as a feature to set up and tear down objects and other dependencies,
    - parameterized testing - Run same tests with different data.

#### setup :
- CReate a new directory on our project call `test`.
- Inside our test directory create a new files called : `__init__.py` and `test_example.py`
- Pytest will run all tests automatically that sit within files that have the name test in them and have the name `test` in them.
- When we write tests for our application, we will create new tests from a new file that matches
the naming convention of the project.
- For example : `todos.py` file will be tested by something called `test_todos.py`.