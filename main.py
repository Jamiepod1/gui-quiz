from quiz import Quiz
from gui import QuizGui
import sys

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-c":
            quiz = Quiz()
            quiz.start_quiz_console()
        elif sys.argv[1] == "-g":
            quiz = Quiz()
            quiz_gui = QuizGui(quiz)
        else:
            print("Incorrect argument:\n'c' for console\n'g' for GUI")
    else:
        print("Required exactly 2 arguments")


main()