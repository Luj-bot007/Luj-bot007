import tkinter as tk

class TrafficLight:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Simulation")

        self.canvas = tk.Canvas(root, width=200, height=400, bg='white')
        self.canvas.pack()

        self.red_light = self.canvas.create_oval(50, 50, 150, 150, fill='black')
        self.yellow_light = self.canvas.create_oval(50, 150, 150, 250, fill='black')
        self.green_light = self.canvas.create_oval(50, 250, 150, 350, fill='black')

        self.current_light = 'red'
        self.change_light()

    def change_light(self):
        if self.current_light == 'red':
            self.canvas.itemconfig(self.red_light, fill='red')
            self.canvas.itemconfig(self.yellow_light, fill='grey')
            self.canvas.itemconfig(self.green_light, fill='grey')
            self.current_light = 'green'
            self.root.after(3000, self.change_light)
        elif self.current_light == 'green':
            self.canvas.itemconfig(self.red_light, fill='grey')
            self.canvas.itemconfig(self.yellow_light, fill='grey')
            self.canvas.itemconfig(self.green_light, fill='green')
            self.current_light = 'yellow'
            self.root.after(3000, self.change_light)
        elif self.current_light == 'yellow':
            self.canvas.itemconfig(self.red_light, fill='grey')
            self.canvas.itemconfig(self.yellow_light, fill='yellow')
            self.canvas.itemconfig(self.green_light, fill='grey')
            self.current_light = 'red'
            self.root.after(1000, self.change_light)

if __name__ == "__main__":
    root = tk.Tk()
    traffic_light = TrafficLight(root)
    root.mainloop()
