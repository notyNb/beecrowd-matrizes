def soma(linhaUsada: int, m: list):
    print(m)
    resultado = 0.0
    for i in range(12):
        print(m[linhaUsada][i])
        resultado += m[linhaUsada][i]
    print(f"{resultado:.1f}")

def media(m: list, linhaUsada: int):
    resultado = 0
    for i in range(len(m[linhaUsada])):
        resultado += m[linhaUsada][i]
        media_final = resultado // (len(m[linhaUsada]))
    print(f"{media_final:.1f}")




def main():
    m = []
    a = 12
    b = 12
    for i in range(a):
        linha = [0] * b
        m.append(linha)
        
    linhaUsada = int(input())
    somaMedia = input()
    for i in range(12):
        for j in range(12):
            valores = float(input())
            m[i][j] = valores

       
    if somaMedia == "S":
        soma(linhaUsada, m)
    elif somaMedia =="M":
        media(m, linhaUsada)

        
main()
