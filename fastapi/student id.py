from fastapi import FastAPI,Path
app = FastAPI()
students= {
    1:{
        "name": "anand",
        "age": 18,
        "class": "1st year"
    }
}

@app.get("/")
def index():
    return{"name":"hello"}

@app.get("/get-student/{student_id}")
def get_student(student_id:int=Path
            (None,description="The ID of the Student you want to view",gt=0,lt=3)):
    return students[student_id]
