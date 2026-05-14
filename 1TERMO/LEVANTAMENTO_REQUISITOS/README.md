# Documento de Levantamento de Requisitos: Sistema de Arquitetura IoT

## 🎯 Conteúdo das Aulas (Escopo do Sistema)
* **Módulo Hardware:** Integração de placas Arduino Uno e ESP32 com sensores industriais.
* **Módulo Conectividade:** Protocolos de comunicação MQTT, HTTP e WebSockets.
* **Módulo Firmware:** Desenvolvimento de códigos em C++ e scripts em MicroPython.
* **Módulo Monitoramento:** Coleta de dados, geração de alertas e relatórios automatizados.

---

## ⚙️ Requisitos Funcionais (RF)
* **RF-001:** O sistema deve coletar dados dos sensores via ESP32 a cada 5 segundos.
* **RF-002:** O firmware deve permitir a configuração local de credenciais Wi-Fi.
* **RF-003:** A plataforma deve emitir alertas visuais quando os limites dos sensores forem excedidos.
* **RF-004:** O sistema deve exportar relatórios técnicos em formato PDF e CSV.
* **RF-005:** O painel de controle deve exibir gráficos de telemetria em tempo real.

---

## 🔒 Requisitos Não Funcionais (RNF)
* **RNF-001:** As mensagens MQTT devem ser criptografadas utilizando o protocolo TLS 1.3.
* **RNF-002:** O microcontrolador ESP32 deve operar em modo *Deep Sleep* para economizar bateria.
* **RNF-003:** O tempo de resposta do acionamento de um atuador não deve passar de 200ms.
* **RNF-004:** A interface web de monitoramento deve ser responsiva para smartphones e computadores.
* **RNF-005:** O firmware em C++ deve ocupar no máximo 75% da memória flash do Arduino.

---

## 🔄 Topologia Ágil (Processo de Desenvolvimento)
* **Sprints:** Ciclos de desenvolvimento quinzenais com entregas de incrementos de hardware/software.
* **Daily Scrum:** Reuniões diárias de 15 minutos para alinhamento de travas técnicas.
* **Sprint Backlog:** Divisão de tarefas focadas em prototipagem, testes de bancada e código.
* **Review:** Demonstração prática do circuito funcionando ao final de cada ciclo.

---

## 📊 Relatórios Técnicos (Entregáveis)
* **Relatório de Validação:** Testes de estresse de conectividade Wi-Fi e perda de pacotes.
* **Relatório de Consumo:** Análise de corrente elétrica do ESP32 em diferentes modos de energia.
* **Dossiê de Firmware:** Documentação de todas as funções, bibliotecas e APIs utilizadas.

---

## 🗺️ Diagramas Necessários
* **Diagrama de Blocos:** Mapeamento do hardware (sensores ➡️ microcontrolador ➡️ atuadores).
* **Diagrama de Arquitetura:** Fluxo de dados da borda (Edge) até o servidor em Nuvem (Cloud).
* **Diagrama de Casos de Uso:** Interações do usuário e do administrador com o painel IoT.
* **Esquemático de Circuitos:** Conexões elétricas detalhadas utilizando softwares como Fritzing ou Proteus.
