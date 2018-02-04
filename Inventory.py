class Product:
    
    def __init__(self,name, inventory):
        self.name = name
        self.price_list = {t: None for t in inventory}
        self.quantity_list = {t: 0 for t in inventory}
    
    def generation_table(self):
        
        rezultat = 'Our inventory: \n\n'
        
        for stuff, price in self.quantity_list.items():
            if self.quantity_list[stuff] > 0:
                rezultat += f'- {stuff} - {price:.2f}\n'
            else:
                rezultat += f'- {stuff} - 0\n'
        
        return rezultat 
    
    def add_stuff(self, stuff, quantity):
        self.quantity_list[stuff] += quantity
    
    def add_price(self, stuff, price):
        self.price_list[stuff] = price
    
    def value_stuff(self, stuff, quantity):
        if self.price_list[stuff] and self.quantity_list[stuff]:
            self.quantity_list[stuff] -= quantity
            return self.price_list[stuff] * quantity
        else:
            return 'Oops, something went wrong. Please try again'
        
  