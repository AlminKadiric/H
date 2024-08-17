import tkinter as tk

class TripleClickDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("Triple Click Detector")
        
        self.label = tk.Label(root, text="Click here", font=("Arial", 24))
        self.label.pack(padx=20, pady=20)
        

        self.click_count = 0
        self.total_clicks = 0
        

        self.label.bind("<Button-1>", self.on_click)

    def on_click(self, event):

        self.click_count += 1
        self.total_clicks += 1


        if self.click_count == 3:
            print(f"Triple click detected! Total clicks: {self.total_clicks}")
   
            self.click_count = 0


        self.root.after(500, self.reset_click_count)

    def reset_click_count(self):
        self.click_count = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = TripleClickDetector(root)
    root.mainloop()
