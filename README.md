# 🎡 Spinning Wheel App

This Python project is a simple GUI-based **Spinning Wheel** game with 16 labeled sectors (`Q1` to `Q16`). Click the "Spin Me!" button to spin the wheel, and a pop-up will prompt you to answer the question pointed by the arrow.

<p align="center">
  <a href="https://www.youtube.com/watch?v=L9rrCugr63A">
    <img src="video_thumbnail.png" alt="Watch the demo" width="480">
  </a>
</p>


---

## 🧰 Features

- Graphical wheel with 16 labeled sectors
- Red down arrow to indicate selected question
- "Spin Me!" button triggers animated wheel spin
- Smooth deceleration with random landing
- Pop-up window displays the selected question

---

## 📦 Requirements

- Python 3.10+
- Conda (recommended)
- Packages:
  - `tk`
  - `pillow`

---

## 🛠 Installation

### 1. Clone or Download the Repository
```bash
git clone git@github.com:astrozoid2604/spinning_wheel.git
cd spinning_wheel
```

### 2. Create Conda Environment
Save this file as `wheel.yaml`:
```yaml
name: wheel
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.10
  - pillow
  - tk
```

Then create the environment:
```bash
conda env create -f wheel.yaml
```

### 3. Activate Environment
```bash
conda activate wheel
```

---

## ▶️ Running the App

Once the environment is active, run the script:
```bash
python wheel.py
```

---

## 📌 Notes

- The wheel uses the **Pillow** library to draw and rotate the sectors.
- The red arrow at the top of the window always points to the selected question after each spin.

---

## 📤 License

This project is for educational and personal use. No license enforced.
