# Cronograma de Aulas: Arquitetura IoT

## 📋 Estrutura do Curso

### Aula 1: Introdução à Arquitetura IoT
* **Conteúdo:** Conceitos básicos, sensores, atuadores e topologias de rede.
* **Hardware:** Visão geral de componentes eletrônicos.
* **Software:** Introdução aos ambientes de desenvolvimento.

### Aula 2: Ecossistema Arduino
* **Conteúdo:** Arquitetura do microcontrolador ATmega328P e pinagem.
* **Hardware:** Placa Arduino Uno.
* **Software:** Arduino IDE e sintaxe básica de C++.

### Aula 3: Plataforma ESP32 e Conectividade
* **Conteúdo:** Arquitetura Dual-Core, Wi-Fi integrado e Bluetooth.
* **Hardware:** Módulo ESP32 NodeMCU.
* **Software:** Configuração da IDE para ESP32 e varredura de redes.

### Aula 4: Programação de Periféricos com C++
* **Conteúdo:** Leitura analógica/digital, PWM e protocolos I2C/SPI.
* **Hardware:** Arduino e ESP32 com sensores (DHT11, LDR).
* **Software:** Desenvolvimento de firmware robusto em C++.

### Aula 5: IoT com Python e MicroPython
* **Conteúdo:** Scripts em nuvem, gateways IoT e firmware embarcado.
* **Hardware:** ESP32 executando MicroPython.
* **Software:** Thonny IDE, bibliotecas `machine` e `network`.

---

## 🛠️ Tecnologias Principais

### 🔹 Arduino
* **Foco:** Prototipagem rápida e controle de hardware de baixo nível.
* **Vantagens:** Baixo custo, robustez e enorme comunidade global.
* **Limitações:** Memória reduzida e ausência de conectividade nativa.

### 🔹 ESP32
* **Foco:** Dispositivos IoT conectados e processamento de borda.
* **Vantagens:** Conectividade Wi-Fi/BLE, alto desempenho e baixo consumo.
* **Aplicações:** Cidades inteligentes, automação residencial e telemetria.

---

## 💻 Linguagens de Programação

### 🔹 C++ (Firmware)
* **Uso:** Linguagem nativa para Arduino e ESP32 (via SDK/IDE).
* **Benefício:** Desempenho máximo e controle total da memória do chip.
* **Exemplo:**
```cpp
void setup() {
  pinMode(2, OUTPUT);
}
void loop() {
  digitalWrite(2, HIGH);
  delay(1000);
  digitalWrite(2, LOW);
  delay(1000);
}
```

### 🔹 Python / MicroPython (Scripts & IoT)
* **Uso:** MicroPython no ESP32 ou Python em gateways/servidores.
* **Benefício:** Desenvolvimento veloz e facilidade para manipulação de dados.
* **Exemplo:**
```python
import machine
import time

led = machine.Pin(2, machine.Pin.OUT)
while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
```
