# 📘 **Guestbook** – Wiktoria & Marta

**Guestbook** is a simple web application created using **Flask** and **MySQL**.  
It allows users to enter their name and a message, which are then displayed below the form.

---

## Table of Contents

- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Installation with Docker](#installation-with-docker)
- [Testing](#testing)  

---

## Features

- 📝 Form for entering a **name** and **message** 
- 📜 Displaying a list of entries with names and messages  
- 💾 Data stored in a **MySQL** database    
- 🚀 Integration with GitHub Actions (CI)  

---

## Requirements

- Python 3.8 or newer  
- pip  
- MySQL (locally or in a Docker container)  
- virtualenv (optional)  
- Docker (if you want to run the database in a container)  

---

## Installation

1. Clone the repository:

```bash
git clone git@github.com:your_username/myapp.git
cd myapp
```

2. Install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run MySQL in Docker:
   
```bash
docker run --name myapp-mysql -e
MYSQL_ROOT_PASSWORD=rootpassword -e
MYSQL_DATABASE=myapp -p 3306:3306 -d mysql:latest
```

4. Create an `.env` file and configure it.

5. Run the application:
   
```bash
export FLASK_APP=app.py      
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5001
```

---

## Installation with Docker

To make it easier to run the application along with the database, a `docker-compose.yml` file is included, which will automatically build and start all necessary services in production mode.

1. Make sure you have **Docker** and **Docker Compose** installed and running.

2. Create an `.env` file based on `.env.example` and configure the environment variables in it.

3. In the terminal, navigate to the directory where the `docker-compose.yml` file is located (e.g., the `app` directory):

   ```bash
   cd app
   ```

4. Run the application and database with the command:

   ```bash
   docker-compose up --build
   ```

After completing these steps, the application will be available at `http://localhost:5001`.


*PS* 🔧 If you are using an external Docker network named `mynet` (defined in `docker-compose.yml`), make sure it has been created beforehand:
```bash
docker network create mynet
```
This command only needs to be executed once, before running the application for the first time. If the network already exists, you do not need to do this again.

---

## Testing

To run the application tests, execute the following command in the terminal:

```bash
pytest
```

Make sure you have the virtual environment (`venv`) activated and all dependencies installed before running the tests.
