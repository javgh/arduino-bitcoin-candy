import serial

def trigger_arduino(arduino_port):
    conn = serial.Serial(arduino_port, 9600)
    conn.write('.')

if __name__ == "__main__":
    trigger_arduino('/dev/ttyUSB0')
