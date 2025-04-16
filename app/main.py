from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from app.db import get_cursor
import psycopg2

app = FastAPI()


class QuestionCreate(BaseModel):  # clase para validar los campos para crear la pregunta
    description: str
    options: list[str]
    correct_answer: str
    level: str


# endpoint questions que devuelve el status de 201 si todo sale bien
@app.post("/questions/", status_code=status.HTTP_201_CREATED)
def create_question(question: QuestionCreate):
    try:
        with get_cursor() as cursor:  # inserta la pregunta en la base de datos
            cursor.execute("INSERT INTO preguntas(pregunta,alternativas,respuesta_correcta,nivel) VALUES (%s,%s,%s,%s) RETURNING id",
                           (question.description, question.options, question.correct_answer, question.level))
            new_id = cursor.fetchall()[0]  # busco el id
        # devuelve como respuesta el mensaje y el id de la pregunta insertada en la bd
        return {"message": "Question created ", "question_id": new_id}
    except psycopg2.Error as error:
        raise HTTPException( #retornar una excepción de tipo http cuando hay un problema con la base de datos
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error : {error}"
        )
