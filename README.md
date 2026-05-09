### Gesture Recognition on Embedded Hardware
### Real-time ML Inference on Arduino Nesso N1

### Overview
Built a complete end-to-end gesture recognition system using TensorFlow Lite Micro on the Arduino Nesso N1. 

The device captures 6-axis motion data, classifies gestures in real-time with <100ms latency, and displays results on the integrated touchscreen—all within a microcontroller with 512 KB SRAM.
This project demonstrates the full embedded ML pipeline: sensor integration → data collection → model training → quantization → deployment → real-time inference.

### Why This Matters
Edge AI inference on resource-constrained hardware is critical for:
- **Low latency** — No cloud dependency, instant local processing
- **Privacy** — Data never leaves the device
- **Battery efficiency** — Inference runs in milliseconds
- **Scalability** — Deploy to millions of devices without server load

### Gestures (5-class Classification)
- **SHAKE** — Rapid back-and-forth motion
- **SWIPE** — Quick side-to-side motion  
- **TAP** — Tilted knock motion
- **CIRCLE** — Rotate hand in circle
- **DOUBLE_TAP** — Two quick taps in succession

### Technical Stack
- **Hardware**: Arduino Nesso N1 (ESP32-C6 @ 160 MHz, 512 KB SRAM)
- **Sensor**: BMI270 6-axis Inertial Measurement Unit (accelerometer + gyroscope)
- **Framework**: TensorFlow Lite Micro
- **Model**: Quantized Convolutional Neural Network (~50 KB, int8)
- **Sampling**: 20 Hz IMU capture
- **Inference Latency**: ~80ms per gesture

### Data Pipeline
1. **Collection**: 1000+ samples per gesture @ 20 Hz (CSV format)
2. **Training**: Convolutional Neural Network model trained on motion time-series data
3. **Optimization**: Post-training int8 quantization (4x size reduction, 2x faster inference)
4. **Deployment**: TFLite Micro model embedded in Arduino firmware
5. **Inference**: Real-time classification on device, <100ms latency

### Applications
- Smart wearables with gesture control
- IoT devices with motion-based interaction
- Vehicle interfaces (relevant for simulators requiring real-time gesture recognition)
- Accessibility interfaces with gesture commands

### Files
- `sketch_may8c.ino` — Data collection & inference firmware
- `gesture_training_data.xlsx` — Labeled training dataset (500+ samples)
- `README.md`

### Future Aim
- Federated learning with cloud retraining pipeline

**Skills Demonstrated**
- Embedded systems programming (C++)
- Sensor integration (I2C IMU)
- Machine learning model optimization
- Real-time inference on microcontrollers
- Hardware-constrained algorithm design
