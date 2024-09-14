import RPi.GPIO as GPIO
from LoRaRF import SX126x

# Define the GPIO pins
NSS_PIN = 8
RESET_PIN = 22
BUSY_PIN = 23
DIO1_PIN = 24  # Optional, can be used for interrupts

# Initialize the LoRa module
LoRa = SX126x()

def setup():
    GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering
    GPIO.setup(NSS_PIN, GPIO.OUT)
    GPIO.setup(RESET_PIN, GPIO.OUT)
    GPIO.setup(BUSY_PIN, GPIO.IN)
    GPIO.setup(DIO1_PIN, GPIO.IN)

    # Set the pins for the LoRa module
    LoRa.setPins(NSS_PIN, RESET_PIN, BUSY_PIN, DIO1_PIN)

    # Begin communication with the LoRa module
    if not LoRa.begin():
        print("LoRa initialization failed!")
        exit(1)
    print("LoRa Initialized!")

def loop():
    # Your LoRa transmission and reception code goes here
    print("HelloWorld")
    pass

if __name__ == "__main__":
    setup()
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up GPIO on exit