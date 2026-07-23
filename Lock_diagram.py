import matplotlib.pyplot as plt

# Create the canvas space
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)

# 1. Draw the Main Microcontroller Unit (MCU Box)
mcu = plt.Rectangle((3.5, 1), 3, 4, fill=True, color='lightskyblue', alpha=0.5, edgecolor='black', lw=2)
ax.add_patch(mcu)
ax.text(5, 3, "Microcontroller\n(Host Laptop PC)", ha='center', va='center', fontweight='bold')

# 2. Draw the Input Matrix Keypad Box
keypad = plt.Rectangle((0.5, 2), 1.5, 2, fill=True, color='lightgray', alpha=0.7, edgecolor='black', lw=1.5)
ax.add_patch(keypad)
ax.text(1.25, 3, "4x4 Matrix\nKeypad\n(Inputs)", ha='center', va='center', fontsize=9)

# 3. Draw the Alarm Buzzer Box
buzzer = plt.Rectangle((7.5, 3.5), 1.5, 1.2, fill=True, color='salmon', alpha=0.7, edgecolor='black', lw=1.5)
ax.add_patch(buzzer)
ax.text(8.25, 4.1, "Piezo Audio\nBuzzer\n(Output 1)", ha='center', va='center', fontsize=9)

# 4. Draw the Door Lock Actuator Box
lock = plt.Rectangle((7.5, 1.3), 1.5, 1.2, fill=True, color='palegreen', alpha=0.7, edgecolor='black', lw=1.5)
ax.add_patch(lock)
ax.text(8.25, 1.9, "Electronic\nDoor Lock\n(Output 2)", ha='center', va='center', fontsize=9)

# 5. Connect Wiring Lines
# Keypad to MCU
ax.plot([2.0, 3.5], [3, 3], color='black', lw=2, linestyle='-')
# MCU to Buzzer
ax.plot([6.5, 7.5], [4.1, 4.1], color='black', lw=2, linestyle='-')
# MCU to Door Lock
ax.plot([6.5, 7.5], [1.9, 1.9], color='black', lw=2, linestyle='-')

# Remove axis lines for a clean schematic look
ax.axis('off')
plt.title("IoT Smart Door Lock Prototype - Schematic Diagram", fontsize=12, fontweight='bold', pad=15)

# Save the schematic layout immediately
plt.savefig("smart_lock_circuit.png", bbox_inches='tight', dpi=300)
print(" Success! Circuit schematic generated using Matplotlib and saved as 'smart_lock_circuit.png'.")

