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

try:

    time.sleep(0.4)    
    pwms['right_back'].ChangeDutyCycle(5)
    pwms['left_back'].ChangeDutyCycle(5)
    time.sleep(0.4)    

    for _ in range(6):  

        time.sleep(1)

        time.sleep(0.5)            
        pwms['left_front'].ChangeDutyCycle(2.5) 
        pwms['right_front'].ChangeDutyCycle(5)   
        time.sleep(0.4)    
        pwms['left_front'].ChangeDutyCycle(5)  
        pwms['right_front'].ChangeDutyCycle(1)
        time.sleep(0.5)    

        time.sleep(1)
    
    time.sleep(0.4)    
    pwms['right_back'].ChangeDutyCycle(8)
    pwms['left_back'].ChangeDutyCycle(1)
    time.sleep(0.4)    

except KeyboardInterrupt:
    pass

pwms['left_back'].ChangeDutyCycle(1)

for leg, pwm in pwms.items():
    pwm.ChangeDutyCycle(initial_positions[leg])
    time.sleep(1)

GPIO.cleanup()
