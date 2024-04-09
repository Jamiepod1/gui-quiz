import requests


class Quiz():


    def __init__(self) -> None:
        self.score = 0
        self.url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean"
        self.questions = []
        self.get_questions()


    def __str__(self) -> str:
        if self.questions == []:
            return "Question list empty"
        else:
            output = ""
            for question in self.questions:
                output += f"{question["question"]}: {question["answer"]}\n"
            return output
            

    def get_questions(self) -> None:
        try:
            response = requests.get(url=self.url)
            response.raise_for_status()
        except HTTPError:
            self.questions = []
        else:
            questions_json = response.json()["results"]
            for entry in questions_json:
                question = {"question": entry["question"], "answer": entry["correct_answer"]}
                self.questions.append(question)


    def start_quiz_console(self) -> None:
        while self.questions != []:
            if self.ask_question():
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect")

        print(f"final score: {self.score}")
        self.score = 0
        self.get_questions()


    def ask_question(self) -> bool:
        question = self.questions.pop(0)
        while True:
            guess = input(f"{question["question"]}: T or F: ").strip().upper()
            if guess == "T":
                return question["answer"] == "True"
            elif guess == "F":
                return question["answer"] == "False"

            


quiz = Quiz()
quiz.start_quiz_console()
