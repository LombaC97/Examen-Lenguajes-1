import buddy
import unittest
from collections import Counter

class TestTreeMethods(unittest.TestCase):
   
    def test_treeInstance(self):
        miArbol = buddy.ArbolBinario(16)
        self.assertIsInstance(miArbol, buddy.ArbolBinario)
   
    #checks if all child nodes of the root node are free after creating a tree
    def test_no_entries(self):
        miArbol = buddy.ArbolBinario(16)
        self.assertIsNone(miArbol.revisarHijos(miArbol.raiz))

    
    #checks if theres one child after doing an insertion 
    def test_new_child_entry(self):
        miArbol = buddy.ArbolBinario(16)
        miArbol.agregar(3, 'Etiqueta')
        self.assertTrue(miArbol.revisarHijos(miArbol.raiz))
    #checks if all children are occupied after inserting a block in the root
    def test_all_childs_entry(self):
        miArbol = buddy.ArbolBinario(16)
        miArbol.agregar(16, 'Etiqueta')
        self.assertTrue(miArbol.revisarHijosPrint(miArbol.raiz))
    
    #checks what happens if trying to insert a block bigger than available space
    def test_too_large(self):
        miArbol = buddy.ArbolBinario(16)        
        self.assertIsNone(miArbol.agregar(17, 'No valido'))

    #checks what happens when trying to insert the same etiqueta two times
    def test_existing_name(self):
        miArbol = buddy.ArbolBinario(16)
        miArbol.agregar(1, 'Hola')
        self.assertIsNone(miArbol.agregar(2,'Hola'))

    #checks what happens when inserting a valid block in a new tree
    def test_new_entry(self):
        miArbol = buddy.ArbolBinario(16)
        self.assertTrue(miArbol.agregar(2,'Hola'))
    
    #checks if the new block etiqueta exists in tree
    def test_new_etiqueta(self):
        miArbol = buddy.ArbolBinario(16)
        miArbol.agregar(3,'Hola')
        self.assertTrue('Hola' in miArbol.names)

    #checks if the new block etiqueta does not exists more than just one time after trying to insert
    #two blocks with the same etiqueta
    def test_new_etiqueta_twice(self):
        miArbol = buddy.ArbolBinario(16)        
        miArbol.agregar(3,'Hola')
        miArbol.agregar(1,'Hola')
        d = miArbol.names.count('Hola')
        self.assertEqual(d, 1)
    
    #checks if a given block was erased from tree
    def test_free_block(self):
        miArbol = buddy.ArbolBinario(16)
        miArbol.agregar(5, 'Hola')
        self.assertTrue(miArbol.liberar('Hola'))

    #checks if the etiqueta was actually erased from the tree
    def test_erased_etiqueta_block(self):
        miArbol = buddy.ArbolBinario(16)
        miArbol.agregar(3,'Hola')
        miArbol.liberar('Hola')
        self.assertFalse('Hola' in miArbol.names)
    #checks what happens when trying to free a non existing etiqueta block
    def test_not_existing_etiqueta(self):
        miArbol = buddy.ArbolBinario(16)
        self.assertIsNone(miArbol.liberar('Hola'))

    #checks what happens when trying to free two different blocks
    def test_erasing_two_blocks(self):
        miArbol = buddy.ArbolBinario(16)
        miArbol.agregar(3, 'Hola1')
        miArbol.agregar(3, 'Hola2')
        self.assertTrue(miArbol.liberar('Hola2'))
        self.assertTrue(miArbol.liberar('Hola1'))
        
    #checks if all children are occupied after inserting and erasing a root block
    def test_free_tree(self):
        miArbol = buddy.ArbolBinario(16)
        miArbol.agregar(16, 'Lo llene todo')
        miArbol.liberar('Lo llene todo')
        self.assertIsNone(miArbol.revisarHijos(miArbol.raiz))

    #checks if a branch is occupied after inserting a new node
    def test_occupied_branch(self):
        miArbol = buddy.ArbolBinario(16)
        node = miArbol.agregar(8, 'Hola')
        self.assertTrue(miArbol.revisarHijos(node))

    #checks if a branch is free after inserting and freeing a new node
    def test_free_branch(self):
        miArbol = buddy.ArbolBinario(16)
        node = miArbol.agregar(8, 'Hola')
        miArbol.liberar('Hola')
        self.assertIsNone(miArbol.revisarHijosPrint(node))
    #Prints a free tree
    def test_print_tree(self):
        miArbol = buddy.ArbolBinario(16)
        miArbol.printArbol(miArbol.raiz)
        print("\n\n")
    #Prints a tree with just one node inserted
    def test_print_tree2(self):
        miArbol = buddy.ArbolBinario(16)
        miArbol.agregar(1,'Hola')
        miArbol.printArbol(miArbol.raiz)
        print("\n\n")
    #prints a tree with some nodes inserted
    def test_print_tree3(self):
        miArbol = buddy.ArbolBinario(32)       
        miArbol.agregar(1,'Hola')
        miArbol.agregar(8,'Hola2')
        
        miArbol.printArbol(miArbol.raiz)
        print("\n\n")

if __name__ == '__main__':
    unittest.main()
