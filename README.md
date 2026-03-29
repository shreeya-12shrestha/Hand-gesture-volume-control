# 🖐️ Hand Gesture Volume Control

Control your computer's volume using hand gestures — no keyboard, no mouse!  
Built with Python, OpenCV, and MediaPipe.

## How It Works

- Shows a **live webcam feed** with hand landmarks drawn on it
- Tracks your **index finger tip** (yellow dot) and **thumb tip** (red dot)
- Draws a **green line** between them
- If the distance between fingers is **large** → 🔊 Volume Up
- If the distance is **small** → 🔉 Volume Down

## Built With

- [Python](https://python.org)
- [OpenCV](https://opencv.org) — webcam feed & drawing
- [MediaPipe](https://mediapipe.dev) — real-time hand tracking (21 landmarks)
- [PyAutoGUI](https://pyautogui.readthedocs.io) — controls system volume

## Installation
```bash
pip install opencv-python mediapipe pyautogui
```

## Run
```bash
python volume_control.py
```

> Press **ESC** to exit the webcam window.

## Usage

1. Run the script
2. Show your hand to the webcam
3. **Spread** index finger & thumb → Volume goes UP 🔊
4. **Pinch** index finger & thumb → Volume goes DOWN 🔉

## Notes

- Works with **two hands** simultaneously
- Make sure your webcam is connected
- Best used in good lighting
