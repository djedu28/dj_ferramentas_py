# @DjEdu28 - Licença MIT - Copyright (c) 2022 @DjEdu28 (Luis Eduardo Silva dos Santos) 
"""
Criado por @DjEdu28 EM: 01/2022
Atualizado em: 02/2022
Monitor da bateria
versão 3.0

Objetivo da ferramenta:
    Observar a porcentagem da bateria e informar se tá descarregando ou carregando
    Ainda aletar caso chegue em um nivel critico de carga
    
novidades:
    * Inserindo musica para as notificações
    
já implementado:
    * Ler dados da bateria
    * Informar por som mudança de estado
    * colorindo a tela
    * Diferenciando notificação pelo som
    * Melhorando notificação sonora (bipes diferentes)
    
Ps.:
   Melhoria nas notificações usando arquivos de musica para os sons
"""
import psutil
from time import sleep
from os import system as sys
from winsound import PlaySound

notas = {
    "do" : 261,
    "re" : 293,             
    "mi" : 329,      
    "fa" : 349,    
    "sol": 392,  
    "la" : 0,
    "si" : 0,          
} 

cima = r".\audio\[cima]mixkit-positive-notification-951.wav"
baixo = [
    r".\audio\[baixo]mixkit-wrong-answer-fail-notification-946.wav",
    r".\audio\[baixo]mixkit-software-interface-remove-2576.wav",
    r".\audio\[baixo]mixkit-game-notification-wave-alarm-987.wav",
]

# def alerta(nota="fa"):
    # from time import sleep
    # print('\a') # som de notificação
    # for i in range(4):
        # tone(notas[nota]*(i+1),300)
        # sleep(0.200)

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
      if battery.percent < 50 and battery.power_plugged == False:
        sys("color 47")
        # [tone(3300,200*n) for n in range(1,4)]
        #alerta()
        PlaySound(baixo[1],0)
        print("Bateria baixa",sep="")
        
      elif (battery.power_plugged == False and avisos<3):
        sys("color 67")
        #print('\a'+"Plug desconectado")
        #tone(4000,400)
        #alerta(nota="do")
        print('\t'+"Plug desconectado")
        PlaySound(baixo[0],0)
        avisos+=1
      elif (battery.power_plugged and avisos>=3):
        avisos = 0
        #tone(1100,200);tone(1100,300)
        #alerta(nota="do")
        #print("\a Carregando...")
        print("\tCarregando...")
        PlaySound(cima,0)
        sys("color 2F")
      elif (battery.percent > 50 and battery.power_plugged):
        sys("color 0F")
      print(end="\r")
      sleep(5)

if __name__ == "__main__":
    main()
