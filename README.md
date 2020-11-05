# Py-AVL-Tree
A python package to make a Tree's like a Binary Tree and Balanced AVL Tree.

# How to install?

Use:

```
pip install Py-AVL-Tree
```


# How to use?

First, import the AVL class.

```python
from TreeAVL.AVL import AVL
```

Now, you have to parse a list with nodes to create a object tree.

```python
from TreeAVL.AVL import AVL

tree = AVL([10, 5, 15, 7, 18, 9])
```

To show your binary tree, just parse your new object tree to print.

```python
from TreeAVL.AVL import AVL

tree = AVL([10, 5, 15, 7, 18, 9])
print(tree)
```

If you have to balance your tree, just call the method BalanceTree()

```python
from TreeAVL.AVL import AVL

tree = AVL([10, 5, 15, 7, 18, 9])
print(tree)
tree.BalanceTree()
print(tree)
```