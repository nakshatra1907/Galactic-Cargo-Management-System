from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node
class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.tree_caps=AVLTree()
        self.tree_obj=AVLTree()
        self.tree_binids=AVLTree()
    
        pass 

    def add_bin(self, bin_id, capacity):
        bino=Bin(bin_id,capacity)
        self.tree_binids.insert(bin_id,bino)
        walk=self.tree_caps.search(capacity)
        if walk is not None:
            walk.value.insert(bin_id,bino)
        else:
            tree=AVLTree()
            tree.insert(bin_id,bino)
            self.tree_caps.insert(capacity,tree)
        pass

    def add_object(self, object_id, size, color):
        ob=Object(object_id,size,color)
        col=int(color.value)
        if col==1:
            xx=None
            x=self.tree_caps.root
            while x!=None:
                if x.key>=size:
                    xx=x
                    x=x.left
                else:
                    x=x.right
            if xx==None:
                raise NoBinFoundException
            else:
                tr=xx.value
                ni=tr.get_min_value_node(tr.root)
                ni.value.add_obj(ob)
                na=ni.value.cap
                ob.bin=ni.value
                tr.delete(ni.key)
                if tr.root==None:
                    self.tree_caps.delete(xx.key)
                tre=self.tree_caps.search(na)
                if tre is not None:
                    tre.value.insert(ni.key,ni.value)
                else:
                    treee=AVLTree()
                    treee.insert(ni.key,ni.value)
                    self.tree_caps.insert(na,treee)
        elif col==4:
            xx=None
            x=self.tree_caps.root
            while x!=None:
                if x.key>=size:
                    xx=x
                    x=x.right
                else:
                    x=x.right
            if xx==None:
                raise NoBinFoundException
            else:
                tr=xx.value
                ni=tr.get_max_value_node(tr.root)
                ni.value.add_obj(ob)
                na=ni.value.cap
                ob.bin=ni.value
                tr.delete(ni.key)
                if tr.root==None:
                    self.tree_caps.delete(xx.key)
                tre=self.tree_caps.search(na)
                if tre is not None:
                    tre.value.insert(ni.key,ni.value)
                else:
                    treee=AVLTree()
                    treee.insert(ni.key,ni.value)
                    self.tree_caps.insert(na,treee)
        elif col==2:
            xx=None
            x=self.tree_caps.root
            while x!=None:
                if x.key>=size:
                    xx=x
                    x=x.left
                else:
                    x=x.right
            if xx==None:
                raise NoBinFoundException
            else:
                tr=xx.value
                ni=tr.get_max_value_node(tr.root)
                ni.value.add_obj(ob)
                na=ni.value.cap
                ob.bin=ni.value
                tr.delete(ni.key)
                if tr.root==None:
                    self.tree_caps.delete(xx.key)
                tre=self.tree_caps.search(na)
                if tre is not None:
                    tre.value.insert(ni.key,ni.value)
                else:
                    treee=AVLTree()
                    treee.insert(ni.key,ni.value)
                    self.tree_caps.insert(na,treee)
        elif col==3:
            xx=None
            x=self.tree_caps.root
            while x!=None:
                if x.key>=size:
                    xx=x
                    x=x.right
                else:
                    x=x.right
            if xx==None:
                raise NoBinFoundException
            else:
                tr=xx.value
                ni=tr.get_min_value_node(tr.root)
                ni.value.add_obj(ob)
                na=ni.value.cap
                ob.bin=ni.value
                tr.delete(ni.key)
                if tr.root==None:
                    self.tree_caps.delete(xx.key)
                tre=self.tree_caps.search(na)
                if tre is not None:
                    tre.value.insert(ni.key,ni.value)
                else:
                    treee=AVLTree()
                    treee.insert(ni.key,ni.value)
                    self.tree_caps.insert(na,treee)
        self.tree_obj.insert(object_id,ob)
            
    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        de=self.tree_obj.search(object_id)
        if de == None:
            return None
        bino=de.value.bin
        bincap=bino.cap
        f=self.tree_caps.search(bincap)
        fu=f.value
        fu.delete(bino.binid)
        bino.remove_object(object_id)
        self.tree_obj.delete(object_id)
        if fu.root==None:
            self.tree_caps.delete(bincap)
        
        tre=self.tree_caps.search(bino.cap)
        if tre is not None:
            tre.value.insert(bino.binid,bino)
        else:
            treee=AVLTree()
            treee.insert(bino.binid,bino)
            self.tree_caps.insert(bino.cap,treee)

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        node=self.tree_binids.search(bin_id)
        if node==None:
            return None
        binoo=node.value
        l=binoo.tree.in_order()
        return (binoo.cap,l)
        
    
        pass

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        node=self.tree_obj.search(object_id)
        if node==None:
            return None
        return node.value.bin.binid
        pass
    
    