import ctypes

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

print(f"Detected screen resolution: {width}x{height}")
