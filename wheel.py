import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageDraw, ImageTk
import math
import random
import time
import threading


qna_dict = {"Q1": ["B) To turn raw data into useful insights for decision-making",
                   f"\
                    Q1. What is the main purpose of data analytics in a company like Amgen?\
                        A) To replace human jobs with machines\
                        B) To turn raw data into useful insights for decision-making\
                        C) To track employee attendanceD\
                        D) To store data withotu using paper\
                   "
                  ], 
            "Q2": ["B) Predicting equipment maintenance needs",
                   f"\
                    Q2. Which of the following is a common use case of data analytics in the healthcare or pharmaceutical industry?\
                        A) Designing logos for new products\
                        B) Predicting equipment maintenance needs\
                        C) Making coffee orders for employees\
                        D) Scanning ID cards at the entrance\
                   "
                  ],
            "Q3": ["B) To visualize key metrics in an easy-to-read format", 
                   f"\
                    Q3. What is a dashboard most commonly used for in data analytics?\
                        A) To show daily weather updates\
                        B) To visualize key metrics in an easy-to-read format\
                        C) To play videos and multimedia content\
                        D) To track personal health goals only\
                   "
                  ],
            "Q4": ["C) Supporting evidence-based decisions using data", 
                   f"\
                    Q4. Which of the following is a benefit of using data analytics at Amgen?\
                        A) Making decisions based on gut feelings\
                        B) Reducing the need for team collaboration\
                        C) Supporting evidence-based decisions using data\
                        D) Replacing meetings entirely\
                   "
                  ],
            "Q5": ["B) A software or system that mimics human thinking and learning", 
                   f"\
                    Q5. What does Artificial Intelligence (AI) generally refer to?\
                        A) A robot that does household chores\
                        B) A software or system that mimics human thinking and learning\
                        C) A new brand of medicine\
                        D) A type of video game technology\
                   "
                  ],
            "Q6": ["C) Voice assistants like Siri or Alexa", 
                   f"\
                    Q6. Which of the following is an example of AI that you may already use in everyday life?\
                        A) A microwave oven\
                        B) A vacuum cleaner without sensors\
                        C) Voice assistants like Siri or Alexa\
                        D) A light switch\
                   "
                  ],
            "Q7": ["C) It helps speed up drug discovery and patient data analysis.", 
                   f"\
                    Q7. Why is AI becoming increasingly important in the pharmaceutical industry?\
                        A) It can automate laboratory cleaning\
                        B) It can design office layouts\
                        C) It helps speed up drug discovery and patient data analysis.\
                        D) It can replace all pharmacists.\
                   "
                  ],
            "Q8": ["B) It can learn from data and improve over time", 
                   f"\
                    Q8. What makes AI different from traditional software?\
                        A) It doesn't need electricity\
                        B) It can learn from data and improve over time\
                        C) It always requires a robot body\
                        D) It’s used only in video games\
                   "
                  ],
            "Q9": ["B) To observe processes directly at the place where value is created", 
                   f"\
                    Q9. What is the main purpose of a Gemba walk?\
                        A) To get your daily steps in\
                        B) To observe processes directly at the place where value is created\
                        C) To find the best coffee machine in the office\
                        D) To practice walking on the manufacturing floor\
                   "
                  ],
            "Q10":["B) Lean Six Sigma principles and best practices", 
                   f"\
                    Q10. What does the AI4CI assistant help team members learn about?\
                         A) Personal time management techniques\
                         B) Lean Six Sigma principles and best practices\
                         C) Finance and accounting processes\
                         D) Corporate compliance policies\
                   "
                  ],
            "Q11":["C) A Non-GxP Proof of Concept", 
                   f"\
                    Q12. AI4CI is currently classified as:\
                         A) A full production system\
                         B) A GxP-validated tool\
                         C) A Non-GxP Proof of Concept\
                         D) A tool for audits\
                   "
                  ],
            "Q12":["B) Root cause analysis", 
                   f"\
                    Q12. The 5 Whys technique is primarily used for:\
                         A) Project planning\
                         B) Root cause analysis\
                         C) Time tracking\
                         D) Employee engagement surveys\
                   "
                  ],
            "Q13":["A) Phishing emails", 
                   f"\
                    Q13. Which of the following is an example of a social engineering attack?\
                         A) Phishing emails\
                         B) Brute force password attacks\
                         C) SQL injection\
                         D) Denial of Service (DoS) attacks\
                   "
                  ],
            "Q14":["A) Stop and be vigilant, it may be a malicious app you are downloading. Excuse yourself from the sales person immediately.", 
                   f"\
                    Q14.A sales person approach you and ask you to download an online app via a QR code where you can get a huge discount when purchasing their product online. But when you scan, it brings you to a third party website, where you need to download and install the app. What do you do?\
                       A) Stop and be vigilant, it may be a malicious app you are downloading. Excuse yourself from the sales person immediately.\
                       B) Download the app since there is a huge discount you can get purchasing off the online platform\
                       C) Download the app since the sale person is seeing your action and you do not want to embarrass yourself\
                       D) Download the software since the sales person is pestering you and it is difficult to avoid the sales person.\
                   "
                  ],
            "Q15":["B) False", 
                   f"\
                    Q15. It is advisable to connect to a  public or free WIFI?\
                        A) True\
                        B) False\
                   "
                  ],
            "Q16":["A) Scamshield", 
                   f"\
                    Q16.ASM strongly emphases to download an App to report Smishing and Vishing (only available in Singapore)?\
                        A) Scamshield\
                        B) No App\
                        C) Symantec\
                        D) There is no such app\
                   "
                  ],
}



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
        self.spin_history = []  # Track last 5 spin results
        self.popup_open = False  # Track if popups are open

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
        if self.is_spinning or self.popup_open:
            return
        self.is_spinning = True
        threading.Thread(target=self.spin_wheel).start()

    def spin_wheel(self):
        total_duration = 2  # Updated from 4 to 2 seconds
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
            self.spin_history.pop(0)  # Keep only the last 5 spins
        self.show_result(selected_label)
        self.is_spinning = False

    def show_result(self, label):
        self.popup_open = True
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

        msg = tk.Label(popup, text=f"Please answer {label}!\n {qna_dict[label][1]}", font=("Arial", 14))
        msg.pack(pady=10)

        # Reveal Answer button
        reveal_btn = tk.Button(popup, text="Reveal Answer!", font=("Arial", 12), 
                              command=lambda: self.show_answer(label))
        reveal_btn.pack(pady=5)

        close_btn = tk.Button(popup, text="✖", command=lambda: [popup.destroy(), self.check_popups_closed()], 
                             font=("Arial", 12))
        close_btn.place(relx=1.0, rely=0.0, anchor="ne")

    def show_answer(self, label):
        answer_popup = Toplevel(self.root)
        answer_popup.title("Answer")

        popup_width = 250
        popup_height = 100
        screen_width = answer_popup.winfo_screenwidth()
        screen_height = answer_popup.winfo_screenheight()
        x = (screen_width // 2) - (popup_width // 2)
        y = (screen_height // 2) - (popup_height // 2)
        answer_popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
        answer_popup.resizable(False, False)

        # Placeholder for answer text
        answer_text = f"{qna_dict[label][0]}"
        msg = tk.Label(answer_popup, text=answer_text, font=("Arial", 12))
        msg.pack(pady=20)

        close_btn = tk.Button(answer_popup, text="✖", command=lambda: [answer_popup.destroy(), self.check_popups_closed()], 
                             font=("Arial", 12))
        close_btn.place(relx=1.0, rely=0.0, anchor="ne")

    def check_popups_closed(self):
        # Check if all popups are closed to allow spinning again
        self.popup_open = False
        for window in self.root.winfo_children():
            if isinstance(window, Toplevel):
                self.popup_open = True
                break

# Launch app
if __name__ == "__main__":
    root = tk.Tk()
    app = SpinningWheelApp(root)
    root.mainloop()
