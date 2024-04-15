from tkinter import *
from quiz import Quiz


class QuizGui():

    def __init__(self, quiz: Quiz) -> None:
        self.quiz = quiz
        self.options_menu_state = False
        self.window = Tk()
        self.window.title("Quiz")
        self.window.geometry("480x730")
        self.window.config(bg="gray", padx=30, pady=30)

        self.tick_image = PhotoImage(file="images/tick.png")
        self.tick_button = Button(image=self.tick_image, highlightthickness=0, command=lambda: self.is_answer_corect("True"))
        self.tick_button.grid(column=0, row=2)

        self.cross_image = PhotoImage(file="images/cross.png")
        self.cross_button = Button(image=self.cross_image, highlightthickness=0, command=lambda: self.is_answer_corect("False"))
        self.cross_button.grid(column=2, row=2)

        #self.question_card_image = PhotoImage(file="images/question_background.png")
        self.question_canvas = Canvas(width=400, height=400, bg="white")
        #self.image_container = self.question_canvas.create_image(400, 400, image=self.question_card_image)
        text = self.quiz.get_question()
        self.question_text = self.question_canvas.create_text(200, 200, text=text, font=("Ariel", 20, "bold"), fill="black", width = 360)
        self.question_canvas.grid(column=0, row=1, columnspan=3, sticky="nesw")

        self.score_label = Label(text="Score: 0", fg="white", bg="gray", font=("Ariel", 20, "bold"))
        self.score_label.grid(column=2, row=0)

        self.settings_button = Button(text="Settings", highlightthickness=0, font=("Ariel", 20, "normal"), command=self.display_settings)
        self.settings_button.grid(column=0, row=0)

        self.question_number = StringVar()
        self.category = StringVar()
        self.dificulty = StringVar()

        self.question_number.set(self.quiz.queston_number_options[5])
        self.category.set("Any category")
        self.dificulty.set(self.quiz.difficulty_options[0])

        self.question_number_dropdown = OptionMenu(self.window, self.question_number, *self.quiz.queston_number_options)

        self.category_dropdown = OptionMenu(self.window, self.category, *[item for item in self.quiz.category_options.keys()])

        self.dificulty_dropdown = OptionMenu(self.window, self.dificulty, *self.quiz.difficulty_options)
        self.question_number_dropdown.grid(column=0, row=1, pady=20)
        self.category_dropdown.grid(column=0, row=2)
        self.dificulty_dropdown.grid(column=0, row=3, pady=20)
        self.question_number_dropdown.grid_remove()
        self.category_dropdown.grid_remove()
        self.dificulty_dropdown.grid_remove()
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


    def display_settings(self) -> None:
        if self.options_menu_state:
            self.cross_button.grid()
            self.tick_button.grid()
            self.score_label.grid()
            self.question_canvas.grid()
            self.settings_button.grid_configure(padx=0)
            self.question_number_dropdown.grid_remove()
            self.category_dropdown.grid_remove()
            self.dificulty_dropdown.grid_remove()
            self.options_menu_state = False
        else:
            self.cross_button.grid_remove()
            self.tick_button.grid_remove()
            self.score_label.grid_remove()
            self.question_canvas.grid_remove()
            self.settings_button.grid_configure(padx=40)
            self.question_number_dropdown.grid()
            self.category_dropdown.grid()
            self.dificulty_dropdown.grid()
            self.options_menu_state = True

        self.window.update_idletasks()