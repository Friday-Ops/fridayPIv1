import RPi.GPIO as GPIO
import time

# Configuração do modo da numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Lista dos pinos GPIO para os servos
servo_pins = {
    'right_back': 25
}

# Configuração dos pinos como saída e inicialização do PWM
pwms = {}
initial_positions = {
    'right_back': 0
}

for leg, pin in servo_pins.items():
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 60)  # 60Hz
    pwm.start(initial_positions[leg])  # Posição inicial
    pwms[leg] = pwm

try:
    for _ in range(2): 

        pwms['right_back'].ChangeDutyCycle(3) 
        time.sleep(4)
        pwms['right_back'].ChangeDutyCycle(1) 
        time.sleep(6)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
