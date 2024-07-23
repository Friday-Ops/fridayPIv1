import RPi.GPIO as GPIO
import time

# Configuração do modo da numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Pino GPIO para o servo motor
servo_pin = 18  # Ajuste conforme necessário

# Configuração do pino como saída e inicialização do PWM
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz
pwm.start(0)  # Posição neutra

try:
    while True:
        # Movimento anti-horário (original)
        pwm.ChangeDutyCycle(3)  # Movimenta anti-horário
        time.sleep(2)

        pwm.ChangeDutyCycle(1)  # Movimenta anti-horário
        time.sleep(4)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
