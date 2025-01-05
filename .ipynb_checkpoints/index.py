

class Stockitem:

    stock_category="Car acessories"

    def __init__(self,code):
        self.__stock_code=code
        self.__stock_quantity=0
        self.__stock_price=0

    
    def getStockQuantityandprice(self):
        self.__stock_quantity=int(input("Enter the Stock quantity"))
        self.__stock_price=float(input("Enter the price for the stock"))

    def setstockprice_withvat(self):
        return self.__stock_price+(self.__stock_price*0.18)
        
    def getstockname(self):  
        return "Unknown Stock Name"

    def getStockDescription(self):
        return "Unknown Stock Description"

    def Display(self):
        print(f"Creating Stock with {self.__stock_quantity} units  {self.getstockname()}, price {self.__stock_price} each ,and code is{self.__stock_code} \n\nPrinting Item stock Information: \nStock Category= {Stockitem.stock_category}\nstock type={self.getstockname()}\nDescription={self.getStockDescription()}\nStock Code={self.__stock_code}\nPrice without VAT={self.__stock_price}\nPrice with VAT={self.setstockprice_withvat()} \nUnit in stock = {self.__stock_quantity}")

    def get_quantity_to_increase(self):
        self.incamount=int(input("enter the stock quantity u want to add"))

    def update_stock(self):
        return self.__stock_quantity+self.incamount

    def updatedisplay(self):
        print(f"\n\nIncreasing {self.incamount} units of  {self.getstockname()}")
        print(f"Printing Item stock Information: \nStock Category= {Stockitem.stock_category}\nstock type={self.getstockname()}\nDescription={self.getStockDescription()}\nStock Code={self.__stock_code}\nPrice without VAT={self.__stock_price}\nPrice with VAT={self.setstockprice_withvat()} \nUnit in stock = {self.update_stock()}")

        



a=Stockitem("weew")
a.getStockQuantityandprice()
a.setstockprice_withvat()
a.Display()
a.get_quantity_to_increase()
a.update_stock()
a.updatedisplay()