import serial
import time

baud_rates = [9600, 19200, 38400, 57600, 115200]
commands = [b'CAPTURE', b'CAPTURE\n', b'CAPTURE\r\n', b'TAKEPHOTO', b'TAKEPHOTO\n', b'TAKEPHOTO\r\n', b'SNAP', b'SNAP\n', b'SNAP\r\n']

log_file = "camera_response_log.txt"

with open(log_file, "w") as log:
    for baud in baud_rates:
        for command in commands:
            try:
                ser = serial.Serial('/dev/ttyS0', baud, timeout=1)
                time.sleep(1)  # Wait for the serial connection to initialize

                log.write(f"Testing baud rate: {baud}, command: {command}\n")
                ser.write(command)
                time.sleep(2)  # Wait for the camera to process the command

                # Read response
                response = ser.read(1024)
                log.write(f"Baud rate: {baud}, Command: {command}, Response: {response}\n")

                ser.close()
            except serial.SerialException as e:
                log.write(f"Error with baud rate {baud}, command {command}: {e}\n")
            except Exception as e:
                log.write(f"Unexpected error with baud rate {baud}, command {command}: {e}\n")

print("Logging complete. Check the camera_response_log.txt file for details.")

