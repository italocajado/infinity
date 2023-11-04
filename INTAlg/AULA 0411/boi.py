boiPesado = 2000
boiMagro = 0

for i in range(1, 10):
    id = int(input("Digite a Id do boi: "))
    peso = float(input("Digite o peso do boi: "))
    if peso < boiPesado:
        boiPesado = peso
        idGordo = id
    if peso > boiMagro:
        boiMagro = peso
        idMagro = id

print("Boi mais magro: ", boiMagro, " Kgs", "ID: ", idMagro)
print("Boi mais pesado: ", boiPesado, " Kgs", "ID: ", idGordo) 