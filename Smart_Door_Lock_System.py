import time
import os
import winsound  # Built-in Windows library for generating hardware audio signals

# System configurations
CORRECT_PIN = "4242"
ACCESS_LOG = "door_lock_log.txt"
max_attempts = 3
print("  IoT SMART DOOR LOCK SYSTEM PROTOTYPE ")
print(f"Security monitoring active. Logging to: {os.path.abspath(ACCESS_LOG)}\n")
# Initialize security file logs
if not os.path.exists(ACCESS_LOG):
    with open(ACCESS_LOG, "w", encoding="utf-8") as f:
        f.write("Timestamp, Security_Status, Event_Description\n")

def log_security_event(status, message):
    "Saves telemetry alerts directly to the security log database."
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(ACCESS_LOG, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}, {status}, {message}\n")
def trigger_hardware_alarm():
    """Simulates an IoT physical alarm buzzer using host system audio."""
    print("[ALERT] ALARM ACTIVATED! UNAUTHORIZED SYSTEM TAMPERING.")
    # Sounds three high-frequency alarm beeps (2000Hz for 400 milliseconds)
    for _ in range(3):
        winsound.Beep(2000, 400)
        time.sleep(0.1)

# Primary operational loop
attempts_remaining = max_attempts
while True:
    print(f"System State: LOCKED | Pin Attempts Left: {attempts_remaining}")
    user_input = input("Scan Keypad (Enter 4-Digit PIN) or type 'exit': ").strip()
    
    if user_input.lower() == 'exit':
        print("\nPowering down smart lock interface. Goodbye.")
        break
    if user_input == CORRECT_PIN:
        print(" [SUCCESS] ACCESS GRANTED. Door unlocked safely.\n")
        log_security_event("SUCCESS", "Authorized user entered correct PIN. Access granted.")
        # Sound a quick success confirmation tone
        winsound.Beep(1000, 200)
        attempts_remaining = max_attempts  # Reset retry counter
        time.sleep(2)  # Simulate open door time window
        print(" Auto-relocking gateway \n")
    else:
        attempts_remaining -= 1
        print(" [DENIED] INVALID PIN COMBINATION.")
        log_security_event("FAILURE", f"Invalid passcode attempt recorded: '{user_input}'")
        winsound.Beep(400, 500)  # Low error feedback buzz
        
        if attempts_remaining == 0:
            print("\n [CRITICAL] MAXIMUM FAILURE THRESHOLD EXCEEDED. LOCKDOWN INITIATED.")
            log_security_event("LOCKDOWN", "System terminal locked down due to multiple failed entry scans.")
            trigger_hardware_alarm()
        print("System frozen for 10 seconds due to high threat levels...")
        time.sleep(10)
        attempts_remaining = max_attempts  # Reset system after cooldown
        print("\nSystem online. Monitoring ready.\n")

import schemdraw
import schemdraw.elements as elm

# Initializing the schematic drawing space
with schemdraw.Drawing(file="smart_lock_circuit.png") as d:
    d.config(fontsize=11)
    
    # 1. Main Core Controller Unit
    d += (mcu := elm.Box(w=3.5, h=5).label('Microcontroller\n(Host Laptop PC)', 'center'))
    
    # 2. Input Element: 4x4 Keypad Module Matrix
    d += elm.Line().left().at(mcu.w, y=mcu.w.y + 1.5).length(1.5)
    d += (keypad := elm.Box(w=2, h=2).label('4x4 Matrix\nKeypad', 'center').anchor('east'))
    
    # 3. Output Element 1: Piezo Audio Alarm Buzzer
    d += elm.Line().right().at(mcu.e, y=mcu.e.y + 1.0).length(1.5)
    d += (buzzer := elm.Speaker().label('System Alarm\nBuzzer', 'right'))
    d += elm.Line().down().at(buzzer.south).length(0.8)
    d += elm.Ground()
    
    # 4. Output Element 2: Solenoid Electronic Door Lock Actuator
    d += elm.Line().right().at(mcu.e, y=mcu.e.y - 1.5).length(1.5)
    d += (lock := elm.Box(w=2, h=1.2).label('Electronic\nDoor Lock', 'center').anchor('west'))
    d += elm.Line().down().at(lock.south).length(0.5)
    d += elm.Ground()

print("Success! Circuit schematic generated and saved as 'smart_lock_circuit.png'.")
