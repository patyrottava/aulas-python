nome = "Guilherme"
idade = 24
profissao = "Programador"
linguagem = "Python"

dados= (nome: "Guilherme" , idade: 28)

print("nome: %s idade: %d" % (nome, idade))
print("nome: {0} idade: {1}" .format(nome, idade))
print("nome: {} idade: {}" .format(nome, idade))
print("nome: {0} idade: {1} idade: {1}" .format(nome, idade))
print("nome: {nome} idade: {age} " .format(name=nome, age=idade))
print("nome: {nome} idade: {idade}".format{**dados})

print(f"nome: {nome} idade: {idade}")