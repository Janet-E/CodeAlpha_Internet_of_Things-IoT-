import time
import random
import os

# Optimal Operational Thresholds (Aquaculture)
MIN_TEMP, MAX_TEMP = 14.0, 24.0
MIN_OXYGEN         = 5.0
MIN_SALINITY, MAX_SALINITY = 28.0, 36.0
MIN_PH, MAX_PH     = 7.5, 8.5

LOG_FILE = "marine_sensor_log.txt"
print(" INITIALIZING IoT MARINE MONITORING SENSOR ")
print(f"System logging activated. Stream saving to: {os.path.abspath(LOG_FILE)}\n")
# Step 1: Open the file fresh and write the header row
with open(LOG_FILE, "w", encoding="utf-8") as f:
    f.write("Timestamp, Temp(C), DO(mg/L), Salinity(PPT), pH, Status\n")

# Step 2: Continuous real-time streaming loop
try:
    while True:
        # Simulate fluctuating marine readings
        water_temp = round(random.uniform(12.0, 26.0), 2)
        oxygen     = round(random.uniform(4.0, 8.5), 2)
        salinity   = round(random.uniform(26.0, 38.0), 2)
        ph_units   = round(random.uniform(7.0, 9.0), 2)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        anomalies = []

        # Validate conditions against environmental boundaries
        if not (MIN_TEMP <= water_temp <= MAX_TEMP):
            anomalies.append(f"Temp Error ({water_temp}°C)")
        if oxygen < MIN_OXYGEN:
            anomalies.append(f"Low Oxygen ({oxygen} mg/L)")
        if not (MIN_SALINITY <= salinity <= MAX_SALINITY):
            anomalies.append(f"Salinity Error ({salinity} PPT)")
        if not (MIN_PH <= ph_units <= MAX_PH):
            anomalies.append(f"pH Error ({ph_units})")
        status_msg = "ALERT: " + " | ".join(anomalies) if anomalies else "System Stable"

        # Stream directly to PowerShell console screen
        print(f"[{timestamp}] Temp: {water_temp}°C | DO: {oxygen}mg/L | Salinity: {salinity}PPT | pH: {ph_units}")
        print(f"Status: {status_msg}")
        print("-" * 60)

        # Force write current state data to disk instantly
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp}, {water_temp}, {oxygen}, {salinity}, {ph_units}, {status_msg}\n")

        # Pause exactly one second before generating the next line of real-time data
        time.sleep(1)
except KeyboardInterrupt:
    print("\nTelemetry data stream terminated safely.")




    
