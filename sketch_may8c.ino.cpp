#include <Arduino.h>
#line 1 "C:\\Users\\Wizards station\\AppData\\Local\\Temp\\.arduinoIDE-unsaved202648-16388-19nerlu.3g2n\\sketch_may8c\\sketch_may8c.ino"
#include "Arduino_BMI270_BMM150.h"

const String DEVICE_ID = "nesso_001";
unsigned long sample_count = 0;
bool recording = false;

#line 7 "C:\\Users\\Wizards station\\AppData\\Local\\Temp\\.arduinoIDE-unsaved202648-16388-19nerlu.3g2n\\sketch_may8c\\sketch_may8c.ino"
void setup();
#line 25 "C:\\Users\\Wizards station\\AppData\\Local\\Temp\\.arduinoIDE-unsaved202648-16388-19nerlu.3g2n\\sketch_may8c\\sketch_may8c.ino"
void loop();
#line 7 "C:\\Users\\Wizards station\\AppData\\Local\\Temp\\.arduinoIDE-unsaved202648-16388-19nerlu.3g2n\\sketch_may8c\\sketch_may8c.ino"
void setup() {
  Serial.begin(115200);
  delay(1000);
  
  Serial.println("=== Nesso N1 Gesture Data Collection ===");
  Serial.println("Commands:");
  Serial.println("  Press 's' to START recording");
  Serial.println("  Press 'e' to STOP recording");
  Serial.println();

  if (!IMU.begin()) {
    Serial.println("ERROR: BMI270 failed!");
    while (1);
  }

  Serial.println("Ready. Type 's' to begin...");
}

void loop() {
  // Check for Serial input (s = start, e = end)
  if (Serial.available()) {
    char cmd = Serial.read();
    
    if (cmd == 's') {
      recording = true;
      sample_count = 0;
      Serial.println("\n>>> RECORDING STARTED <<<");
      Serial.println("accelX, accelY, accelZ, gyroX, gyroY, gyroZ");
    }
    else if (cmd == 'e') {
      recording = false;
      Serial.println(">>> RECORDING STOPPED <<<");
      Serial.print("Total samples: ");
      Serial.println(sample_count);
      Serial.println("\nType 's' to record again, or label this gesture and copy data to spreadsheet");
      Serial.println();
    }
  }

  if (recording) {
    float accelX, accelY, accelZ;
    float gyroX, gyroY, gyroZ;

    if (IMU.accelerationAvailable()) {
      IMU.readAcceleration(accelX, accelY, accelZ);
    }

    if (IMU.gyroscopeAvailable()) {
      IMU.readGyroscope(gyroX, gyroY, gyroZ);
    }

    // Print CSV
    Serial.print(accelX, 3); Serial.print(",");
    Serial.print(accelY, 3); Serial.print(",");
    Serial.print(accelZ, 3); Serial.print(",");
    Serial.print(gyroX, 3); Serial.print(",");
    Serial.print(gyroY, 3); Serial.print(",");
    Serial.println(gyroZ, 3);
    
    sample_count++;
  }

  delay(50);
}
