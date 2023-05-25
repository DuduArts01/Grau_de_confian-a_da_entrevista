# N (população de alunos na escola)
# n (Tamanho da amostra, quantidade de pessoas entrevistadas)
# n0 (Tamanho inicial da amostra com erro incluso)
# γ (Grau de confiança)
# α (Probabilidade de erro esperado)

N = int(input("População da escola: "))
# Total de alunos da escola

n = int(input("Quantidade de pessoas entrevistadas: "))

n0 = (N * n) / (N - n)
#formula inicial --> n = (N * n0) / (N + n0)



α	 = 1/ n0
#formula inicial --> n0 = 1 / α



γ	= 1 - α

#formula inicial α = 1 - γ

print("---------------------------")
print(f"\nGrau de confiança é {γ}\n")
print("---------------------------")
