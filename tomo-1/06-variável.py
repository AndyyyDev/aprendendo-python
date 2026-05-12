nome = "Huayyra"
print(nome)

nome = "Porsche"
print("Bem vindo a loja", nome)

nome = "Huayyra"
print("Bem vindo a loja", nome)
print(nome, "hoje é seu primeiro dia")

nome = "Um"
print(nome)
nome = "Dois"
print(nome)
nome = "Três"
print(nome)

# Apenas demonstrando que as variáveis podem ser reatribuídas e que o valor anterior é perdido.

hp_incicial = 100
hp_atual = hp_incicial
print(hp_atual)

# Estou reusando o valor para criar outras variáveis.

nome_do_personagem = "Huayyra"
hp_atual = 99
nivel_do_personagem = 57
ultimo_ponto_de_salvamento = "Bonfire"

# Demonstrando que python prefere aceitar snake_case.

# Compare = Lembrar de sempre investir em nomes bons!!!. <<<

# Ruim

x = 9000
y = x * 1.5

# Bom

hp_máximo = 9000
hp_com_buff = hp_máximo * 1.5

hp, mp, tp = 9000, 500, 300
print(hp, mp, tp)

classe = "Guerreiro"
classe_anterior = classe

classe = "Mago"

print(classe)
print(classe_anterior)