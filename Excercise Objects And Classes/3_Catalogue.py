class Catalogue:
    def __init__(self, catalogue_name):
        self.name = catalogue_name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [i for i in self.products if i.startswith(first_letter)]

    def __repr__(self):
        result = ''
        sorted_products = sorted(self.products)
        result += f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(sorted_products)
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
