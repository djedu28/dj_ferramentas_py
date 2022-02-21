# @DjEdu28 - Licença MIT - Copyright (c) 2022 @DjEdu28 (Luis Eduardo Silva dos Santos) 
"""
Criado por @DjEdu28 EM: 01/2022
Monitor da bateria
versão 0.1 - beta

Objetivo da ferramenta:
    Observar a porcentagem da bateria e informar se tá descarregando ou carregando
    Ainda aletar caso chegue em um nivel critico de carga
    
implementado:
    * Ler dados da bateria
    * Informar por som mudança de estado
"""
import psutil
from time import sleep

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

def main():
    avisos = 0
    print("\n"*3)
    while True:
      battery = psutil.sensors_battery()
      print("    Porcentagem:", battery.percent,end=" ")
      print("Carregando:", battery.power_plugged," "*10,end=" ")
      if battery.percent < 50 and battery.power_plugged == False:
        print('\a'+"Bateria baixa",sep="")
        
      elif (battery.power_plugged == False and avisos<3):
        print('\a'+"Plug desconectado")
        avisos+=1
      elif (battery.power_plugged and avisos>=3):
        avisos = 0
        #print("\a Carregando...")
        print('\a'+"\tCarregando...")
      
      print(end="\r")
      sleep(5)

if __name__ == "__main__":
    main()
