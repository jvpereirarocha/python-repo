class Product:
    def __init__(self, description, price):
        self._description = description
        self._price = price

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self.check_element(value)

    def check_element(self, value):
        if int(value) < 0:
            raise Exception('Invalid price')
        else:
            return self.value

    def __str__(self):
        return f"{self.description} - R$ {self.price}"


product = Product("Playstation 5", -1)

print("product: ", product)
