# Gesture Recognition on Embedded Hardware

## What This Project Does
A real-time gesture recognition system that runs directly on the Arduino Nesso N1 microcontroller. The device captures motion data from its built-in sensors, processes it locally using machine learning, and identifies gestures (shake, tap, swipe, circle, double-tap) in real-time.

All processing happens on the device itself—no cloud connection needed, no latency, no privacy concerns.

## Why It Matters
Most AI systems rely on cloud servers, which creates latency and privacy risks. This project demonstrates **edge AI**: running intelligent models directly on small devices. This approach is essential for:

- Real-time responsiveness (no network delays)
- Privacy (data stays on your device)
- Battery efficiency (local processing uses less power than cloud connectivity)
- Reliability (works offline)

## How It Works
1. **Sensor captures motion** — 6-axis motion data from BMI270 IMU
2. **Model processes data locally** — TensorFlow Lite Micro runs inference on device
3. **Gesture is recognized** — Result displayed in ~80 milliseconds
4. **Repeat** — Ready for next gesture

## Real-World Applications
- **Smart Wearables** — Gesture-controlled smartwatches or fitness trackers
- **IoT Devices** — Motion-based interaction without touchscreens
- **Accessibility** — Gesture commands for people with limited mobility
- **Vehicle Interfaces** — Hand gestures for in-car control (relevant for driving simulators)
- **Robotics** — Real-time gesture recognition for robot interaction

## Future: Cloud-Based Retraining
The current system uses a fixed model. The next phase will add **cloud retraining**:

1. **Device collects new gesture data** over time
2. **Data is anonymized and uploaded to cloud**
3. **Model is retrained monthly** with new data
4. **Updated model is downloaded back to device**
5. **Recognition accuracy improves over time**

This creates a **feedback loop**: the device learns from real-world usage while maintaining privacy through local processing.

## Technical Details
- Microcontroller: Arduino Nesso N1 (ESP32-C6, 512 KB RAM)
- Sampling Rate: 20 Hz
- Model Type: Quantized CNN (~50 KB)
- Inference Speed: <100ms per gesture
