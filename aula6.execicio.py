# 1. Implemente uma função recursiva que calcule a potência de um número (base^expoente).
def exp_rec(b, e):
    if e == 0:
      return 1
    return b * exp_rec(b, e-1)

resultado = exp_rec(10, 2)
print(resultado)

# 2. Crie uma função recursiva para calcular o n-ésimo termo da sequência de
# Fibonacci.Lembre-se de que a sequência começa com 0 e 1.
def seq_fibo(n):
    if n <= 1:
        return n
    return seq_fibo(n-1) + seq_fibo(n-2)

resultado = seq_fibo(10)
print(resultado)

# 3. Escreva uma função recursiva que conte quantos dígitos um número tem.
def quan_dig(n):
    if n == 0:
        return 0
    return 1 + quan_dig( n//10 )

resultado = quan_dig(585850)
print(resultado)    

# 4. Escreva uma função recursiva que verifique se uma string é um palíndromo.  
