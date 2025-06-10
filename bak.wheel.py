import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageDraw, ImageTk
import math
import random
import time
import threading

class SpinningWheelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spinning Wheel")

        # Center the main window on screen
        window_width = 420
        window_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.canvas_size = 400
        self.center = self.canvas_size // 2
        self.num_sectors = 16
        self.sector_angle = 360 / self.num_sectors
        self.labels = [f"Q{i+1}" for i in range(self.num_sectors)]
        self.current_angle = 0
        self.is_spinning = False

        # Canvas
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size + 50, bg='white')
        self.canvas.pack()

        # Down arrow
        self.arrow = self.canvas.create_polygon(
            self.center - 10, 10,
            self.center + 10, 10,
            self.center, 40,
            fill='red',
            tags='arrow'
        )

        # Spin button
        self.spin_button = tk.Button(root, text="Spin Me!", font=('Arial', 14), command=self.start_spin)
        self.spin_button.pack(pady=10)

        # Initial wheel
        self.wheel_img = None
        self.draw_wheel(0)

    def draw_wheel(self, angle_offset):
        image = Image.new("RGBA", (self.canvas_size, self.canvas_size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        radius = self.center - 10

        for i in range(self.num_sectors):
            start_angle = i * self.sector_angle + angle_offset
            end_angle = start_angle + self.sector_angle
            color = "#%06x" % random.randint(0x444444, 0xAAAAAA)
            draw.pieslice([10, 10, self.canvas_size - 10, self.canvas_size - 10],
                          start=start_angle, end=end_angle, fill=color, outline="black")

            # Label
            mid_angle = math.radians((start_angle + end_angle) / 2)
            text_x = self.center + (radius - 40) * math.cos(mid_angle)
            text_y = self.center + (radius - 40) * math.sin(mid_angle)
            draw.text((text_x - 10, text_y - 5), self.labels[i], fill="black")

        self.wheel_img = ImageTk.PhotoImage(image)
        self.canvas.delete("wheel")
        self.canvas.create_image(self.center, self.center, image=self.wheel_img, tags="wheel")
        self.canvas.tag_raise('arrow')

    def start_spin(self):
        if self.is_spinning:
            return
        self.is_spinning = True
        threading.Thread(target=self.spin_wheel).start()

    def spin_wheel(self):
        total_duration = 4
        steps = 100
        sleep_interval = total_duration / steps
        final_angle = random.uniform(3 * 360, 6 * 360)
        angle = 0

        for i in range(steps):
            ease_out = 1 - (i / steps)
            delta = (final_angle / steps) * ease_out
            angle += delta
            self.current_angle = angle % 360
            self.draw_wheel(self.current_angle)
            time.sleep(sleep_interval)

        # Corrected angle to match arrow at 12 o'clock
        adjusted_angle = (self.current_angle + 90) % 360
        final_index = int((360 - adjusted_angle) % 360 // self.sector_angle)
        selected_label = self.labels[final_index]
        self.show_result(selected_label)
        self.is_spinning = False

    def show_result(self, label):
        popup = Toplevel(self.root)
        popup.title("Your Question")

        popup_width = 250
        popup_height = 100
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        x = (screen_width // 2) - (popup_width // 2)
        y = (screen_height // 2) - (popup_height // 2)
        popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
        popup.resizable(False, False)

        msg = tk.Label(popup, text=f"Please answer {label}!", font=("Arial", 14))
        msg.pack(pady=20)

        close_btn = tk.Button(popup, text="✖", command=popup.destroy, font=("Arial", 12))
        close_btn.place(relx=1.0, rely=0.0, anchor="ne")

# Launch app
if __name__ == "__main__":
    root = tk.Tk()
    app = SpinningWheelApp(root)
    root.mainloop()
