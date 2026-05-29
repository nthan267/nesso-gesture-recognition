# collect.py
# Place in: C:\Users\Wizards station\Documents\Arduino\
# Run:      python collect.py
# Requires: pip install pyserial
#
# IMPORTANT: Close Arduino Serial Monitor before running
# Handles DISCARD signal — weak captures are automatically thrown away

import serial
import serial.tools.list_ports
import csv
import os

OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gesture_data.csv')
BAUD_RATE   = 115200

def find_port():
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if any(x in p.description.upper() for x in ['USB','CH340','CP210','UART','NESSO']):
            return p.device
    print("\nAvailable ports:")
    for i, p in enumerate(ports):
        print(f"  {i}: {p.device} — {p.description}")
    return ports[int(input("Enter number: "))].device

def main():
    port = find_port()
    print(f"Connecting to {port}...\n")

    file_exists = os.path.isfile(OUTPUT_FILE)
    csvfile = open(OUTPUT_FILE, 'a', newline='')
    writer  = csv.writer(csvfile)

    if not file_exists:
        writer.writerow(['accelX','accelY','accelZ','gyroX','gyroY','gyroZ','label'])
        print(f"Created: {OUTPUT_FILE}")
    else:
        print(f"Appending to: {OUTPUT_FILE}")

    ser = serial.Serial(port, BAUD_RATE, timeout=2)
    print("Board calibrating — hold still for 3 seconds...")
    print("Ctrl+C to stop.\n")

    current_label  = None
    pending_rows   = []   # buffer rows until END or DISCARD
    session_count  = 0
    discard_count  = 0
    total_rows     = 0
    captures = {g: 0 for g in ['circle','shake','swipe_h','swipe_v','tap']}

    try:
        while True:
            raw = ser.readline()
            if not raw:
                continue
            try:
                line = raw.decode('utf-8').strip()
            except:
                continue

            if line.startswith('BASELINE:'):
                print(f"Calibrated. Baseline: {line.split(':')[1]}")
                print("Ready! Do your gestures.\n")

            elif line.startswith('LABEL:'):
                current_label = line.split(':', 1)[1].strip()
                pending_rows  = []
                print(f"[REC] {current_label:<12} ", end='', flush=True)

            elif line == 'END':
                # Write all pending rows to CSV
                for row in pending_rows:
                    writer.writerow(row)
                csvfile.flush()
                total_rows += len(pending_rows)
                if current_label in captures:
                    captures[current_label] += 1
                print(f"→ {len(pending_rows)} rows  ({captures.get(current_label,0)} captures)")
                pending_rows  = []
                current_label = None

            elif line == 'DISCARD':
                discard_count += 1
                print(f"→ DISCARDED (too weak) [{discard_count} total discards]")
                pending_rows  = []
                current_label = None

            elif current_label and ',' in line:
                parts = line.split(',')
                if len(parts) == 6:
                    try:
                        pending_rows.append([float(p) for p in parts] + [current_label])
                    except ValueError:
                        pass

    except KeyboardInterrupt:
        print(f"\n{'='*35}")
        print("Session summary:")
        for g, c in captures.items():
            print(f"  {g:<12}: {c} captures")
        print(f"\nDiscarded: {discard_count}")
        print(f"Total rows saved: {total_rows}")
        print(f"File: {OUTPUT_FILE}")

    finally:
        csvfile.close()
        ser.close()

if __name__ == '__main__':
    main()
