from TreeAVL.AVL import AVL

while True:
    user = input("Digite os valores para adicionar na árvore:\nExemplo de input: 2,5,6,8\nPara sair digite: 0,0,0\nValores: ").split(",")
    list_nodes = [int(x.strip()) for x in user]
    if list_nodes.count(0) == 3:
        break
    arvore = AVL(list_nodes)
    arvore.generateDictTree(0)
    arvore.generateCountDictBalance()
    while True:
        user = input("\n1 - Imprimir árvore binária\n2 - Balancear árvore\n3 - Inserir novo vértice\n4 - Sair\nOpcao: ")
        if user == "1":
            print(arvore.ShowBinaryTree())
        elif user == "2":
            arvore.BalanceTree()
        elif user == "3":
            new_node = int(input("Valor do novo vértice: "))
            arvore.insertNode(new_node)
            arvore.generateDictTree(0)
            arvore.generateCountDictBalance()
        elif user == "4":
            break
        else:
            print("Comando inválido.")