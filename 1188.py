def soma(m: list):
    resultado = 0.0
    p = 6
    k = 6
    for i in range(7, 12):
        p -= 1
        k += 1
        for j in range(p, k):
            resultado += m[i][j]
            
    print(f"{resultado:.1f}")

def media(m: list):
    resultado = 0
    p = 6
    k = 6
    for i in range(7, 12):
        p -= 1
        k += 1
        for j in range(p, k):
            resultado += m[i][j]
    media_final = resultado / (30)
    print(f"{media_final:.1f}")




def main():
    m = []
    a = 12
    b = 12
    for i in range(a):
        linha = [0] * b
        m.append(linha)
        
    somaMedia = input()
    for i in range(12):
        for j in range(12):
            valores = float(input())
            m[i][j] = valores

       
    if somaMedia == "S":
        soma(m)
    elif somaMedia =="M":
        media(m)

        
main()
