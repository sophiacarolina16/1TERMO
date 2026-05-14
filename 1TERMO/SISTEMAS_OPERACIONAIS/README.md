# Cronograma de Aulas: Sistemas Operacionais (Windows, Linux e iOS)

## 📋 Estrutura do Curso

### Aula 1: Introdução e Arquitetura de Kernel
* **Conteúdo:** Papel do SO, modo usuário vs. modo kernel, tipos de estruturas.
* **Windows:** Abordagem do Kernel Híbrido e a camada de abstração de hardware (HAL).
* **Linux:** Funcionamento do Kernel Monolítico e carregamento dinâmico de módulos (LKM).
* **iOS:** Estrutura do ecossistema Darwin, kernel XNU e as camadas do sistema (Cocoa Touch até Core OS).

### Aula 2: Gerenciamento de Processos e Threads
* **Conteúdo:** Ciclo de vida de processos, troca de contexto e algoritmos de escalonamento.
* **Windows:** Escalonamento baseado em prioridades dinâmicas e o conceito de *Fibers*.
* **Linux:** O escalonador *Completely Fair Scheduler* (CFS) e criação de processos com `fork()`.
* **iOS:** Priorização de threads da interface de usuário e gerenciamento via *Grand Central Dispatch* (GCD).

### Aula 3: Gerenciamento de Memória
* **Conteúdo:** Memória virtual, paginação, segmentação e estratégias de alocação.
* **Windows:** Alocação com o gerenciador de memória do NT e paginação no arquivo `pagefile.sys`.
* **Linux:** Mecanismo de paginação sob demanda e o uso de partições ou arquivos *Swap*.
* **iOS:** Ausência de *Swap* tradicional, compressão de memória RAM e descarte de dados limpos.

### Aula 4: Sistemas de Arquivos e Armazenamento
* **Conteúdo:** Alocação de blocos, indexação, permissões e tolerância a falhas.
* **Windows:** Estrutura do NTFS, tabela master de arquivos (MFT) e permissões avançadas (ACLs).
* **Linux:** O padrão Ext4, sistema de indexação por *inodes* e a árvore de diretórios unificada.
* **iOS:** O sistema Apple File System (APFS), criptografia nativa forte e clonagem instantânea de arquivos.

### Aula 5: Segurança, Ciclo de Vida e Segundo Plano
* **Conteúdo:** Isolamento de processos, níveis de privilégio e políticas de execução.
* **Windows:** Controle de Conta de Usuário (UAC) e subsistemas de segurança de credenciais.
* **Linux:** Permissões POSIX (Read, Write, Execute), usuários *root* e módulos LSM (SELinux/AppArmor).
* **iOS:** Conceito de *Sandboxing* estrito, congelamento de apps e restrições de execução em segundo plano.

---

## 🛠️ Visão Geral das Plataformas

### 🔹 Microsoft Windows
* **Foco:** Mercado corporativo, desktops domésticos e retrocompatibilidade com aplicações legadas (Win32).
* **Características:** Interface gráfica integrada, forte ecossistema de ferramentas administrativas e gerenciamento por Registro.

### 🔹 Linux
* **Foco:** Servidores de alta performance, supercomputadores, dispositivos embarcados e ambientes de nuvem.
* **Características:** Código aberto, modularidade extrema, forte dependência de CLI e alta capacidade de customização.

### 🔹 Apple iOS
* **Foco:** Dispositivos móveis corporativos e de consumo integrado ao ecossistema de hardware proprietário Apple.
* **Características:** Foco total na experiência do usuário, segurança nativa por hardware e otimização severa de recursos energéticos.
