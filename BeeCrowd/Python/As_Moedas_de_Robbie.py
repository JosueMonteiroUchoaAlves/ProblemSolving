# https://judge.beecrowd.com/pt/problems/view/2709

def pegarMoedas(n):
    listaMoedas = [int(input()) for _ in range(n)]
    return listaMoedas

while True:
    try:
        numeroDeMoedas = int(input())        
        moedas = pegarMoedas(numeroDeMoedas)
        salto = -int(input())
        total=0
        for index in range(len(moedas)-1, -1, salto):
            total+=moedas[index] 
        #print(total)
        
        if total == 2:
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        elif total % 2 == 0:
            print("Bad boy! I’ll hit you.")
        elif total == 1:
            print("Bad boy! I’ll hit you.")
        else:
            primoMaximo = total//2+1
            for num in range(3, primoMaximo):
                if total % num == 0:
                    print("Bad boy! I’ll hit you.")
                    break
            else:
                print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
    except Exception: # EOFError
        break
