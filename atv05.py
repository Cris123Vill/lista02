livros = [
    [1, "Dom Casmurro", "Machado de Assis", 1899],
    [2, "1984", "George Orwell", 1949],
    [3, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943],
]

# O primeiro livro está na linha 0 e o ano de lançamento está na coluna 3
print("Antes da atualização:", livros[0])
livros[0][3] = 2024

print("Depois da atualização:", livros[0])
