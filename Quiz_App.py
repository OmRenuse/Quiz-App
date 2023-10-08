import tkinter as tk

class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, answer):
        return answer == self.correct_option

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack()

        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(root, text="", variable=self.radio_var, value=i)
            self.radio_buttons.append(radio_button)
            radio_button.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack()

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question.question)
            for i in range(4):
                self.radio_buttons[i].config(text=question.options[i])
            self.radio_var.set(-1)
        else:
            self.show_score()

    def check_answer(self):
        user_answer = self.radio_var.get()
        if user_answer != -1:
            question = self.questions[self.current_question_index]
            if question.is_correct(user_answer):
                self.score += 1
            self.current_question_index += 1
            self.load_question()

    def show_score(self):
        self.question_label.config(text="Quiz Completed!")
        for radio_button in self.radio_buttons:
            radio_button.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.result_label.config(text=f"Your Score: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    questions = [
        Question("What is the capital of France?",
                 ["London", "Berlin", "Paris", "Madrid"],
                 2),

        Question("Which planet is known as the Red Planet?",
                 ["Earth", "Mars", "Venus", "Jupiter"],
                 1),

        Question("What is the largest mammal in the world?",
                 ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                 1)
    ]

    root = tk.Tk()
    app = QuizApp(root, questions)
    root.mainloop()
