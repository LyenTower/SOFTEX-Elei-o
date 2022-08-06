import enum
class Candidatos(enum.Enum):
    candidato_a = 889
    candidato_b = 847
    candidato_c = 515
    branco = 0
candidatos = {"candidato A":0, "candidato B":0, "candidato C": 0, "branco": 0 , "nulo": 0}

votação = True
while votação:
    print("Qual candidato você gostaria de votar?")
    try:
        voto = int(input())
        if voto == Candidatos.candidato_a.value:
            candidatos["candidato A"] += 1
        elif voto == Candidatos.candidato_b.value:
            candidatos["candidato B"]+= 1
        elif voto == Candidatos.candidato_c.value:
            candidatos["candidato C"]+= 1
        elif voto == Candidatos.branco.value:
            candidatos["branco"]+= 1
        else:
            candidatos["nulo"]+= 1
        escolha = input("Você gostaria de ver a situação da eleição?")
        if escolha == 'sim':
            votação = False
    except:
        print("Você não digitou nenhuma das opções, vote novamente.")
print(f"O candidato eleito foi: {max(candidatos, key=candidatos.get)}")
print("Votos para candidato A: {}".format(candidatos["candidato A"]))
print("Votos para candidato B: {} ".format(candidatos["candidato B"]))
print("Votos para candidato C: {} ".format(candidatos["candidato C"]))
print("Votos para branco: {} ".format(candidatos["branco"]))
print("Votos para nulo: {} ".format(candidatos["nulo"]))