# Dual ChatGPT Windows: Setup Guide

This project launches two Google Chrome windows, side-by-side, each loading ChatGPT using the default Chrome profile. The windows are centered on your screen and sized based on a configurable percentage of your screen width.

While this script is designed for Windows, it could be adapted for macOS or Linux by replacing the window positioning code (pygetwindow) with platform-specific tools such as AppleScript or wmctrl.

## 📦 Download the Repository

To use this project on your own machine:

1. Click the green **Code** button on the GitHub repository page.
2. Select **Download ZIP**, then unzip it to your desired folder.
3. Alternatively, if you have Git installed, you can run:

   ```bash
   git clone https://github.com/pbeens/Two-ChatGPT-Windows.git
   ```
4. Navigate to the folder in your terminal or code editor to begin setup.

## 🚀 What This Script Does

* Opens **two Chrome windows to ChatGPT**.
* Each window uses your **logged-in Chrome profile**.
* Automatically **sizes and positions** the windows side-by-side and centered.
* Fully configurable through the script: window width, Chrome profile, and URL.

## 🧱 Prerequisites

### 1. **Install Python**

Make sure Python 3.8+ is installed.

Download from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

> ✅ Add Python to PATH during installation.

### 2. **Install `uv` Package Manager**

`uv` is a fast, modern package manager that replaces `pip` and `venv`.

Install it using PowerShell or Command Prompt:

```bash
pip install uv
```

### 3. **Create and Activate a Virtual Environment**

In your project folder:

```bash
uv venv .venv
```

Then activate it:

```bash
.venv\Scripts\activate
```

> ⚠️ **VS Code Users:** Even if you activate the venv in your terminal, VS Code may still use the wrong Python interpreter.
>
> Open the Command Palette (`Ctrl+Shift+P`), choose `Python: Select Interpreter`, and make sure it points to:
>
> ```
> .venv\Scripts\python.exe
> ```

### 4. **Install Project Dependencies**

Run this inside the activated virtual environment:

```bash
uv pip install -r requirements.txt
```

The required package is:

```text
pygetwindow
```

## 🔍 Find Your Chrome Profile and Executable Path

1. **Launch Chrome** and go to:

```
chrome://version
```

2. Find:

   * **Executable Path** → this is the full path to your Chrome installation.

     Example:

     ```
     C:\Program Files\Google\Chrome\Application\chrome.exe
     ```

   * **Profile Path** → will look like:

     ```
     C:\Users\YourName\AppData\Local\Google\Chrome\User Data\Default
     ```

     The last part is your profile name. Common ones:

     * `Default`
     * `Profile 1`

3. Plug these into your script:

```python
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE_DIRECTORY_L = "Default"
PROFILE_DIRECTORY_R = "Default"
```

## ▶️ Run the Program

Make sure your virtual environment is activated, then run:

```bash
python dual_chatgpt_windows.py
```

You should see two Chrome windows launch, logged into ChatGPT, placed side-by-side.

## 🛠 Optional Tweaks

* Adjust `WIDTH_FACTOR = 0.5` for 50% width, `0.25` for 25%, etc.
* You can replace `Default` with another Chrome profile if you want different accounts side-by-side.
* You can easily modify the script to open a different website by changing the value of the `URL` variable.
* Set `DEBUG = True` to print detailed diagnostics (screen size, window math, detected Chrome windows) when troubleshooting. Set it to `False` to suppress console output during normal use.
