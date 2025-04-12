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

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def run_quiz(self):

        question = self.get_next_question()  # obtiene la primera pregunta

        while question is not None:  # mientras halla preguntas restantes por preguntar
            print(
                # imprime la pregunta
                f"Pregunta {self.current_question_index}: {question.description}")

            # imprime todas las alternativas
            for idx, option in enumerate(question.options):
                print(f"{idx+1}) {option}")

            # guarda la alternativa del usuario (indice + 1)
            selection = int(input("Tu respuesta: "))

            # verifica si la respuesta es correcta
            isCorrect = "!Correcto!" if question.options[selection-1] == question.correct_answer else "!Incorrecto"

            print(isCorrect)  # muestra el resultado al usuario

            print("")  # salto de linea para una mejor vista

            # obtiene la siguiente pregunta , si es none es porque no hay más preguntas y se termina el bucle
            question = self.get_next_question()

        # reinicia el index para que el usuario pueda participar otra vez
        self.current_question_index = 0
