from node import Node

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if not node:
            return Node(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            
            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value  
            node.right = self._delete(node.right, temp.key)

        
        if not node:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, node):
        result = []
        if node:
            result.extend(self._in_order(node.left))
            result.append(node.key)
            result.extend(self._in_order(node.right))
        return result

    def pre_order(self):
        return self._pre_order(self.root)

    def _pre_order(self, node):
        if not node:
            return []
        return [(node.key, node.value)] + self._pre_order(node.left) + self._pre_order(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_min_value_node(self, node):
        
        current = node
        while current.left is not None:
            current = current.left
        return current
    def get_max_value_node(self, node):
        
        current = node
        while current.right is not None:
            current = current.right
        return current


