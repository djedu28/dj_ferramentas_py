# Monitor da Bateria (testado em Windows)

## Historia
Todo projeto começa de uma necessidade, a minha era monitorar a bateria do notebook
com problemas no carregador, não podia tirar o olho do ícone de carga na bandeja, 
ou então o notebook descarregava e eu só ia saber quando o Windows fosse me notificar (com 15% de carga restante)
o que é tarde de mais.

Por conta da dificuldade que era carregar, quanto mais cedo soubesse que tava descarregando, mais cedo poderia corrigir.

Então esse programa informa se o carregador foi conectado/desconectado  
e faz ininterruptos  alertas assim que atingir o nível critico (que eu defini 50%)

## Objetivo da ferramenta:
- Observar a porcentagem da bateria e informar se tá descarregando ou carregando
- Ainda alertar caso chegue em um nível critico de carga

# Versões
*	[V0.1](/monitor_da_bateriav0_1.py) — Beta
*	[V1.0](/monitor_da_bateriav1.py) — Colorindo a tela
*	[V2.0](/monitor_da_bateriav2.py) — Notificação com som padrão do sistema
*	[V2.1](/monitor_da_bateriav2_1.py) — Melhorando notificação sonora (usando tons/notas musicais)
*	[V3.0](/monitor_da_bateriav3.py) — Inserindo música nas notificações (reproduzindo arquivo de música)
*	[V3.1](/monitor_da_bateriav3_1.py) — Organizando o código para publicação

# Sobre a V3.1

## novidades:
*	Organizando o código
*	configurações acessíveis para fácil personalização
	
## já implementado:
*	Ler dados da bateria
*	Informar por som mudança de estado
*	colorindo a tela
*	Diferenciando notificação pelo som
*	Inserindo música para as notificações

# REQUISITOS

## python 3.0+
acesse [https://www.python.org/](https://www.python.org/) para instalar

## psutil
psutil (utilitários de processo e sistema), para saber mais [clique aqui](https://pypi.org/project/psutil/).

### para instalar, basta
	pip install psutil

