import requests
import html


class Quiz():


    def __init__(self) -> None:
        self.score = 0
        self.queston_number_options = [num for num in range(5, 51)]
        self.category_options = {"Any category": "", "General knowlegde": "9", "Film": "11", "Music": "12", "Science and nature": "17", "Computers": "18", "Mythology": "20", "Sports": "21", "Geography": "22", "Politics": "24"}
        self.difficulty_options = {"Any difficulty": "", "Easy": "easy", "Medium": "medium", "Hard": "hard"}
        self.url = "https://opentdb.com/api.php?amount={}{}{}&type=boolean"
        self.questions = []



    def __str__(self) -> str:
        if self.questions == []:
            return "Question list empty"
        else:
            output = ""
            for question in self.questions:
                output += f"{question["question"]}: {question["answer"]}\n"
            return output
        
    def console_start_menu(self) -> None:
        while True:
            user_input = input("Type 'start' to start quiz, 'settings' for settings or 'quit' to quit: ").lower()
            if user_input == "start":
                if self.questions == []:
                    self.get_questions()
                return self.start_quiz_console()
            elif user_input == "settings":
                self.get_questions(self.get_settings())
                if self.questions == []:
                    print("Oops, there was an error trying to get specified questions. Please try some different settings")
            elif user_input == "quit":
                break
            else:
                pass



            
    def get_settings(self) -> tuple:
        question_number = 0
        while question_number < 5 or question_number > 50:
            try:
                question_number = int(input("How many questions? (5-50)"))
            except ValueError:
                pass

        print("\nCategory options:")
        for option in self.category_options.keys():
            print(option)
        
        while True:
            category = input("Select category: ")
            try:
                category = self.category_options[category]
            except KeyError:
                pass
            else:
                break

        print("\nDifficulty options:")
        for option in self.difficulty_options.keys():
            print(option)

        while True:
            difficulty = input("\nSelect difficulty: ")
            try:
                difficulty = self.difficulty_options[difficulty]
            except KeyError:
                pass
            else:
                break

        return (question_number, category, difficulty)
        

    def get_questions(self, request_options=("10", "", "")) -> None:
        question_number = request_options[0]
        if request_options[1] == "":
            category = ""
        else:
            category = f"&category={request_options[1]}"

        if request_options[2] == "":
            difficulty = ""
        else:
            difficulty = f"&difficulty={request_options[2]}"

        request_url = self.url.format(question_number, category, difficulty)

        try:
            response = requests.get(url=request_url)
            response.raise_for_status()
        except requests.HTTPError:
            self.questions = []
        else:
            questions_json = response.json()["results"]
            for entry in questions_json:
                question = {"question": entry["question"], "answer": entry["correct_answer"]}
                self.questions.append(question)


    def get_question(self) -> str:
        if self.questions == []:
            return "Error: Cannot reteive questions :("
        else:
            return html.unescape(self.questions[0]["question"])
    

    def get_answer(self) -> str:
        if self.questions == []:
            return "Error: Cannot reteive questions :()"
        else:
            return self.questions[0]["answer"]
    

    def next_question(self) -> None:
        self.questions.pop(0)

    

    def are_there_questions_left(self) -> bool:
        return self.questions != []
        

    def start_quiz_console(self) -> None:
        question_number = 1
        while self.questions != []:
            if self.ask_question_console(question_number):
                self.score += 1
                print("Correct!\n")
            else:
                print("Incorrect\n")
            self.next_question()
            question_number += 1

        print(f"final score: {self.score}")
        self.score = 0
        return self.console_start_menu()


    def ask_question_console(self, question_number) -> bool:
        while True:
            guess = input(f"Q{question_number}: {self.get_question()} (T/F): ").strip().upper()
            if guess == "T":
                return self.get_answer() == "True"
            elif guess == "F":
                return self.get_answer() == "False"

