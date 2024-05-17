# quiz_gui.py

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("500x400")
        
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 14))
        style.configure('TButton', font=('Arial', 12))
        style.configure('TRadiobutton', font=('Arial', 12))
        
        self.frame = ttk.Frame(root, padding="10 10 10 10")
        self.frame.pack(expand=True, fill=tk.BOTH)
        
        self.question_label = ttk.Label(self.frame, text="", wraplength=400)
        self.question_label.pack(pady=20)
        
        self.var = tk.StringVar()
        
        self.radio_buttons = []
        for i in range(4):
            rb = ttk.Radiobutton(self.frame, text="", variable=self.var, value="")
            rb.pack(anchor="w", padx=20, pady=5)
            self.radio_buttons.append(rb)
        
        self.submit_button = ttk.Button(self.frame, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)
        
        self.next_button = ttk.Button(self.frame, text="Next", command=self.load_next_question, state="disabled")
        self.next_button.pack(pady=10)
        
        self.score_label = ttk.Label(self.frame, text="Score: 0")
        self.score_label.pack(pady=10)
        
        self.conn = sqlite3.connect('quiz.db')
        self.cursor = self.conn.cursor()
        
        self.questions = self.load_questions()
        self.current_question = 0
        self.score = 0
        
        self.load_next_question()
    
    def load_questions(self):
        self.cursor.execute("SELECT * FROM questions")
        return self.cursor.fetchall()
    
    def load_next_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.question_label.config(text=q[1])
            options = [q[2], q[3], q[4], q[5]]
            for i, rb in enumerate(self.radio_buttons):
                rb.config(text=options[i], value=options[i])
            self.var.set("")
            self.submit_button.config(state="normal")
            self.next_button.config(state="disabled")
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score is {self.score} out of {len(self.questions)}")
            self.root.quit()
    
    def check_answer(self):
        selected_answer = self.var.get()
        correct_answer = self.questions[self.current_question][6]
        if selected_answer == correct_answer:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Your answer is incorrect! The correct answer is {correct_answer}")
        self.current_question += 1
        self.submit_button.config(state="disabled")
        self.next_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
