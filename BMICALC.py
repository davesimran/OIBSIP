import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.create_widgets()
        self.load_data()

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            
            bmi = weight / (height ** 2)
            category = self.classify_bmi(bmi)

            result_text = f"BMI: {bmi:.2f} ({category})"
            self.result_label.config(text=result_text, foreground=self.get_category_color(category))
            
            self.save_data(weight, height, bmi)
            self.plot_bmi_trend()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

    @staticmethod
    def classify_bmi(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        else:
            return "Overweight"

    def get_category_color(self, category):
        if category == "Underweight":
            return "blue"
        elif category == "Normal":
            return "green"
        else:
            return "red"

    def create_widgets(self):
        # Create a style for consistent appearance
        style = ttk.Style()
        style.configure("TLabel", font=('Arial', 12))
        style.configure("TButton", font=('Arial', 12))
        style.configure("TEntry", font=('Arial', 12))

        # Weight entry
        self.weight_label = ttk.Label(self.root, text="Weight (kg):")
        self.weight_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.weight_entry = ttk.Entry(self.root)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10)

        # Height entry
        self.height_label = ttk.Label(self.root, text="Height (m):")
        self.height_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.height_entry = ttk.Entry(self.root)
        self.height_entry.grid(row=1, column=1, padx=10, pady=10)

        # Calculate BMI button
        self.calculate_button = ttk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=15)

        # Result label
        self.result_label = ttk.Label(self.root, text="", font=('Arial', 14, 'bold'))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        # BMI History button
        self.bmi_history_button = ttk.Button(self.root, text="View BMI History", command=self.show_bmi_history)
        self.bmi_history_button.grid(row=4, column=0, columnspan=2, pady=10)

    def save_data(self, weight, height, bmi):
        with open("bmi_data.csv", "a") as file:
            file.write(f"{weight},{height},{bmi}\n")

    def load_data(self):
        try:
            with open("bmi_data.csv", "r") as file:
                pass  
        except FileNotFoundError:
            pass  

    def show_bmi_history(self):
        pass

    def plot_bmi_trend(self):

        try:
            with open("bmi_data.csv", "r") as file:
                data = file.readlines()

            weights = [float(line.split(',')[0]) for line in data]
            heights = [float(line.split(',')[1]) for line in data]
            bmis = [float(line.split(',')[2]) for line in data]

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(bmis, marker='o', linestyle='-', color='b')
            ax.set_title('BMI Trend Over Time')
            ax.set_xlabel('Entries')
            ax.set_ylabel('BMI')
            ax.grid(True)

            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(row=5, column=0, columnspan=2, pady=10)
            canvas.draw()
        except FileNotFoundError:
            pass  

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()
