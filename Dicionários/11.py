import math
def soma(x1, x2):
    return x1 + x2

def subtracao(x1, x2):
    return x1 - x2

def multiplicacao(x1, x2, x3, x4):
    return x1 * x2 - x3 * x4

def modulo(numero):
    return abs(numero)

numeros_complexos = []

z_real = float(input())
z_imag = float(input())
w_real = float(input())
w_imag = float(input())

z = abs(math.sqrt(z_real**2 + z_imag**2))
w = abs(math.sqrt(w_real**2 + w_imag**2))

numeros = {'real':soma(z_real, w_real),'imaginario':soma(z_imag, w_imag)}
numeros_complexos.append(numeros)
numeros = {'real':subtracao(z_real, w_real),'imaginario':subtracao(z_imag, w_imag)}
numeros_complexos.append(numeros)
numeros = {'real':multiplicacao(z_real, w_real, z_imag, w_imag),'imaginario':multiplicacao(z_real, w_imag, -w_real, z_imag)}
numeros_complexos.append(numeros)

for _ in numeros_complexos:
    print(_)
    
print(f"{z:.2f}")
print(f"{w:.2f}")