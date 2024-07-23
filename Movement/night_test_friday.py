import RPi.GPIO as GPIO
import time

# Configuração do modo da numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Função para converter ms para duty cycle
def ms_to_duty_cycle(ms):
    return (ms / 20.0) * 100

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
    'left_front': ms_to_duty_cycle(4.5),
    'right_front': 0,
    'left_back': 1,
    'right_back': 0
}

for leg, pin in servo_pins.items():
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 60)  # 60Hz
    pwm.start(initial_positions[leg])  # Posição inicial
    pwms[leg] = pwm

try:
    for _ in range(1):  
        
        time.sleep(1)
        
        pwms['left_front'].ChangeDutyCycle(1)       
        pwms['right_front'].ChangeDutyCycle(4.5)   
        time.sleep(0.2)    
        pwms['left_front'].ChangeDutyCycle(5.5)  
        pwms['right_front'].ChangeDutyCycle(1)

        time.sleep(1)
        
        pwms['left_back'].ChangeDutyCycle(1)       
        pwms['right_back'].ChangeDutyCycle(1)   
        time.sleep(2)    
        pwms['left_back'].ChangeDutyCycle(3)  
        pwms['right_back'].ChangeDutyCycle(2)

        time.sleep(1)

    for leg, pwm in pwms.items():
        pwm.ChangeDutyCycle(initial_positions[leg])
        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
