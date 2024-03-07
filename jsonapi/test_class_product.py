from class_product import Product
import pytest

class TestProduct:
    def test_fechAll(self):
        result = Product.fetchAll()
        assert isinstance(result, list) # Verifica che il risultato sia un array
        assert None not in result # Verifica che non ci siano valori nulli nell'array

    def test_Create(self):
            new_product = {
                        'nome': 'Occhiali',
                        'marca': 'LV',
                        'prezzo': 8970
                    }
            product = Product.Create(new_product)
            assert product.nome == new_product["nome"] and product.marca == new_product["marca"] and product.prezzo == new_product["prezzo"]

    
    def test_find(self):
        id_product = 45
        product = Product.find(id_product)
        assert product != None and product.nome == 'tosaerba' and product.marca == 'oleomac' and product.prezzo == 289.99
    
    
    def test_update(self):
        id_product = 14
        product = Product.find(id_product)
        update_product = {
                    'nome': 'Trattore',
                    'marca': 'Ferrari',
                    'prezzo': 5678
                }
        product.update(update_product)
        found_product = Product.find(id_product)
        assert found_product.nome == update_product["nome"] 
        assert found_product.marca == update_product["marca"] 
        assert found_product.prezzo == update_product["prezzo"]
        
    def test_delete(self):
        id_product = 14
        product = Product.find(id_product)
        product.delete()
        found_product = Product.find(id_product)
        assert  found_product == None