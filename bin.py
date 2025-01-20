from avl import AVLTree
from node import Node
class Bin:
    def __init__(self, bin_id, capacity):
        self.binid=bin_id
        self.cap=capacity
        self.tree=AVLTree()
        pass

    def add_obj(self, object):
        # Implement logic to add an object to this bin
        self.tree.insert(object.obid,object)
        self.cap-=object.size
        #add bin_id to object later on
        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        node=self.tree.search(object_id)
        self.cap+=node.value.size
        self.tree.delete(node.key)