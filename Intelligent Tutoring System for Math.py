import customtkinter as ctk
from tkinter import messagebox

# Initialize the customtkinter theme
ctk.set_appearance_mode("light")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class MathTutorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # App settings
        self.title("Intelligent Math Tutor")
        self.geometry("900x600")
        self.resizable(False, False)

        # Sidebar navigation
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.pack(side="left", fill="y")

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Math Tutor", font=("Arial", 20, "bold"))
        self.logo_label.pack(pady=20)

        self.nav_buttons = []
        nav_items = ["Dashboard", "Practice", "Progress", "Settings"]
        for item in nav_items:
            button = ctk.CTkButton(self.sidebar_frame, text=item, corner_radius=5, command=lambda name=item: self.nav_command(name))
            button.pack(pady=10, padx=20, fill="x")
            self.nav_buttons.append(button)

        # Main content area
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(padx=20, pady=20, expand=True, fill="both")

        # Widgets in main area
        self.title_label = ctk.CTkLabel(self.main_frame, text="Welcome to Math Tutor!", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=30)

        self.problem_label = ctk.CTkLabel(self.main_frame, text="Solve the Problem Below:", font=("Arial", 18))
        self.problem_label.pack(pady=10)

        self.problem_text = ctk.CTkLabel(self.main_frame, text="5 + 3 = ?", font=("Arial", 30))
        self.problem_text.pack(pady=20)

        self.answer_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Enter your answer here", font=("Arial", 16))
        self.answer_entry.pack(pady=10)

        self.submit_button = ctk.CTkButton(self.main_frame, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.feedback_label = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 16))
        self.feedback_label.pack(pady=20)

        # Sample problem data
        self.current_answer = 8  # Correct answer for 5 + 3

    def nav_command(self, name):
        messagebox.showinfo("Navigation", f"Navigating to {name}!")

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.current_answer:
                self.feedback_label.configure(text="Correct! Well done!", text_color="green")
            else:
                self.feedback_label.configure(text="Incorrect. Try again!", text_color="red")
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid number!")

if __name__ == "__main__":
    app = MathTutorApp()
    app.mainloop()
