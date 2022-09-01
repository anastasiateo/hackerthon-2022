class Phone:
    count = 0
    def __int__(self):
        self.__make = None
        self.__model = None
        self.__price = 0
        self.__class__.count += 1

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        if price.isdigit():
            self.__price = price
        else:
            self.__price = 0
            print('Price should be in numbers.')

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def __str__(self):
        s = 'The phone created is {} {} priced at ${}. Now has {} phone in total'.format(self.__make, self.__model, self.__price, self.__class__.count )
        return s


make = input("Enter the make of the phone: ")
model = input("Enter the model of the phone: ")
p = input("Enter the price of the phone:$ ")
ph = Phone()
ph.set_make(make)
ph.set_model(model)
ph.set_price(p)
print(ph)


