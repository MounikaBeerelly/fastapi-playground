### Python Virtual Environments 
- A Python Virtual Environment (`venv`) is an isolated environment that lets you install and manage project-specific Python packages without affecting the global Python installation.
- This is essential for FastAPI (and any backend project).
#### Why Use Virtual Environments?
- Avoid dependency conflicts between projects
- Keep system Python clean
- Reproducible builds (requirements.txt)
- Different Python versions per project
### How to install dependencies
- Pip is the Python Package manager
- Pip is used to install and update packages
- make sure you have the latest version of pip installed
- Check the pip version `python -m pip --version`
- Check the installed packages using `pip list` command.

### Setting up Virtual Environment
1. Create virtual environment using - `python -m venv fastapienv`
2. Activate fastapi environment - `fastapienv\Scripts\activate.bat`
3. Check the list of packages - `pip list`
4. Install fastapi - `pip install fastapi`
5. Install uvicorn - `pip install "uvicorn[standard]"`
6. Deactivate environment - `deactivate`

### How to run the application
- Run the fastapi application using `uvicorn books:app --reload`
    - books - name of the file
    - app - app is an instance of the FastAPI class
        - It holds:
            - All routes (endpoints)
            - Middleware
            - Startup/shutdown events
            - Dependencies
    - Uvicorn runs this object
    
- URL of the application - `http://127.0.0.1:8000/`
- Swagger URL of the application - `http://127.0.0.1:8000/docs`

