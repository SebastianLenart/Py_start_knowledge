from csv import reader
from random import choice


class Question:
    def __init__(self, question: str, answers: list, correct_answer: int):
        self.answers = answers
        self.question = question
        self.correct_answer = correct_answer

    def display(self):
        response = f"Pytanie: {self.question} \n"
        for no, answer in enumerate(self.answers, start=1):
            response += f"{no}. {answer} \n"
        return response

    def check_answer(self, answer_id: str):
        return self.correct_answer == answer_id


class Quiz:
    def __init__(self, filename):
        self.questions = []
        self.load_questions(filename)

    def load_questions(self, filename):
        with open(filename, encoding="utf-8") as file:
            iterator = reader(file, delimiter=";")
            for row in iterator:
                # print(row.pop(0))
                # # print(row.pop()) # ostatni
                # print(row.pop(-1)) # ostatni
                # print(row) # same opcje
                # print("*"*10)
                question = row.pop(0)
                correct_answer = row.pop(-1)
                answers = row

                print(question)
                print(correct_answer)
                print(answers)

                if len(answers) != 3:
                    raise ValueError("Nie mozna zaladowac pytan.") # to sie nie wyswietla
                self.questions.append(Question(question, answers, correct_answer))

    def run(self):
        in_progress = True
        result = 0
        while in_progress:
            try:
                question = choice(self.questions)
                print(question.display())
                self.questions.remove(question) # usuwam tylko z listy, ale obiekt jest przypisany wiec nie trace
                answer = input("Podaj poprawna odp: ")
                if question.check_answer(answer):
                    print("OK")
                    result += 1
                else:
                    print("NIE")
                    break
            except IndexError:
                print("Koniec listy, nie mozna randomowac po pustej liscie")
                break

        print(f"Koniec, wynik to: {result}")



if __name__ == "__main__":
    try:
        quiz = Quiz("quiz.csv")
        quiz.run()
    except FileNotFoundError:
        print("Plik nie istnieje")
    except ValueError:
        print("Cos nie tak z pytaniami") # to sie wyswietla
    except KeyboardInterrupt:
        print("keybord interak")




        