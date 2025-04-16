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
@app.post("/questions/create", status_code=status.HTTP_201_CREATED)
def create_question(question: QuestionCreate):
    try:
        with get_cursor() as cursor:  # inserta la pregunta en la base de datos
            cursor.execute(
                """
            INSERT INTO preguntas (pregunta, alternativas, respuesta_correcta, nivel)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """,
                (
                    question.description,
                    question.options,
                    question.correct_answer,
                    question.level
                )
            )
            new_id = cursor.fetchall()[0]  # busco el id
        # devuelve como respuesta el mensaje y el id de la pregunta
        return {"message": "Question created ", "question_id": new_id}
    except psycopg2.Error as error:
        # retornar una excepción de tipo http
        # cuando hay un problema con la base de datos
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"database error : {error}"
        )


@app.get("/questions/{id}")
def get_question(id: str):
    try:
        with get_cursor() as cursor:
            cursor.execute(
                "SELECT * FROM preguntas WHERE id=%s",
                (id,))
            pregunta = cursor.fetchall()[0]

        return {"pregunta": pregunta[1]}

    except psycopg2.Error as error:
        raise HTTPException(
            status_code=400,
            detail=f"database error : {error}"
        )


@app.get("/questions")
def get_questions():
    try:
        with get_cursor() as cursor:
            cursor.execute(
                "SELECT * FROM preguntas")
            preguntas = cursor.fetchall()
            preguntas_json = []

            for pregunta in preguntas:
                preguntas_json.append({
                    "id": pregunta[0],
                    "pregunta": pregunta[1],
                    "alternativas": pregunta[2],
                    "respuesta_correcta": pregunta[3],
                    "nivel": pregunta[4]
                })
        return preguntas_json

    except psycopg2.Error as error:
        raise HTTPException(
            status_code=400,
            detail=f"database error : {error}"
        )
