# 🛡️ Cyber Security Portfolio & Labs

Bem-vindo(a) ao meu repositório central de práticas e estudos em **Segurança da Informação**.

Meu nome é Fernando e sou estudante de Segurança da Informação. Criei este espaço para documentar minha evolução técnica, mapear a construção de ambientes controlados (Sandboxes) e detalhar a execução de laboratórios de Penetration Testing e Offensive Security.

O objetivo principal deste repositório é aplicar na prática os conceitos teóricos, demonstrando habilidades de exploração de vulnerabilidades, análise de redes e documentação técnica.

---

## 🔬 Índice de Laboratórios

Abaixo está o registro cronológico dos meus projetos e laboratórios práticos. Clique no título para acessar a documentação completa, arquitetura e os resultados (prints) de cada um.

### 2026
* 📁 **[Lab 01: Configuração de Sandbox e Exploração de Backdoor (CVE-2011-2523)](./Lab_01_Exploracao_FTP/)**
  - **Foco:** Construção de sandbox isolado (Host-only), reconhecimento ativo, identificação de serviço vulnerável e exploração de backdoor (vsftpd 2.3.4).
  - **Ferramentas:** VMware, Kali Linux, Nmap, Searchsploit, Metasploit, Meterpreter.
  - **Resultados:** Exploração bem-sucedida com obtenção de sessão root e análise de pós-exploração.

* 📁 **[Lab 02: Implementação de IPS e Virtual Patching com Snort 3](./Lab_02_Implementacao_IPS/)**
  - **Foco:** Proteção preventiva em sandbox isolada usando Snort 3 como IPS para mitigar exploração de backdoor (virtual patching).
  - **Ferramentas:** Snort 3 (Lua), regras customizadas, ambientes isolados (Host-only/NAT temporário).
  - **Resultados:** Detecção e bloqueio de tentativa de exploração em tempo real; lições sobre instalação em ambientes air-gapped e tuning de DAQ (`-k none`).

* 📁 **[Lab 03: Calculadora em Bash Script](./Lab_03_Calculadora_em_Bash_Script/)**
  - **Foco:** Projeto didático em Bash para praticar scripting e I/O no terminal.
  - **Ferramentas:** Bash.
  - **Resultados:** Script funcional com operações básicas (soma, subtração, multiplicação, divisão) e tratamento de erros (divisão por zero).

* 📁 **[Lab 04: Implementação e Tuning de IDS com Snort](<./Lab_04_Implementação e Tuning de Sistema de Detecção de Intrusões (IDS) com Snort/>)**
  - **Foco:** Configuração do Snort 2.x em Ubuntu, escrita de regras customizadas e tuning para redução de falsos positivos (ex.: regras ICMP refinadas).
  - **Ferramentas:** Snort IDS, Ubuntu 24.04 LTS, ferramentas de diagnóstico de rede.
  - **Resultados:** Regras ajustadas para detectar pings ICMP externos sem gerar falsos positivos; documentação de comandos e procedimentos de validação.

* 📁 **[Lab 05: Implementação de um SOC com Wazuh SIEM XDR](<./Lab_05_Implementação de um SOC com Wazuh SIEMXDR/>)**
  - **Foco:** Instalação e configuração de um SOC (Security Operations Center) com Wazuh SIEM/XDR para coleta centralizada de eventos, correlação de alertas e monitoramento de endpoints Linux.
  - **Ferramentas:** Wazuh Manager, Wazuh Dashboard, Wazuh Agent, Ubuntu 25.10, HTTPS/443.
  - **Resultados:** Servidor Wazuh funcional com agente Linux registrado e ativo, visualização de eventos de segurança no painel de Threat Hunting.

* 📁 **[Lab 06: Auditoria e Pentest em Aplicações Web (OWASP Top 10) utilizando DVWA e Docker](<./Lab_06_Auditoria e Pentest em Aplicações Web (OWASP Top 10) utilizando DVWA e Docker/>)**
  - **Foco:** Implantação isolada de DVWA em Docker, identificação de vulnerabilidades OWASP Top 10, exploração de força bruta, SQL injection e command injection.
  - **Ferramentas:** Docker, DVWA, Hydra, SQLMap, Ubuntu.
  - **Resultados:** Ambiente vulnerável operacional, exploração valiosa de autenticação fraca, injeção SQL e execução remota de comandos.

* 📁 **[Lab 07: Port Scanner em Python](<./Lab_07_Port Scanner/>)**
  - **Foco:** Desenvolvimento de scanner de portas TCP com coleta de banners para identificação de serviços.
  - **Ferramentas:** Python 3, socket, threading, queue.
  - **Resultados:** Identificação de portas abertas e banners de serviços em alvos autorizados.

* 📁 **[Lab 08: Ataque de Negação de Serviço (DoS) - Slowloris](<./Lab_08_Ataque de Negação de Serviço (DOS)/>)**
  - **Foco:** Simulação, análise e mitigação de ataque de Negação de Serviço (DoS) da camada 7 usando Slowloris para esgotamento de pool de conexões.
  - **Ferramentas:** Kali Linux, Metasploitable 2, Apache, slowhttptest, Wireshark.
  - **Resultados:** Execução bem-sucedida do ataque com serviço Apache indisponibilizado; elaboração de estratégias de defesa como uso do módulo `mod_reqtimeout`.

* 📁 **[Lab 09: Análise de Tráfego e MITM (ARP Spoofing)](<./Lab_09_Análise de Tráfego, Interceptação e Integridade em Rede Local (MITM  ARP Spoofing)/>)**
  - **Foco:** Simulação, análise forense e execução de ataque Man-in-the-Middle (MITM) utilizando ARP Spoofing para interceptação silenciosa de tráfego.
  - **Ferramentas:** Kali Linux, Metasploitable 2, arpspoof, sysctl, Wireshark, curl.
  - **Resultados:** Execução bem-sucedida do envenenamento ARP bidirecional, roteamento invisível e interceptação de credenciais em texto claro (HTTP).

---

## 🛠️ Tecnologias e Ferramentas

Ao longo destes laboratórios, venho desenvolvendo fluência em diversas tecnologias:

* **Sistemas Operacionais:** Linux (Kali, Ubuntu), Windows.
* **Redes:** TCP/IP, Roteamento, Análise de Tráfego.
* **Segurança Ofensiva:** Nmap, Metasploit, Searchsploit, Exploit-DB.
* **Virtualização:** VMware (Configurações avançadas de rede).

---
*Aviso Legal: Todos os laboratórios documentados neste repositório foram executados estritamente em ambientes virtuais controlados (Sandboxes) e de minha propriedade. O objetivo é puramente educacional e focado na pesquisa e defesa cibernética.*