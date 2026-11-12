funcionarios = []

funcionarios.append([1, "Carlos", "Analista", 3500.00])
funcionarios.append([2, "Mariana", "Desenvolvedora", 4800.00])

for indice, funcionario in enumerate(funcionarios):
    if funcionario[0] == 2:
        funcionarios[indice][3] += 500
        print(f"Salário atualizado! Novo salário de {funcionario[1]}: R$ {funcionarios[indice][3]:.2f}")
        break
else:
    print("Funcionário não encontrado")
