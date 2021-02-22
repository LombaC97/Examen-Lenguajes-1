from pregunta6 import *
import unittest
from io import StringIO
from unittest.mock import patch

class expresionesTest(unittest.TestCase):

    def test_evaluar_expresion(self):
        expresion = "EVAL POST 8 3 - 8 4 4 + * +"
        a_evaluar = expresion.split(' ')              
        self.assertEqual(evalExpresion(a_evaluar[2:]) , 69)

    def test_expresion_invalida(self):
        expresion = "EVAL POST 6 4 h"
        a_evaluar = expresion.split(' ')
        self.assertFalse(esValida(a_evaluar))

    def test_crea_arbol(self):
        expresion = "EVAL POST 8 3 - 8 4 4 + * +"
        a_evaluar = expresion.split(' ')       
        arbol = crearArbol(a_evaluar[2:])
        self.assertNotEqual(arbol, [])
    
    def test_mostrar_expresion(self):
        expresion = "MOSTRAR POST 8 3 - 8 4 4 + * +"
        a_evaluar = expresion.split(' ')       
        arbol = crearArbol(a_evaluar[2:])
        with patch('sys.stdout', new=StringIO()) as fake_out:
            arbol.verExpresion()
            self.assertEqual(fake_out.getvalue()[:-1], '8 - 3 + 8 * (4 + 4)\n') 

    def test_main(self):

        expresion = "EVAL PRE + * + - 3 4 5 7 3\nMOSTRAR POST 8 3 5 - /\nEVAL POST 8 3 -\nSALIR\n"
        
        with patch('sys.stdin', StringIO(expresion)) as mocked_stdin:
            with patch('sys.stdout', new=StringIO()) as mocked_stdout:

                main()
                output = mocked_stdout.getvalue()                
                expected_output = "Ingrese la expresion que desee ejecutar: \n45\nIngrese la expresion que desee ejecutar: \n8 / (3 - 5)\n\nIngrese la expresion que desee ejecutar: \n5\nIngrese la expresion que desee ejecutar: \n"
                
                self.assertEqual(output, expected_output)


   