# About Developer:
# Developer: Tufail Mabood (M.Sc. Str.)
# WhatsApp: +923440907874 or https://wa.me/+923440907874

# Import all libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- User-friendly input section ---
def get_float_input(prompt, default):
    """Prompt user for a float value with a default option."""
    try:
        value = input(f"{prompt} [Default: {default}]: ")
        return float(value) if value else default
    except ValueError:
        print("Invalid input. Using default value.")
        return default

def get_drift_protocol():
    """Prompt user to enter drift percentages and cycles, or use defaults."""
    print("\nEnter drift percentages and number of cycles (e.g., 0.1:3,0.25:3,0.5:3)")
    user_input = input("Leave blank to use defaults: ")

    if not user_input:
        return {
            '0.1%': 3,
            '0.25%': 3,
            '0.5%': 3,
            '1%': 3,
            '2%': 3,
            '3%': 3,
            '4%': 3
        }

    drift_protocol = {}
    try:
        entries = user_input.split(',')
        for entry in entries:
            drift, cycles = entry.split(':')
            drift = drift.strip()
            cycles = int(cycles.strip())
            drift_protocol[f"{drift}%"] = cycles
        return drift_protocol
    except Exception:
        print("Invalid format. Using default drift protocol.")
        return {
            '0.1%': 3,
            '0.25%': 3,
            '0.5%': 3,
            '1%': 3,
            '2%': 3,
            '3%': 3,
            '4%': 3
        }

# --- Get user inputs ---
time_per_cycle = get_float_input("Enter time per cycle (seconds)", 2)
sampling_rate = get_float_input("Enter sampling rate (points per second)", 100)
column_height = get_float_input("Enter column height (mm)", 1875.0)
drift_protocol = get_drift_protocol()

# --- Calculate amplitude protocol ---
amplitude_protocol = {
    drift: (float(drift.strip('%')) / 100 * column_height, cycles)
    for drift, cycles in drift_protocol.items()
}

# --- Function to create triangular waveform ---
def bidirectional_waveform(amplitude, cycle_time, samples):
    quarter_cycle = cycle_time / 4
    t = np.linspace(0, cycle_time, samples, endpoint=False)

    amp = np.piecewise(
        t,
        [
            t < quarter_cycle,  # 0 to +amplitude
            (t >= quarter_cycle) & (t < 2 * quarter_cycle),  # +amplitude to 0
            (t >= 2 * quarter_cycle) & (t < 3 * quarter_cycle),  # 0 to -amplitude
            t >= 3 * quarter_cycle  # -amplitude to 0
        ],
        [
            lambda t: amplitude * (t / quarter_cycle),
            lambda t: amplitude * (1 - (t - quarter_cycle) / quarter_cycle),
            lambda t: -amplitude * ((t - 2 * quarter_cycle) / quarter_cycle),
            lambda t: -amplitude * (1 - (t - 3 * quarter_cycle) / quarter_cycle)
        ]
    )
    
    return t, amp

# --- Generate cyclic loading data ---
time_data = []
amplitude_data = []
current_time = 0

print("\n--- Generating Cyclic Loading Data ---")
for drift, (amplitude, cycles) in amplitude_protocol.items():
    print(f"Drift: {drift}, Amplitude: {amplitude:.3f} mm, Cycles: {cycles}")
    for _ in range(cycles):
        t, amp = bidirectional_waveform(amplitude, time_per_cycle, int(sampling_rate * time_per_cycle))
        time_data.extend(current_time + t)  # Adjust time for each cycle
        amplitude_data.extend(amp)
        current_time += time_per_cycle  # Increment time for next cycle

# --- Save data to CSV ---
df = pd.DataFrame({'Time (s)': time_data, 'Amplitude (mm)': amplitude_data})
df.to_csv('cyclic_loading_protocol.csv', index=False)

# --- Plot the results ---
plt.figure(figsize=(12, 6))
plt.plot(df['Time (s)'], df['Amplitude (mm)'], label='Cyclic Loading', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (mm)')
plt.title('Cyclic Loading Protocol (Based on Drift Percentage)')
plt.grid(True)
plt.legend()
plt.show()

print("\n Cyclic loading protocol saved as 'cyclic_loading_protocol.csv'.")
