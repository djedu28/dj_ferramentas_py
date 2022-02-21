# @DjEdu28 - Licença MIT - Copyright (c) 2022 @DjEdu28 (Luis Eduardo Silva dos Santos) 
"""
Criado por @DjEdu28 EM: 01/2022
Atualizado em: 01/2022
Monitor da bateria
versão 2.0

Objetivo da ferramenta:
    Observar a porcentagem da bateria e informar se tá descarregando ou carregando
    Ainda aletar caso chegue em um nivel critico de carga
    
novidades:
    * Diferenciando notificação pelo som
    
já implementado:
    * Ler dados da bateria
    * Informar por som mudança de estado
    * colorindo a tela
Ps.:
    Tentativa de diferenciar as notificações usando notas/tons diferentes
"""
import psutil
from time import sleep
from os import system as sys

# def secs2hours(secs):
    # mm, ss = divmod(secs, 60)
    # hh, mm = divmod(mm, 60)
    # return "%d:%02d:%02d" % (hh, mm, ss)
notas = {
    "do" : 261,
    "re" : 293,             
    "mi" : 329,      
    "fa" : 349,    
    "sol": 392,  
    "la" : 0,
    "si" : 0,          
} 
def tone(freq,duration):
    from winsound import Beep
    # duration = 1000  # milliseconds
    if freq in notas: freq = notas[freq]
    
    Beep(freq, duration)

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
        [tone(3300,200*n) for n in range(1,4)]
        print("Bateria baixa",sep="")
        
      elif (battery.power_plugged == False and avisos<3):
        sys("color 67")
        #print('\a'+"Plug desconectado")
        tone(4000,400)
        print('\t'+"Plug desconectado")
        avisos+=1
      elif (battery.power_plugged and avisos>=3):
        avisos = 0
        tone(1100,200);tone(1100,300)
        #print("\a Carregando...")
        print("\tCarregando...")
        sys("color 2F")
      elif (battery.percent > 50 and battery.power_plugged):
        sys("color 0F")
      print(end="\r")
      sleep(5)

if __name__ == "__main__":
    main()
