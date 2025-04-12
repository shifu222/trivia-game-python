from trivia import Question,Quiz

quiz = Quiz()
quiz.add_question(Question("What is 2 + 2?", ["1", "2", "3", "4"], "4"))
quiz.add_question(Question("What is 2 + 1?", ["1", "2", "3", "4"], "3"))
quiz.add_question(Question("What is 2 + 0?", ["1", "2", "3", "4"], "2"))
quiz.add_question(Question("What is 2 + 4?", ["1", "2", "3", "6"], "6"))

quiz.run_quiz()
quiz.run_quiz()