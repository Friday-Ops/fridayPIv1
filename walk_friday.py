import RPi.GPIO as GPIO
import time

# Configuração do modo da numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Lista dos pinos GPIO para os servos
servo_pins = {
    'left_front': 17,
    'right_front': 18,
    'left_back': 22,
    'right_back': 25
}

# Configuração dos pinos como saída e inicialização do PWM
pwms = {}
initial_positions = {
    'left_front': 0,
    'right_front': 0,
    'left_back': 0,
    'right_back': 0
}

for leg, pin in servo_pins.items():
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 60)  # 60Hz
    pwm.start(initial_positions[leg])  # Posição inicial
    pwms[leg] = pwm

def smooth_move(pwm, start, end, steps=10, delay=0.003):
    increment = (end - start) / steps
    for i in range(steps):
        start += increment
        pwm.ChangeDutyCycle(start)
        time.sleep(delay)

try:
    time.sleep(0.4)
    smooth_move(pwms['right_back'], initial_positions['right_back'], 5)
    smooth_move(pwms['left_back'], initial_positions['left_back'], 6)
    time.sleep(0.4)

    for _ in range(3):
        time.sleep(1)
        
        time.sleep(0.5)
        smooth_move(pwms['left_front'], initial_positions['left_front'], 2.5)
        smooth_move(pwms['right_front'], initial_positions['right_front'], 5)
        time.sleep(0.2)
        smooth_move(pwms['left_front'], 2.5, 5)
        smooth_move(pwms['right_front'], 5, 1)
        time.sleep(0.5)
        
        time.sleep(1)
    
    time.sleep(0.3)
    smooth_move(pwms['right_back'], 5, 11)
    smooth_move(pwms['left_back'], 5, 1)
    time.sleep(0.3)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
