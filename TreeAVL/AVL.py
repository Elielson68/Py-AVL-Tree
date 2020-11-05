def _formatting_spaces_before_the_value(space):
    space += " "
    return space


def _space_between_format(count_old_space):
    if count_old_space == 2:
        spaces_to_add = count_old_space + 4
    else:
        spaces_to_add = count_old_space + count_old_space + 2
    space = " " * spaces_to_add
    return spaces_to_add, space


def _formatting_bar_spaces_below_a_value(value):
    space_insert = len(str(value)) + 2
    space_between_bar = " " * space_insert
    return space_between_bar


def _height_tree(value):
    value *= 2
    return value


def isLeftSon(f, s):
    if s < f:
        return True
    return False


def isRightSon(f, s):
    if s > f:
        return True
    return False


def whoFather(tree, son):
    for father in tree:
        if son in tree[father]:
            return father
    return None


def isSheet(tree, father):
    if len(tree[father]) == 0:
        return True
    return False


def FilterRowTree(tree, rows, filhos=None):
    if filhos is None:
        filhos = []
    lista = []
    novos_filhos = []
    for filho in filhos:
        if filho is not None:
            filho = int(filho)
            if haveSon(tree[filho]):
                new_list = []
                for x in tree[filho]:
                    if type(x) == int:
                        if isLeftSon(filho, x):
                            new_list.append(x)
                        else:
                            new_list.append(x)
                    else:
                        new_list.append(x)
                lista += new_list
            if limitSon(tree[filho]):
                novos_filhos.append(tree[filho][0])
                novos_filhos.append(tree[filho][1])
            elif haveSon(tree[filho]):
                novos_filhos.append(tree[filho][0])
        else:
            novos_filhos.append(None)
    if filhos == [] or len(filhos) == filhos.count(None):
        return rows
    else:
        if len(novos_filhos) != novos_filhos.count(None):
            rows.append(novos_filhos)
        FilterRowTree(tree, rows, novos_filhos)


def FilterRowTreeWithDeadSon(tree, rows, filhos=None):
    if filhos is None:
        filhos = []
    lista = []
    novos_filhos = []
    for filho in filhos:
        if filho is not None and filho != "dead":
            filho = int(filho)
            if haveSon(tree[filho]):
                new_list = []
                for x in tree[filho]:
                    if type(x) == int:
                        if isLeftSon(filho, x):
                            new_list.append(str(x))
                        else:
                            new_list.append(str(x))
                    else:
                        new_list.append(x)
                lista += new_list
            if limitSon(tree[filho]):
                novos_filhos.append(str(tree[filho][0]))
                novos_filhos.append(str(tree[filho][1]))
            elif haveSon(tree[filho]):
                novos_filhos.append(str(tree[filho][0]))
        elif filho == "dead":
            new_list = ["dead", "dead"]
            novos_filhos += new_list
    if filhos == [] or len(filhos) == filhos.count("dead"):
        return rows
    else:
        if len(novos_filhos) != novos_filhos.count("dead"):
            rows.append(novos_filhos)
        FilterRowTreeWithDeadSon(tree, rows, novos_filhos)


def limitSon(tree):
    if len(tree) == 2:
        return True
    return False


def haveSon(cls):
    if len(cls) > 0:
        return True
    return False


def isUniqueSon(tree):
    if len(tree) == 1:
        return True
    return False


def string_size_compensation(string, side):
    if len(string.strip()) == 1 and side == 0:
        return string + " "
    elif len(string.strip()) == 1 and side == 1:
        return " " + string
    else:
        return string


