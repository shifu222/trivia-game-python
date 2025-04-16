from app.db import get_cursor


class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def run_quiz(self):

        print("************************************")
        print("*     🎉 BIENVENIDO A LA TRIVIA 🎉     *")
        print("************************************")
        print("📝 Instrucciones:")
        print("1. Elige el nivel de dificultad.")
        print("2. Responde las preguntas escribiendo la letra de la opción.")
        print("3. Cada respuesta correcta te da un punto.")
        print("************************************\n")
        print("Elige el nivel")
        print("1) Facil")
        print("2) Intermedio")
        print("3) Difícil")
        level = input("Ingrese la alternativa: ")  # recupera el nivel

        niveles = {
            "1": "facil",
            "2": "intermedio",
            "3": "dificil"
        }

        # si es que no es una opcion correcta se detiene el programa
        if not niveles.get(level):
            print("Opción incorrecta")
            return

        with get_cursor() as cursor:
            cursor.execute("""SELECT pregunta, alternativas, respuesta_correcta FROM preguntas WHERE nivel = %s""", (niveles.get(level),))  # busca las preguntas del nivel elegido en la base de datos
            rows = cursor.fetchall()  # retorna todas las preguntas

        for row in rows:  # para cada pregunta

            description = row[0]
            options = row[1]
            correct_answer = row[2]

            # crea una pregunta de los datos recuperados de la base de datos
            new_question = Question(description, options, correct_answer)

            self.add_question(new_question)  # agrega las preguntas


        question = self.get_next_question()  # recupera la pregunta

        while question is not None:  # mientras halla preguntas restantes por preguntar
            print(
                # imprime la pregunta
                f"Pregunta {self.current_question_index}: {question.description}")

            # imprime todas las alternativas
            for idx, option in enumerate(question.options):
                print(f"{idx+1}) {option}")

            try:
                # Obtiene la respuesta del usuario
                selection = int(input("Tu respuesta: "))
                if selection < 1 or selection > len(question.options):
                    raise ValueError("Selección fuera de rango.")
            except ValueError as e:
                print(f"Error: {e}")
                continue

            # verifica si la respuesta es correcta y si es, modifica la puntuación general con el método answer_question
            isCorrect = "!Correcto!" if self.answer_question(
                question, question.options[selection-1]) else "!Incorrecto"

            print(isCorrect)  # muestra el resultado al usuario

            print("")  # salto de linea para una mejor vista

            # obtiene la siguiente pregunta , si es none es porque no hay más preguntas y se termina el bucle
            question = self.get_next_question()

        # reinicia el index para que el usuario pueda participar otra vez
        self.current_question_index = 0

        # muestra la cantidad de respuestas correctas e incorrectas
        print(
            f"Selecctionaste {self.correct_answers} respuestas correctas y {self.incorrect_answers} incorrectas")

        # muestra la puntuación total
        print(f"Puntuación total: {self.correct_answers}")

    def answer_question(self, question, answer):
        if question.is_correct(answer):  # verifica que la respuesta sea correcta
            self.correct_answers += 1  # aumenta la cantida
            return True
        else:
            self.incorrect_answers += 1
            return False
