import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")
        self.counter = 0

        # Label to display the counter
        self.label = tk.Label(root, text=f"Counter: {self.counter}", font=("Arial", 24))
        self.label.pack(pady=20)

        # Button to increment the counter
        self.button = tk.Button(root, text="Increment", command=self.increment_counter, font=("Arial", 16))
        self.button.pack(pady=10)

    def increment_counter(self):
        self.counter += 1
        self.label.config(text=f"Counter: {self.counter}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
