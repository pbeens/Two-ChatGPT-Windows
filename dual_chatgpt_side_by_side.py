import subprocess
import time
import pygetwindow as gw
import sys
import os
import tkinter as tk

# === CONFIG ===
DEBUG = False
WIDTH_FACTOR = 0.5  # 0.25 = 25% width per window, adjust as needed
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE_DIRECTORY_L = "Default"
PROFILE_DIRECTORY_R = "Default"
URL = "https://chat.openai.com/"

# === FUNCTIONS ===

def get_screen_resolution():
    root = tk.Tk()
    root.withdraw()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height

def launch_chrome(url, profile_dir):
    return subprocess.Popen([
        CHROME_PATH,
        "--new-window",
        f"--profile-directory={profile_dir}",
        url
    ], shell=True if sys.platform.startswith('win') else False)

# === MAIN EXECUTION ===

if __name__ == "__main__":
    # Get screen size
    screen_width, screen_height = get_screen_resolution()

    # Calculate window sizes and centered positions
    window_width = int(screen_width * WIDTH_FACTOR)
    window_height = screen_height
    total_width = window_width * 2

    left_x = (screen_width - total_width) // 2
    right_x = left_x + window_width
    left_y = 0
    right_y = 0

    if DEBUG:
        print(f"📐 Screen: {screen_width}x{screen_height}")
        print(f"🪟 Each window: {window_width}x{window_height} (factor={WIDTH_FACTOR})")
        print(f"⬅️ Left window pos: {left_x}, {left_y}")
        print(f"➡️ Right window pos: {right_x}, {right_y}")
        print("🔁 Killing existing Chrome processes...")
    
    # Kill Chrome to ensure clean positioning
    os.system("taskkill /f /im chrome.exe >nul 2>&1")

    # Launch ChatGPT windows
    print("🚀 Launching left window...")
    launch_chrome(URL, PROFILE_DIRECTORY_L)
    time.sleep(2)

    print("🚀 Launching right window...")
    launch_chrome(URL, PROFILE_DIRECTORY_R)

    print("⏳ Waiting for Chrome windows to appear...")

    # Wait until at least two Chrome windows show up
    max_wait = 15
    elapsed = 0
    windows = []

    while elapsed < max_wait:
        windows = [w for w in gw.getWindowsWithTitle('Chrome') if w.title]
        if len(windows) >= 2:
            break
        time.sleep(1)
        elapsed += 1

    if DEBUG:
        print(f"🪟 Found {len(windows)} Chrome windows after {elapsed} seconds.")

    # Reposition windows
    positioned = 0
    for win in reversed(windows):
        try:
            if positioned == 0:
                print(f"⬅️ Moving: {win.title}")
                win.moveTo(left_x, left_y)
                win.resizeTo(window_width, window_height)
                positioned += 1
            elif positioned == 1:
                print(f"➡️ Moving: {win.title}")
                win.moveTo(right_x, right_y)
                win.resizeTo(window_width, window_height)
                positioned += 1
                break
        except Exception as e:
            print(f"⚠️ Failed to position {win.title}: {e}")

    if positioned < 2:
        print("⚠️ Not all Chrome windows were positioned. Try increasing the delay.")
    else:
        print("✅ Both ChatGPT windows launched and positioned successfully.")
