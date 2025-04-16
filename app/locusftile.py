from locust import HttpUser, task


class TriviaUser(HttpUser):
    @task
    def play_trivia(self):
        payload = {
            "description": "nueva pregunta",
            "options": ["alternativa1", "alternativa2", "alternativa3"],
            "correct_answer": ["alternativa2"],
            "level": "facil"
        }
        self.client.post("/questions/create", json=payload)
