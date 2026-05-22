from machine import Pin

led = Pin(2, Pin.OUT)
led2 = Pin(4, Pin.OUT)

print("Digite:")
print("1 = Ligar LED 1")
print("0 = Desligar LED 1")
print("3 = Ligar LED 2")
print("2 = Desligar LED 2")
print("sair = encerrar programa")

while True:
    comando = input("Comando: ")
    
    if comando == "1":
        led.on()
        print("LED vermelho Ligado")
        
    elif comando == "0":
        led.off()
        print("LED vermelho Desligado")
        
    elif comando == "3":
        led2.on()
        print("LED verde Ligado")
        
    elif comando == "2":
        led2.off()
        print("LED verde Desligado")
        
    elif comando.lower() == "sair":
        led.off()
        led2.off()
        print("Programa encerrado")
        break
    
    else:
        print("Comando inválido")