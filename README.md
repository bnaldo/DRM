# Mini Teachable Platform

This repository contains a minimal FastAPI application that mimics basic features of a Teachable-like platform.

## Features
- List existing courses
- Create new courses
- Retrieve course details
- Add lessons to a course

## Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/` for a simple HTML preview of courses or
`http://localhost:8000/docs` for the interactive API docs.

## Running Tests

```bash
pytest
```
