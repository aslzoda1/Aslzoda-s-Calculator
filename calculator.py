import customtkinter as ctk
import math

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AslzodaCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aslzoda's Calculator")
        self.geometry("400x600")
        self.resizable(False, False)

        self.result_var = ctk.StringVar(value="0")

        self.entry = ctk.CTkEntry(
            self, 
            textvariable=self.result_var,
            font=("Orbitron", 40), 
            height=100, 
            corner_radius=10,
            justify="right",
            fg_color="#1e1e1e",
            border_color="#333"
        )
        self.entry.pack(pady=20, padx=20, fill="x")

        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(pady=10, padx=20, fill="both", expand=True)

        buttons = [
            ('C', 'orange'), ('√', 'gray'), ('^', 'gray'), ('/', 'blue'),
            ('7', 'white'), ('8', 'white'), ('9', 'white'), ('*', 'blue'),
            ('4', 'white'), ('5', 'white'), ('6', 'white'), ('-', 'blue'),
            ('1', 'white'), ('2', 'white'), ('3', 'white'), ('+', 'blue'),
            ('0', 'white'), ('.', 'white'), ('%', 'gray'), ('=', 'green')
        ]

        row, col = 0, 0
        for (text, color_type) in buttons:
            btn_color = self.get_color(color_type)
            hover_color = self.get_hover_color(color_type)
            
            button = ctk.CTkButton(
                self.buttons_frame, 
                text=text, 
                width=80, 
                height=70, 
                font=("Arial", 22, "bold"),
                fg_color=btn_color,
                hover_color=hover_color,
                text_color="white" if color_type != 'white' else "black",
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            
            col += 1
            if col > 3:
                col = 0
                row += 1

    def get_color(self, color_type):
        colors = {
            'orange': "#ff9500",
            'gray': "#a5a5a5",
            'blue': "#34c759",
            'white': "#f0f0f0",
            'green': "#007bff"
        }
        return colors.get(color_type, "#333")

    def get_hover_color(self, color_type):
        hovers = {
            'orange': "#cc7a00",
            'gray': "#808080",
            'blue': "#28a745",
            'white': "#d9d9d9",
            'green': "#0056b3"
        }
        return hovers.get(color_type, "#444")

    def on_button_click(self, char):
        current_text = self.result_var.get()

        if char == "C":
            self.result_var.set("0")
        elif char == "=":
            try:
                expression = current_text.replace('^', '**')
                result = eval(expression)
                self.result_var.set(str(result))
            except:
                self.result_var.set("Xato!")
        elif char == "√":
            try:
                res = math.sqrt(float(current_text))
                self.result_var.set(str(res))
            except:
                self.result_var.set("Xato!")
        else:
            if current_text == "0" or current_text == "Xato!":
                self.result_var.set(char)
            else:
                self.result_var.set(current_text + char)

if __name__ == "__main__":
    app = AslzodaCalculator()
    app.mainloop()