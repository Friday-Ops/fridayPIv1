import RPi.GPIO as GPIO
import time

# Configuração do modo da numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Lista dos pinos GPIO para os servos
servo_pins = {
    'left_front': 17
}

# Função para converter ms para duty cycle
def ms_to_duty_cycle(ms):
    return (ms / 20.0) * 100

# Configuração dos pinos como saída e inicialização do PWM
pwms = {}
initial_positions = {
    'left_front': ms_to_duty_cycle(4.5)
}

for leg, pin in servo_pins.items():
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 60)  # 60Hz
    pwm.start(initial_positions[leg])  # Posição inicial
    pwms[leg] = pwm

try:
    for _ in range(1):  # Executar o ciclo uma vezes

        time.sleep(2)
        pwms['left_front'].ChangeDutyCycle(2.5) 
        time.sleep(2)
        pwms['left_front'].ChangeDutyCycle(5.5)  # Voltar para posição neutra
        time.sleep(2)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
