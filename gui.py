from tkinter import *
from quiz import Quiz


class QuizGui():

    def __init__(self, quiz: Quiz) -> None:
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg="gray", padx=30, pady=30)

        self.tick_image = PhotoImage(file="images/tick.png")
        self.tick_button = Button(image=self.tick_image, highlightthickness=0, command=lambda: self.is_answer_corect("True"))
        self.tick_button.grid(column=0, row=2)

        self.cross_image = PhotoImage(file="images/cross.png")
        self.cross_button = Button(image=self.cross_image, highlightthickness=0, command=lambda: self.is_answer_corect("False"))
        self.cross_button.grid(column=1, row=2)

        #self.question_card_image = PhotoImage(file="images/question_background.png")
        self.question_canvas = Canvas(width=400, height=400, bg="white")
        #self.image_container = self.question_canvas.create_image(400, 400, image=self.question_card_image)
        text = self.quiz.get_question()
        self.question_text = self.question_canvas.create_text(200, 200, text=text, font=("Ariel", 20, "bold"), fill="black", width = 360)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=30)

        self.score_label = Label(text="Score: 0", fg="white", bg="gray", font=("Ariel", 20, "bold"))
        self.score_label.grid(column=1, row=0)

        self.window.mainloop()


    def display_question(self, text) -> None:
        self.question_canvas.itemconfig(self.question_text, text=text)


    def is_answer_corect(self, answer) -> None:
        if self.quiz.are_there_questions_left():

            if answer == self.quiz.get_answer():
                self.quiz.score += 1
                self.update_score()
                self.change_canvas_colour("green")
                self.window.after(1000, self.next_question)

            else:
                self.change_canvas_colour("red")
                self.window.after(1000, self.next_question)
        else:
            if answer == "True":
                self.reset_quiz()
            else:
                self.window.quit()


    def next_question(self) -> None:
        self.change_canvas_colour()
        if self.quiz.are_there_questions_left():
            self.quiz.next_question()

            if self.quiz.are_there_questions_left():
                question_text = self.quiz.get_question()
                self.display_question(question_text)
            else:
                text = f"Final score: {self.quiz.score}\nDo you want to play another round?"
                self.display_question(text)
    
    def update_score(self) -> None:
        self.score_label.config(text=f"Score: {self.quiz.score}")


    def reset_quiz(self) -> None:
        self.quiz.get_questions()
        self.quiz.score = 0
        self.update_score()
        question_text = self.quiz.get_question()
        self.display_question(question_text)


    def change_canvas_colour(self, colour="white") -> None:
        self.question_canvas.config(bg=colour)
