# etapa 1 - Crie uma lista com os nomes de 5 objetos.
objetos = ["perfume", "pulseira", "anel", "hidratante", "esmalte"]
print("Lista de objetos criadas!")

# etapa 2 - Adicione mais um objeto ao final da lista.
objetos.append("gloss")
print("Objeto adicionado com sucesso!")

# etapa 3 - Acesse o objeto que está na segunda posição.
segundo_objeto = objetos[1]
print(f"Objeto 2 acessado: {segundo_objeto}")

# etapa 4 - Remova um objeto da lista.
objetos.remove("hidratante")
print("Objeto removido!")

# etapa 5 - Exiba o tamanho da lista.
len(objetos)
print(len(objetos))

# etapa 6 - Mostre todos os itens com um laço for.
for objeto in objetos:
    print(objeto)

# etapa 7 - Verifique se 'cadeira' está na lista. Se sim remova-a, senão adicione.
if "cadeira" in objetos:
    objetos.remove("cadeira")
    print("Cadeira removida!")
else:
    objetos.append("cadeira")
    print("Cadeira adicionada!")

# etapa 8 - Ordene a lista em ordem alfabética.
objetos.sort()
print(objetos)

#etapa 9 - Exiba o primeiro e o último objeto.
primeiro_objeto = objetos[0]
print(primeiro_objeto)
ultimo_objeto = objetos[5]
print(ultimo_objeto)

#etapa 10 - Limpe toda a lista
objetos.clear()
print(objetos)