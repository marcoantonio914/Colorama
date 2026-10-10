#Uso da biblioteca Colorama
from colorama import Fore, Style
#Uso da biblioteca random para simular o nível
import random

#Cria a função simular
def simular(nivel):
    simular = "nivel"
#Define uma correspondencia para cada nível
    if nivel == 1:
        simular = Fore.RED+"Nível 1: Muito baixo (crítico)"
    elif nivel == 2:
        simular = Fore.YELLOW+"Nível 2: Baixo"
    elif nivel == 3:
        simular = Fore.GREEN+"Nível 3: Médio"
    elif nivel == 4:
        simular = Fore.CYAN+"Nível 4: Alto"
    elif nivel == 5:
        simular = Fore.BLUE+"Nível 5: Muito alto (alerta)"
    else:
        simular = "Nível inválido"

#Limpa a cor utilizada pelo colorama    
    return simular + Style.RESET_ALL

#Sorteia um número entre 1 e 5
nivel = random.randint(1, 5)
#Chama a função simular passando o nível sorteado como argumento
simulacao = simular(nivel)
#Exibe o resultado da simulação
print(simulacao)