#Uso da biblioteca Colorama para diferenciar as cores
from colorama import Fore, Style
#Uso da biblioteca random para a simulação do nível
import random

#Optei pelo uso do objeto dict para associar os niveis
#do reservatorio com a situacao e a cor correspondente.

#Lista com níveis do reservatório
niveis = ["Nível 1", "Nível 2", "Nível 3", "Nível 4", "Nível 5"]

#Lista com a situação do reservatório e a cor correspondente
situacao = [
    Fore.RED+"Muito baixo (crítico)",
    Fore.YELLOW+"Baixo",
    Fore.GREEN+"Médio",
    Fore.CYAN+"Alto",
    Fore.BLUE+"Muito alto (alerta)"]

#Criação do dicionário classificacao associando
#os niveis com a situacao
classificacao = dict(zip(niveis, situacao))

#Simulação do nível do reservatório com a função random
simulacao = random.choice(niveis)

#Exibe o nível sorteado em simulacao,
#procura no dicionario classificacao a situaçlão do nível sorteado
#Limpa a cor utilizada pelo colorama
print (f"{simulacao}:{classificacao[simulacao]}{Style.RESET_ALL}")


