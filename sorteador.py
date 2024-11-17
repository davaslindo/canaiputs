import random

def sorteador_de_um_nome(nomes):
    if not nomes:
        return "A lista de nomes está vazia!"
    return random.choice(nomes)

# Lista de nomes para o sorteio
nomes = ["Daich do 1°", "Daniel chato", "Bea linda", "Vini inspiração", "Bagi", "Carinha", "Joao Victor 1ano", "PH", "Brenda", "Miotto", "Lucca", "LuisinhoFotocopia", "Stalberg Mulher", "Stalberg", "Raimona", "Davi", "Mateus Beiço", "Mirella", "Artur", "RaphaCoss"]

# Realiza o sorteio de um único nome
nome_sorteado = sorteador_de_um_nome(nomes)
print("*SORTEIA O PAU NA MINHA CARA*")
print(f"O nome sorteado é: {nome_sorteado}")