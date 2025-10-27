import time
import random
import queue
import threading

# Queue to simulate serial communication between "ESP32" and "Python AI"
serial_out = queue.Queue()
serial_in = queue.Queue()

# -------------------------------
# VIRTUAL ESP32 BEHAVIOR
# -------------------------------
def esp32_simulator():
    while True:
        # Fake temperature sensor data (20.0–30.0 °C)
        temp = round(random.uniform(20.0, 30.0), 1)
        serial_out.put(f"TEMP:{temp}")
        # Wait 3 seconds before sending next reading
        time.sleep(3)

        # Check for AI command
        try:
            cmd = serial_in.get_nowait()
            print(f"[ESP32] CMD_RECEIVED: {cmd}")
        except queue.Empty:
            pass

# -------------------------------
# MAIN PROGRAM (your Python + Gemini AI)
# -------------------------------
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-pro")

def ai_controller():
    while True:
        if not serial_out.empty():
            line = serial_out.get()
            if line.startswith("TEMP:"):
                temp = float(line.split(":")[1])
                print(f"[Sensor] Temperature: {temp}°C")

                # Ask Gemini what to do
                prompt = f"The spacecraft cabin temperature is {temp}°C. Suggest an appropriate action (short answer)."
                response = model.generate_content(prompt)
                action = response.text.strip()
                print(f"[Gemini AI] {action}\n")

                # Send command back to ESP32
                serial_in.put(action)

        time.sleep(20)

# -------------------------------
# START SIMULATION
# -------------------------------
print("Starting Geminaut ESP32 simulation...")
threading.Thread(target=esp32_simulator, daemon=True).start()
ai_controller()
