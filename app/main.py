from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import List

from .models import Course, CourseCreate, Lesson

app = FastAPI(title="Mini Teachable API")

courses: List[Course] = []
course_id_counter = 1


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    items = "".join(f"<li>{c.title}</li>" for c in courses)
    return (
        "<html><head><title>Mini Teachable</title></head><body>"
        "<h1>Courses</h1><ul>" + items + "</ul></body></html>"
    )


@app.get("/courses", response_model=List[Course])
def list_courses() -> List[Course]:
    return courses


@app.post("/courses", response_model=Course, status_code=201)
def create_course(course: CourseCreate) -> Course:
    global course_id_counter
    new_course = Course(id=course_id_counter, title=course.title, description=course.description, lessons=[])
    course_id_counter += 1
    courses.append(new_course)
    return new_course


@app.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int) -> Course:
    for c in courses:
        if c.id == course_id:
            return c
    raise HTTPException(status_code=404, detail="Course not found")


@app.post("/courses/{course_id}/lessons", response_model=Course)
def add_lesson(course_id: int, lesson: Lesson) -> Course:
    for c in courses:
        if c.id == course_id:
            lesson_id = len(c.lessons) + 1
            c.lessons.append(Lesson(id=lesson_id, title=lesson.title, content=lesson.content))
            return c
    raise HTTPException(status_code=404, detail="Course not found")
