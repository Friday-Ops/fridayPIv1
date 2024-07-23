import RPi.GPIO as GPIO
import time

# Configuração do modo da numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Lista dos pinos GPIO para os servos
servo_pins = {
    'left_back': 22
}

# Configuração dos pinos como saída e inicialização do PWM
pwms = {}
initial_positions = {
    'left_back': 0
}

for leg, pin in servo_pins.items():
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 60)  # 60Hz
    pwm.start(initial_positions[leg])  # Posição inicial
    pwms[leg] = pwm

try:
    for _ in range(1):  # Executar o ciclo uma vezes

        # Movimentar as pernas traseiras
        pwms['left_back'].ChangeDutyCycle(3) 
        time.sleep(2)
        pwms['left_back'].ChangeDutyCycle(1) 
        time.sleep(5)


except KeyboardInterrupt:
    pass

GPIO.cleanup()
