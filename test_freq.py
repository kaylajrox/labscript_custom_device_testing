import serial

COM_PORT = "COM5"
BAUD_RATE = 115200  # Not necessary for SynthUSB3 but required for opening the port


frequency_choice = 850.0 # MHz
power_choice = 4.0 # dbm


frequency = f"f{frequency_choice}"
power =f"W{power_choice}"


# Open serial connection
ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)

def send_command(command):
    """Send a command to SynthUSB3 and read response (if applicable)"""
    ser.write(command.encode())  # Send command
    response = ser.read(100).decode().strip()  # Read response
    return response

# Example: Set frequency to 1000 MHz
response = send_command(frequency)
print(f"Outputting frequency of {frequency_choice} MHz")

# Example: Query current frequency
response = send_command("f?")
print(f"Current Frequency: {response} MHz")


# Example: Set frequency to 1000 MHz
response2 = send_command(power)
print(f"Outputting power of {power_choice} dBm")

# Example: Query current frequency
response2 = send_command("f?")
print(f"Current power: {response2} dBm")

# Close the connection
ser.close()
