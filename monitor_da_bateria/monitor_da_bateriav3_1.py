# @DjEdu28 - Licença MIT - Copyright (c) 2022 @DjEdu28 (Luis Eduardo Silva dos Santos) 
"""
Criado por @DjEdu28 EM: 01/2022
Atualizado em: 02/2022
Monitor da bateria
versão 3.1

Objetivo da ferramenta:
    Observar a porcentagem da bateria e informar se tá descarregando ou carregando
    Ainda alertar caso chegue em um nível critico de carga
    
novidades:
    * Organizando o código
    * configurações acessíveis para fácil personalização
    
já implementado:
    * Ler dados da bateria
    * Informar por som mudança de estado
    * colorindo a tela
    * Diferenciando notificação pelo som
    * Inserindo música para as notificações
    
Ps.:
   Organizado lógica e criando variável config para fácil personalização
   Melhoria nas notificações usando arquivos de música para os sons
"""
import psutil
from time import sleep
from os import system as sys
from winsound import PlaySound

config = {
    "nivel_critico" : 50, #% da bateria
    
    # local dos arquivos sonoros
    "som_carregando" : r".\audio\[cima]mixkit-positive-notification-951.wav",
    "som_descarregando" : r".\audio\[baixo]mixkit-wrong-answer-fail-notification-946.wav",
    "som_carga_critica": r".\audio\[baixo]mixkit-software-interface-remove-2576.wav",
    
    "n_avisos":3, # numero de avisos seguidos para dar
}
"""
audios indexados: (não possuo licença para uso comercial, estão aqui apenas como exemplo e este script não é comercializado)
    bom
        [cima]mixkit-positive-notification-951.wav
    ruim
        [baixo]mixkit-game-notification-wave-alarm-987.wav
        [baixo]mixkit-software-interface-remove-2576.wav
        [baixo]mixkit-wrong-answer-fail-notification-946.wav
"""

notas = {
    "do" : 261,
    "re" : 293,             
    "mi" : 329,      
    "fa" : 349,    
    "sol": 392,  
    "la" : 0,
    "si" : 0,          
} 

#----------------------------------------------------------

def tone(freq,duration):
    from winsound import Beep
    # duration = 1000  # milliseconds
    if freq in notas: freq = notas[freq]
    
    Beep(freq, duration)

def alerta(nota="fa"):
    from time import sleep
    print('\a') # som de notificação
    for i in range(4):
        tone(notas[nota]*(i+1),300)
        sleep(0.200)

def main():
    avisos = 0
    sys("color 0F")
    print("\n"*3)
    while True:
      battery = psutil.sensors_battery()
      print("    Porcentagem:", battery.percent,end=" ")
      print("Carregando:", battery.power_plugged," "*10,end=" ")
      if battery.percent < config["nivel_critico"] and battery.power_plugged == False:
        sys("color 47")
        # [tone(3300,200*n) for n in range(1,4)]
        #alerta()
        PlaySound(config["som_carga_critica"],0)
        print("Bateria baixa",sep="")
        
      elif (battery.power_plugged == False and avisos<config[n_avisos]):
        sys("color 67")
        #tone(4000,400)
        #alerta(nota="do")
        print('\t'+"Plug desconectado")
        PlaySound(config["som_descarregando"],0)
        avisos+=1
      elif (battery.power_plugged and avisos>=config[n_avisos]):
        avisos = 0
        #tone(1100,200);tone(1100,300)
        #alerta(nota="do")
        print("\tCarregando...")
        PlaySound(config["som_carregando"],0)
        sys("color 2F")
      elif (battery.percent > 50 and battery.power_plugged):
        sys("color 0F")
      print(end="\r")
      sleep(5)

if __name__ == "__main__":
    main()
