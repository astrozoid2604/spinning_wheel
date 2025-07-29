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

### 1. [Only for WindowsOS] Install WSL
- Open `PowerShell` as Administrator
    - Press `Start`, type `PowerShell`, right-click and choose `Run as Administrator`
- Run the WSL installation command
```bash
wsl --install
```
- Restart your computer when prompted
- Set up your Linux uses after restart:
    - A terminal will open asking you to create a username and password for `Ubuntu WSL terminal`.
- Upon restart, verify your installation of WSL in `PowerShell` by running below command.
```bash
wsl --list --verbose
```
- If every steps above is done correctly, you will see the `VERSION` column as `2`, and `NAME` must include Ubuntu. The `xx` below means don't-cares.
```bash
  NAME          STATE  VERSION
* Ubuuntu-xx.xx xxxx   2
```

### 2. [Only for WindowsOS] Install Conda
- Open `Ubuntu WSL terminal`. Remember to key in the username and password you set in previous step in `Install WSL`.
- Download Conda for Linux by running command below in `Ubuntu WSL terminal`.
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
```
- Run the installer
```bash
bash ~/miniconda.sh
```
- Follow the prompts
    - Accept license
    - Install to default location
    - Say "yes" to initializing Conda
- Restart your `Ubuntu WSL terminal` by closing and reopening it again upon completion of Conda installation above. Installation will take up to 15 minutes.
- Verify Conda works by running below command. If it's correct, you will see some output printed like version of the conda, etc.
```bash
conda --version
```

### 3. [Only for WindowsOS] Install Python
- Open `Ubuntu WSL terminal` and run below command to update package list.
```bash
sudo apt update
```
- Install Python 3 and Pip
```bash 
sudo apt install python3 python3-pip -y
```
- Verify installation
```bash
python3 --version
pip --version
```
- Set aliases of commands
```bash
echo "alias python=python3" >> ~/.bashrc
echo "alias pip=pip3" >> ~/.bashrc
source ~/.bashrc
```

### 4. Clone or Download the Repository
```bash
git clone git@github.com:astrozoid2604/spinning_wheel.git
cd spinning_wheel
```

### 5. Create Conda Environment
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

### 6. Activate Conda Environment
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
