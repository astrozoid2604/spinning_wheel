import tkinter as tk
from tkinter import Toplevel, Canvas, Frame, Scrollbar
from PIL import Image, ImageDraw, ImageTk
import math
import random
import time
import threading

qna_dict = {
    "Q1": ["B) To turn raw data into useful insights for decision-making",
           f"Q1. What is the main purpose of data analytics in a company like Amgen?\n"
           f"    A) To replace human jobs with machines\n"
           f"    B) To turn raw data into useful insights for decision-making\n"
           f"    C) To track employee attendance\n"
           f"    D) To store data without using paper"],
    "Q2": ["B) Predicting equipment maintenance needs",
           f"Q2. Which of the following is a common use case of data analytics in the healthcare or pharmaceutical industry?\n"
           f"    A) Designing logos for new products\n"
           f"    B) Predicting equipment maintenance needs\n"
           f"    C) Making coffee orders for employees\n"
           f"    D) Scanning ID cards at the entrance"],
    "Q3": ["B) To visualize key metrics in an easy-to-read format",
           f"Q3. What is a dashboard most commonly used for in data analytics?\n"
           f"    A) To show daily weather updates\n"
           f"    B) To visualize key metrics in an easy-to-read format\n"
           f"    C) To play videos and multimedia content\n"
           f"    D) To track personal health goals only"],
    "Q4": ["C) Supporting evidence-based decisions using data",
           f"Q4. Which of the following is a benefit of using data analytics at Amgen?\n"
           f"    A) Making decisions based on gut feelings\n"
           f"    B) Reducing the need for team collaboration\n"
           f"    C) Supporting evidence-based decisions using data\n"
           f"    D) Replacing meetings entirely"],
    "Q5": ["B) A software or system that mimics human thinking and learning",
           f"Q5. What does Artificial Intelligence (AI) generally refer to?\n"
           f"    A) A robot that does household chores\n"
           f"    B) A software or system that mimics human thinking and learning\n"
           f"    C) A new brand of medicine\n"
           f"    D) A type of video game technology"],
    "Q6": ["C) Voice assistants like Siri or Alexa",
           f"Q6. Which of the following is an example of AI that you may already use in everyday life?\n"
           f"    A) A microwave oven\n"
           f"    B) A vacuum cleaner without sensors\n"
           f"    C) Voice assistants like Siri or Alexa\n"
           f"    D) A light switch"],
    "Q7": ["C) It helps speed up drug discovery and patient data analysis.",
           f"Q7. Why is AI becoming increasingly important in the pharmaceutical industry?\n"
           f"    A) It can automate laboratory cleaning\n"
           f"    B) It can design office layouts\n"
           f"    C) It helps speed up drug discovery and patient data analysis.\n"
           f"    D) It can replace all pharmacists."],
    "Q8": ["B) It can learn from data and improve over time",
           f"Q8. What makes AI different from traditional software?\n"
           f"    A) It doesn't need electricity\n"
           f"    B) It can learn from data and improve over time\n"
           f"    C) It always requires a robot body\n"
           f"    D) It’s used only in video games"],
    "Q9": ["B) To observe processes directly at the place where value is created",
           f"Q9. What is the main purpose of a Gemba walk?\n"
           f"    A) To get your daily steps in\n"
           f"    B) To observe processes directly at the place where value is created\n"
           f"    C) To find the best coffee machine in the office\n"
           f"    D) To practice walking on the manufacturing floor"],
    "Q10": ["B) Lean Six Sigma principles and best practices",
            f"Q10. What does the AI4CI assistant help team members learn about?\n"
            f"     A) Personal time management techniques\n"
            f"     B) Lean Six Sigma principles and best practices\n"
            f"     C) Finance and accounting processes\n"
            f"     D) Corporate compliance policies"],
    "Q11": ["C) A Non-GxP Proof of Concept",
            f"Q12. AI4CI is currently classified as:\n"
            f"     A) A full production system\n"
            f"     B) A GxP-validated tool\n"
            f"     C) A Non-GxP Proof of Concept\n"
            f"     D) A tool for audits"],
    "Q12": ["B) Root cause analysis",
            f"Q12. The 5 Whys technique is primarily used for:\n"
            f"     A) Project planning\n"
            f"     B) Root cause analysis\n"
            f"     C) Time tracking\n"
            f"     D) Employee engagement surveys"],
    "Q13": ["A) Phishing emails",
            f"Q13. Which of the following is an example of a social engineering attack?\n"
            f"     A) Phishing emails\n"
            f"     B) Brute force password attacks\n"
            f"     C) SQL injection\n"
            f"     D) Denial of Service (DoS) attacks"],
    "Q14": ["A) Stop and be vigilant, it may be a malicious app you are downloading. Excuse yourself from the sales person immediately.",
            f"Q14. A sales person approaches you and asks you to download an online app via a QR code where you can get a huge discount when purchasing their product online. But when you scan, it brings you to a third party website, where you need to download and install the app. What do you do?\n"
            f"     A) Stop and be vigilant, it may be a malicious app you are downloading. Excuse yourself from the sales person immediately.\n"
            f"     B) Download the app since there is a huge discount you can get purchasing off the online platform\n"
            f"     C) Download the app since the sales person is seeing your action and you do not want to embarrass yourself\n"
            f"     D) Download the software since the sales person is pestering you and it is difficult to avoid the sales person."],
    "Q15": ["B) False",
            f"Q15. It is advisable to connect to a public or free WIFI?\n"
            f"     A) True\n"
            f"     B) False"],
    "Q16": ["A) Scamshield",
            f"Q16. ASM strongly emphasizes downloading an App to report Smishing and Vishing (only available in Singapore)?\n"
            f"     A) Scamshield\n"
            f"     B) No App\n"
            f"     C) Symantec\n"
            f"     D) There is no such app"]
}

class SpinningWheelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spinning Wheel")

        # Center the main window on screen (doubled size)
        window_width = 840
        window_height = 1000
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.canvas_size = 800
        self.center = self.canvas_size // 2
        self.num_sectors = 16
        self.sector_angle = 360 / self.num_sectors
        self.labels = [f"Q{i+1}" for i in range(self.num_sectors)]
        self.current_angle = 0
        self.is_spinning = False
        self.spin_history = []
        self.popup_open = False
        self.active_popups = set()  # Track open popup windows

        # Canvas
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size + 100, bg='white')
        self.canvas.pack()

        # Down arrow
        self.arrow = self.canvas.create_polygon(
            self.center - 20, 20,
            self.center + 20, 20,
            self.center, 80,
            fill='red',
            tags='arrow'
        )

        # Spin button
        self.spin_button = tk.Button(root, text="Spin Me!", font=('Arial', 28), command=self.start_spin)
        self.spin_button.pack(pady=20)

        # Initial wheel
        self.wheel_img = None
        self.draw_wheel(0)

    def draw_wheel(self, angle_offset):
        image = Image.new("RGBA", (self.canvas_size, self.canvas_size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        radius = self.center - 20

        for i in range(self.num_sectors):
            start_angle = i * self.sector_angle + angle_offset
            end_angle = start_angle + self.sector_angle
            color = "#%06x" % random.randint(0x444444, 0xAAAAAA)
            draw.pieslice([20, 20, self.canvas_size - 20, self.canvas_size - 20],
                          start=start_angle, end=end_angle, fill=color, outline="black")

            # Label
            mid_angle = math.radians((start_angle + end_angle) / 2)
            text_x = self.center + (radius - 80) * math.cos(mid_angle)
            text_y = self.center + (radius - 80) * math.sin(mid_angle)
            draw.text((text_x - 20, text_y - 10), self.labels[i], fill="black", font_size=24)

        self.wheel_img = ImageTk.PhotoImage(image)
        self.canvas.delete("wheel")
        self.canvas.create_image(self.center, self.center, image=self.wheel_img, tags="wheel")
        self.canvas.tag_raise('arrow')

    def start_spin(self):
        if self.is_spinning or self.popup_open:
            return
        self.is_spinning = True
        threading.Thread(target=self.spin_wheel).start()

    def spin_wheel(self):
        total_duration = 2
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

        # Ensure the result is not in the last 5 spins
        adjusted_angle = (self.current_angle + 90) % 360
        final_index = int((360 - adjusted_angle) % 360 // self.sector_angle)
        attempts = 0
        max_attempts = 10
        while self.labels[final_index] in self.spin_history and attempts < max_attempts:
            final_angle += self.sector_angle
            self.current_angle = final_angle % 360
            adjusted_angle = (self.current_angle + 90) % 360
            final_index = int((360 - adjusted_angle) % 360 // self.sector_angle)
            self.draw_wheel(self.current_angle)
            attempts += 1

        selected_label = self.labels[final_index]
        self.spin_history.append(selected_label)
        if len(self.spin_history) > 5:
            self.spin_history.pop(0)
        self.show_result(selected_label)
        self.is_spinning = False

    def show_result(self, label):
        self.popup_open = True
        popup = Toplevel(self.root)
        popup.title("Your Question")
        self.active_popups.add(popup)  # Track this popup

        # Create a canvas with scrollbar
        canvas = Canvas(popup)
        scrollbar = Scrollbar(popup, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Calculate dynamic size based on text content
        text = f"Please answer {label}!\n{qna_dict[label][1]}"
        font_size = 14
        char_width = 8
        line_height = 20
        lines = text.split('\n')
        max_chars = max(len(line) for line in lines)
        num_lines = len(lines)
        popup_width = min(max_chars * char_width + 40, 600)
        popup_height = min(num_lines * line_height + 100, 400)

        # Center the popup
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        x = (screen_width // 2) - (popup_width // 2)
        y = (screen_height // 2) - (popup_height // 2)
        popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
        popup.resizable(True, True)

        # Add content to scrollable frame
        msg = tk.Label(scrollable_frame, text=text, font=("Arial", font_size), wraplength=popup_width - 40, justify="left")
        msg.pack(pady=10)

        reveal_btn = tk.Button(scrollable_frame, text="Reveal Answer!", font=("Arial", 12),
                               command=lambda: self.show_answer(label))
        reveal_btn.pack(pady=5)

        def close_popup():
            self.active_popups.discard(popup)
            popup.destroy()
            self.check_popups_closed()

        close_btn = tk.Button(scrollable_frame, text="✖", command=close_popup, font=("Arial", 12))
        close_btn.pack(anchor="ne")

        # Bind mouse wheel for scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(-1 * (event.delta // 120), "units")
        popup.bind("<MouseWheel>", _on_mousewheel)
        popup.bind("<Destroy>", lambda e: [self.active_popups.discard(popup), self.check_popups_closed()])

    def show_answer(self, label):
        answer_popup = Toplevel(self.root)
        answer_popup.title("Answer")
        self.active_popups.add(answer_popup)

        # Create a canvas with scrollbar
        canvas = Canvas(answer_popup)
        scrollbar = Scrollbar(answer_popup, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Calculate dynamic size based on text content
        text = qna_dict[label][0]
        font_size = 12
        char_width = 8
        line_height = 20
        lines = text.split('\n')
        max_chars = max(len(line) for line in lines)
        num_lines = len(lines)
        popup_width = min(max_chars * char_width + 40, 600)
        popup_height = min(num_lines * line_height + 100, 400)

        # Center the popup
        screen_width = answer_popup.winfo_screenwidth()
        screen_height = answer_popup.winfo_screenheight()
        x = (screen_width // 2) - (popup_width // 2)
        y = (screen_height // 2) - (popup_height // 2)
        answer_popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
        answer_popup.resizable(True, True)

        # Add content to scrollable frame
        msg = tk.Label(scrollable_frame, text=text, font=("Arial", font_size), wraplength=popup_width - 40, justify="left")
        msg.pack(pady=20)

        def close_popup():
            self.active_popups.discard(answer_popup)
            answer_popup.destroy()
            self.check_popups_closed()

        close_btn = tk.Button(scrollable_frame, text="✖", command=close_popup, font=("Arial", 12))
        close_btn.pack(anchor="ne")

        # Bind mouse wheel for scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(-1 * (event.delta // 120), "units")
        answer_popup.bind("<MouseWheel>", _on_mousewheel)
        answer_popup.bind("<Destroy>", lambda e: [self.active_popups.discard(answer_popup), self.check_popups_closed()])

    def check_popups_closed(self):
        self.popup_open = len(self.active_popups) > 0

# Launch app
if __name__ == "__main__":
    root = tk.Tk()
    app = SpinningWheelApp(root)
    root.mainloop()
