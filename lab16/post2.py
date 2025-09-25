import tkinter as tk
class TextInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Input App")
        self.instruction_label = tk.Label(root, text="Enter some text:", font=("Arial", 14))
        self.instruction_label.pack(pady=10)
        self.entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.entry.pack(pady=10)
        self.button = tk.Button(root, text="Display Text", command=self.display_text, font=("Arial", 14))
        self.button.pack(pady=10)
        self.display_label = tk.Label(root, text="", font=("Arial", 14), wraplength=300)
        self.display_label.pack(pady=20)

    def display_text(self):
        text = self.entry.get()
        self.display_label.config(text=f"Displayed Text: {text}")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TextInputApp(root)
    root.mainloop()
