# Picasso Test Project

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Async File Processing](#async-file-processing)
- [Docker Setup](#docker-setup)
- [Contributing](#contributing)
- [License](#license)

## Introduction
ARSY is a Django-based web application that provides a file upload and processing feature. It uses Django REST framework for creating APIs and Celery for asynchronous file processing.

## Features
- File upload and processing.
- List all uploaded files with their processing status.
- Docker-compose setup for easy deployment.
- Asynchronous file processing with Celery.
- RESTful API endpoints.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed.
- Docker and Docker Compose installed.

## Getting Started
1. Clone this repository to your local machine.
2. Create a virtual environment and activate it.
3. Install project dependencies using `pip install -r requirements.txt`.
4. Set up the database and apply migrations: `python manage.py migrate`.
5. Run the development server: `python manage.py runserver`.

## Usage
- Access the web application at `http://localhost:8000`.
- Use the provided API endpoints for file upload and listing.
- Check the [API Endpoints](#api-endpoints) section for more details.

## API Endpoints
- File Upload: `POST /api/upload/`
```python
import requests

url = "http://127.0.0.1:8000/api/v1/upload/"

payload = {'title': 'Model',
'description': 'Simply model',
'owner': '1'}
files=[
  ('file',('hard_drive.glb',open('/D:/Download/hard_drive.glb','rb'),'application/octet-stream'))
]
headers = {
  'Authorization': 'Bearer Fez3KA0sKs'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```

## Async File Processing
- File processing is done asynchronously using Celery.
- Uploaded files are queued for processing.
- The processing status is updated when complete.

## Docker Setup
To run the project in Docker containers, follow these steps:
1. Ensure Docker and Docker Compose are installed.
2. Run `docker-compose up -d --build` to build and start the containers.
3. Access the application at `http://localhost:8000`.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License.

## Start development server at http://127.0.0.1:8000/admin***

## For API documentation goto http://127.0.0.1:8000/redoc or http://127.0.0.1:8000/swagger***
