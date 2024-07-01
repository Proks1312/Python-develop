class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products = file.read()
        return products

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_product_names = [product.split(', ')[0] for product in existing_products]

        new_products = []
        for product in products:
            if product.name in existing_product_names:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                new_products.append(str(product))

        if new_products:
            with open(self.__file_name, 'a') as file:
                for product in new_products:
                    file.write(product + '\n')

apple = Product("Apple", 100.0, "Fruit")
potato = Product("Potato", 50.0, "Vegetables")
chiken = Product("Chiken" , 1000 , "Meat")


# shop = Shop()

# print(shop.get_products())

# shop.add(apple, potato,chiken)

# print(shop.get_products())
