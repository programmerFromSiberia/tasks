# необходимо реализовать возможность подсчета товаров
# общий список товаров
# добавление товара в магазин
# удаление товара из магазина



class Product:
    def __init__(self, name: str = '', category: str = '', price: int = 0):
        self.__name = name
        self.__category = category
        self.__price = price

    def show(self):
        print(self.__name, self.__category, self.__price, end=' | ')


class Shop:
    def __init__(self, name: str = '', *products: Product):
        if not(type(name) == str):
            raise TypeError('name is not str')
        if not(type(products) in [Product, tuple]):
            raise TypeError('products is not Product or tuple')
        
        self.__name = name
        self.__products = []
        for product in products:
            self.__products.append(product)
        
    def show(self):
        print(self.__name, ' : ')
        for product in self.__products:
            product.show()
    
    @property
    def products(self):
        return self.__products
    
    def append_product(self, *products: Product):
        if not(type(products) in [Product, tuple]):
            raise TypeError('products is not Product or tuple')
        for product in products:
            self.__products.append(product)
    
    def del_product(self, product: Product):
        if not(type(product) == Product):
            raise TypeError('products is not Product ')
        self.__products.remove(product)

shop = Shop('SHOP_2_0', Product('short', 'одежда', 250), Product('boots', 'обувь', 2000), Product('jerry', 'украшение', 10000))
shop.show()