class AVL:
    """

    This class create dict tree's and balance using AVL algorithm.

    In ::parameter:: tree: Parse a list of nodes, like a: [10, 58, 65, 15]

    and to print the binary tree just call your object in the print

    tree = AVL([10, 58, 65, 15])
    print(tree)

    To insert new Nodes in the tree, just call method insertNode(your_node)

    the nodes have be a integer number.

    """
    def __init__(self, tree: list):
        self.tree = tree
        self.length_tree = len(tree)
        self.dict_tree = {}
        self.dict_tree_with_dead_sheets = {}
        self.dict_balance = {}
        self.generateDictTree(0)
        self.generateCountDictBalance()

    def __repr__(self):
        return self.ShowBinaryTree()

    def insertNode(self, node):
        self.tree.append(node)
        self.generateDictTree(0)
        self.generateCountDictBalance()

    def _insertSon(self, fat, s):
        if limitSon(self.dict_tree[fat]):
            left_s = self.dict_tree[fat][0]
            if isLeftSon(fat, s):
                self._insertSon(left_s, s)
            right_s = self.dict_tree[fat][1]
            if isRightSon(fat, s):
                self._insertSon(right_s, s)
        elif haveSon(self.dict_tree[fat]):
            if isLeftSon(fat, s):
                if isLeftSon(fat, self.dict_tree[fat][0]):
                    self._insertSon(self.dict_tree[fat][0], s)
                else:
                    self.dict_tree[fat].insert(0, s)
            if isRightSon(fat, s):
                if isRightSon(fat, self.dict_tree[fat][0]):
                    self._insertSon(self.dict_tree[fat][0], s)
                else:
                    self.dict_tree[fat].append(s)
        else:
            self.dict_tree[fat].append(s)

    def generateTreeWithDeadSheets(self):
        nodes = list(self.dict_tree.keys())
        for sheet in nodes:
            if limitSon(self.dict_tree[sheet]):
                self.dict_tree_with_dead_sheets[sheet] = [self.dict_tree[sheet][0], self.dict_tree[sheet][1]]
            elif haveSon(self.dict_tree[sheet]):
                self.dict_tree_with_dead_sheets[sheet] = [self.dict_tree[sheet][0]]
                if isLeftSon(sheet, self.dict_tree[sheet][0]):
                    self.dict_tree_with_dead_sheets[sheet].append("dead")
                else:
                    self.dict_tree_with_dead_sheets[sheet].insert(0, "dead")
            else:
                self.dict_tree_with_dead_sheets[sheet] = []
                self.dict_tree_with_dead_sheets[sheet].append("dead")
                self.dict_tree_with_dead_sheets[sheet].append("dead")

    def ShowBinaryTree(self):
        # Inserção dos espaços abaixo.
        first_value = self.tree[0]
        first_value_space = "{}".format(first_value)
        self.generateTreeWithDeadSheets()
        RowsWithDeadSons = [[first_value_space]]
        FilterRowTreeWithDeadSon(self.dict_tree_with_dead_sheets, RowsWithDeadSons, [first_value])
        RowsWithDeadSons.reverse()
        arv_draw = ""
        space_before = ""
        count_space_between_brothers = 2
        space_between_brothers = " " * count_space_between_brothers
        count_space_between_primos = 2
        space_between_primos = " " * count_space_between_primos

        count_height_tree_max = 2
        count_height_tree_min = 0

        for i, row in enumerate(RowsWithDeadSons):
            sequence_values = ""
            for ii, son in enumerate(row):
                if son != "dead":
                    father = whoFather(self.dict_tree, int(son))
                    father = father if father is not None else int(son)
                    if isUniqueSon(self.dict_tree[father]):
                        if 1 < len(RowsWithDeadSons[i][ii]) < 3 and first_value != int(son) and ii != 0:
                            RowsWithDeadSons[i][ii] = " " + RowsWithDeadSons[i][ii]

                if ii == 0 and son != "dead":
                    node_with_space = string_size_compensation(RowsWithDeadSons[i][ii], 0)
                    sequence_values += space_before + node_with_space

                elif ii == 0 and son == "dead":
                    sequence_values += space_before + " "

                elif i == 0 and ii == 0 and ii % 2 == 0 and son != "dead":
                    node_with_space = string_size_compensation(RowsWithDeadSons[i][ii], 0)
                    sequence_values += space_between_brothers + node_with_space

                elif i == 0 and ii == 0 and ii % 2 == 0 and son == "dead":
                    sequence_values += space_between_brothers + " "

                elif i == 0 and ii == 0 and ii % 2 == 1 and son != "dead":
                    node_with_space = string_size_compensation(RowsWithDeadSons[i][ii], 1)
                    sequence_values += space_between_primos + node_with_space

                elif i == 0 and ii == 0 and ii % 2 == 1 and son == "dead":
                    sequence_values += " " + space_between_primos

                elif ii != 0 and son != "dead":
                    node_with_space = (string_size_compensation(RowsWithDeadSons[i][ii], 0) if ii % 2 == 0 else
                                       string_size_compensation(RowsWithDeadSons[i][ii], 1))
                    sequence_values += space_between_primos + node_with_space

                elif ii != 0 and son == "dead":
                    sequence_values += space_between_primos + "  "

            arv_draw = sequence_values + arv_draw
            arv_draw = "\n" + arv_draw

            # INSERÇÃO DAS BARRAS ABAIXO
            space_between_bar = space_between_brothers
            draw_bar = []
            space_bar = ""
            space_before_bar = " " * (count_height_tree_min + 1)
            count_space_between_two_bars = count_space_between_primos
            space_between_two_bars = " " * (count_space_between_two_bars + 2)

            """
                O MOTIVO DAS LINHAS DESALINHAREM AS VEZES É POR TER VALORES COM 1 DIGITO E COM 2 NA MESMA LINHA.
                VERIFICAR COMO ALTERAR ISSO PARA QUE FIQUE PERFEITO.
            
            """
            for count in range(0, count_height_tree_max):
                for ii, son in enumerate(row):
                    if son != "dead":
                        son = int(son)
                        father = whoFather(self.dict_tree, son)
                        father = father if father is not None else son
                        if father:
                            if haveSon(self.dict_tree[father]):
                                space_before_bar_aux = space_before_bar if ii == 0 else space_between_two_bars
                                if isLeftSon(father, son):
                                    space_bar += "{}/".format(space_before_bar_aux)
                                elif isRightSon(father, son):
                                    if ii == 0:
                                        space_bar += "{}\\{}".format(space_between_bar, space_between_two_bars)
                                    else:
                                        space_bar += "{}\\".format(space_between_bar)
                    else:
                        if ii == 0:
                            space_bar += "{} ".format(space_before_bar)
                        elif ii % 2 == 0:
                            space_bar += "{} ".format(space_between_two_bars)
                        else:
                            space_bar += " {}".format(space_between_bar)

                count_space_between_two_bars += 2
                space_between_two_bars = " " * (count_space_between_two_bars + 2)
                space_bar = "\n" + space_bar
                if "/" in space_bar or "\\" in space_bar:
                    draw_bar.append(space_bar)
                else:
                    draw_bar = []
                space_bar = ""
                space_between_bar = space_between_bar.replace(" ", "", 2)
                space_before_bar += " "

            for spaces in draw_bar:
                arv_draw = spaces + arv_draw
            space_before = " " * (count_height_tree_max + count_height_tree_min)
            count_height_tree_min = count_height_tree_max + count_height_tree_min
            count_height_tree_max = _height_tree(count_height_tree_max)
            (count_space_between_brothers, space_between_brothers) = _space_between_format(count_space_between_primos)
            count_space_between_primos = count_space_between_brothers
            space_between_primos = space_between_brothers
        arv_draw = arv_draw.replace("\n", "", 1)
        file = open("arvore.txt", "w")
        file.write(arv_draw)
        file.close()
        return arv_draw

    def getDictTree(self):
        return self.dict_tree

    def generateDictTree(self, index_father):
        self.dict_tree = {}
        for i, son in enumerate(self.tree):
            self.dict_tree[son] = []
            self._generateDictBalance(son)
        for son in self.tree:
            if self.tree[index_father] != son:
                self._insertSon(self.tree[index_father], son)

    def _generateDictBalance(self, node):
        self.dict_balance[node] = {"left": 0, "right": 0}

    def getListSheet(self):
        return [x for x in self.dict_tree if self.dict_tree[x] == []]

    def BalanceCount(self, balance, node, direction):
        if limitSon(self.dict_tree[node]):
            self.dict_balance[balance][direction] += 1
            self.BalanceCount(balance, self.dict_tree[node][0], direction)
            self.BalanceCount(balance, self.dict_tree[node][1], direction)
        elif haveSon(self.dict_tree[node]):
            self.dict_balance[balance][direction] += 1
            if isLeftSon(node, self.dict_tree[node][0]):
                self.BalanceCount(balance, self.dict_tree[node][0], direction)
            if isRightSon(node, self.dict_tree[node][0]):
                self.BalanceCount(balance, self.dict_tree[node][0], direction)

    def BalanceTree(self):
        aux_tree = [x for x in self.tree]
        aux_tree_reverse = [x for x in aux_tree]
        aux_tree_reverse.reverse()
        for node in aux_tree_reverse:
            if self.dict_balance[node]["fb"] > 1:
                index_node_desb = aux_tree_reverse.index(node)
                index_son_desb = aux_tree_reverse.index(self.dict_tree[node][0])
                value_desb = aux_tree_reverse[index_node_desb]
                value_son_desb = aux_tree_reverse[index_son_desb]
                if self.dict_balance[value_son_desb]["fb"] < 0:
                    index_son_of_son_desb = aux_tree_reverse.index(self.dict_tree[value_son_desb][0])
                    son_of_son_desb = aux_tree_reverse[index_son_of_son_desb]
                    aux_tree_reverse[index_node_desb] = son_of_son_desb
                    aux_tree_reverse[index_son_desb] = value_desb
                    aux_tree_reverse[index_son_of_son_desb] = value_son_desb
                    break
                else:
                    aux_tree_reverse[index_node_desb] = value_son_desb
                    aux_tree_reverse[index_son_desb] = value_desb
                    break
            if self.dict_balance[node]["fb"] < -1:
                index_node_desb = aux_tree_reverse.index(node)
                index_son_desb = aux_tree_reverse.index(self.dict_tree[node][0])
                value_desb = aux_tree_reverse[index_node_desb]
                value_son_desb = aux_tree_reverse[index_son_desb]
                if self.dict_balance[value_son_desb]["fb"] > 0:
                    index_son_of_son_desb = aux_tree_reverse.index(self.dict_tree[value_son_desb][0])
                    son_of_son_desb = aux_tree_reverse[index_son_of_son_desb]
                    aux_tree_reverse[index_node_desb] = son_of_son_desb
                    aux_tree_reverse[index_son_desb] = value_desb
                    aux_tree_reverse[index_son_of_son_desb] = value_son_desb
                    break
                else:
                    aux_tree_reverse[index_node_desb] = value_son_desb
                    aux_tree_reverse[index_son_desb] = value_desb
                    break
        aux_tree_reverse.reverse()
        self.tree = aux_tree_reverse
        self.generateDictTree(0)
        self.generateCountDictBalance()
        balance_values = [x['fb'] for x in list(self.dict_balance.values())]
        list_desb_values = []
        for x in balance_values:
            if x > 1:
                list_desb_values.append(x)
            if x < -1:
                list_desb_values.append(x)
        if len(list_desb_values) > 0:
            self.BalanceTree()

    def generateCountDictBalance(self):
        for node in self.dict_tree:
            if limitSon(self.dict_tree[node]):
                self.dict_balance[node]["left"] += 1
                self.dict_balance[node]["right"] += 1
                self.BalanceCount(node, self.dict_tree[node][0], "left")
                self.BalanceCount(node, self.dict_tree[node][1], "right")
            elif haveSon(self.dict_tree[node]):
                if isLeftSon(node, self.dict_tree[node][0]):
                    self.dict_balance[node]["left"] += 1
                    self.BalanceCount(node, self.dict_tree[node][0], "left")
                else:
                    self.dict_balance[node]["right"] += 1
                    self.BalanceCount(node, self.dict_tree[node][0], "right")
        for node in self.dict_balance:
            self.dict_balance[node]["fb"] = self.dict_balance[node]["left"] - self.dict_balance[node]["right"]
