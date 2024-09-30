import requests
import json


try:
    print("Escolha um Filme para a busca !")
    nomeFilme = str(input("Nome do filme: "))
    re = requests.get("http://www.omdbapi.com/?t="+ nomeFilme + "&apikey=f2d24bac")
    dic_re = re.json()
except:
    print("Por favor, digite um nome válido...")

print("Busca realizada com sucesso... ")
print(dic_re)


res = str(input("\nDeseja salvar essas informações em um novo arquivo de texto? "))
if res.upper() == "SIM":
    print("Dados serão salvos")


    def salva_arquivo(nomeFilme):

        try:
            arquivo = open(nomeFilme + ".txt", "w")
            json.dump(dic_re, arquivo, indent=4)
            print("Arquivo editado com sucesso")
        except:
            print("Falha na criação do arquivo...")

    salva_arquivo(nomeFilme)
else:
    print("Ok, programa sendo finalizado...")






