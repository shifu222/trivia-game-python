from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


# test para crear una pregunta
def test_create_question():
    response = client.post("/questions/create", json={
        "description": "What is 2 + 2?",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "4",
        "level": "facil"
    })
    assert response.status_code == 201


# test para verificar el retorno de una pregunta
def test_get_question():
    response = client.get("/questions/1")
    data = response.json()
    assert response.status_code == 200
    assert data["pregunta"] == '¿Cuál es la capital de España?'


# test para verificar que los datos se insertaron correctamente
def test_insert_question_bd():

    with open("datos.json", "r", encoding="utf-8") as f:
        # se guarda la lista de preguntas originales
        data_original = json.load(f)

    response = client.get("/questions")

    assert response.status_code == 200
    data_api = response.json()  # se guarda la lista de preguntas de la bd

    # se agrega uno más porque se inserta un dato más en el test_trivia.py
    assert (len(data_original) +
            1) == len(data_api), "La cantidad de preguntas no coincide"

    # compara las preguntas uno por uno
    for original, desde_api in zip(data_original, data_api):
        assert original["pregunta"] == desde_api["pregunta"]
        assert original["alternativas"] == desde_api["alternativas"]
        assert original["respuesta_correcta"] == desde_api["respuesta_correcta"]
        assert original["nivel"] == desde_api["nivel"]
