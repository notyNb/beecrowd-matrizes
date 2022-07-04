def soma(colunaUsada: int, m: list):
    resultado = 0.0
    for i in range(12):
        resultado += m[i][colunaUsada]
    print(f"{resultado:.1f}")

def media(m: list, colunaUsada: int):
    resultado = 0
    for i in range(12):
        resultado += m[i][colunaUsada]
        media_final = resultado / (12)
    print(f"{media_final:.1f}")




def main():
    m = []
    a = 12
    b = 12
    for i in range(a):
        linha = [0] * b
        m.append(linha)
        
    colunaUsada = int(input())
    somaMedia = input()
    for i in range(12):
        for j in range(12):
            valores = float(input())
            m[i][j] = valores

       
    if somaMedia == "S":
        soma(colunaUsada, m)
    elif somaMedia =="M":
        media(m, colunaUsada)

        
main()
