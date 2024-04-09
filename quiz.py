import requests

class Quiz():
    def __init__(self) -> None:
        self.score = 0
        self.url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean"
        self.questions = {}
        self.get_questions()


    def get_questions(self):
        try:
            response = requests.get(url=self.url)
            response.raise_for_status()
        except HTTPError:
            self.questions = {}
        else:
            questions_json = response.json()["results"]
            for entry in questions_json:
                self.questions[entry["question"]] = entry["correct_answer"]

        
    

quiz = Quiz()
print(quiz.questions)
