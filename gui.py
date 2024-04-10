from tkinter import *
from quiz import Quiz


class QuizGui():

    def __init__(self, quiz: Quiz) -> None:
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg="gray", padx=30, pady=30)

        self.tick_image = PhotoImage(file="images/tick.png")
        self.tick_button = Button(image=self.tick_image, highlightthickness=0, command=self.tick_button_clicked)
        self.tick_button.grid(column=0, row=2)

        self.cross_image = PhotoImage(file="images/cross.png")
        self.cross_button = Button(image=self.cross_image, highlightthickness=0, command=self.cross_button_ticked)
        self.cross_button.grid(column=1, row=2)

        self.question_card_image = PhotoImage(file="images/question_background.png")
        self.question_canvas = Canvas(width=400, height=400)
        self.image_container = self.question_canvas.create_image(400, 400, image=self.question_card_image)
        self.question_text = self.question_canvas.create_text(200, 200, text="Question", font=("Ariel", 20, "bold"), fill="black")
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=30)

        self.score_label = Label(text="Score: 0", fg="white", bg="gray", font=("Ariel", 20, "bold"))
        self.score_label.grid(column=1, row=0)

        self.window.mainloop()


    def display_question(self, text):
        self.question_canvas.itemconfig(self.question_text, text=text)



    def tick_button_clicked(self):
        self.display_question("True")


    def cross_button_ticked(self):
        self.display_question("False")