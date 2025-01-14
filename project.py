import csv
import os

class Stockitem:
    stock_category = "Car Accessories"

    def __init__(self, code):
        self.__stock_code = code
        self.__stock_quantity = 0
        self.__stock_price = 0.0

    def get_stock_quantity_and_price(self):
        try:
            self.__stock_quantity = int(input("Enter the Stock quantity: "))
            self.__stock_price = float(input("Enter the price for the stock: "))
        except ValueError as e:
            print(f"Input Error: {e}")
        else:
            print(f"Created Stock with {self.__stock_quantity} units of {self.get_stock_name()}, price {self.__stock_price} each, and code {self.__stock_code}\n\n")

    def setstockprice_withvat(self):
        return self.__stock_price + (self.__stock_price * 0.175)

    def get_stock_name(self):
        return "Unknown Stock Name"

    def get_Stock_Description(self):
        return "Unknown Stock Description"

    def increase_stock(self):
        self.__stock_quantity += self.incamount

    def decrease_stock(self):
        self.__stock_quantity -= self.decamount

    def update_price(self):
        self.__stock_price = self.new_price

    def __str__(self):
           
        return ("-----------------------------------------------------\n"
                           "\t\tPrinting stock information\n"
                "-----------------------------------------------------"
                 f"\nStock Category   \t: {Stockitem.stock_category}"
                 f"\nStock Type       \t: {self.get_stock_name()}"
                 f"\nDescription      \t: {self.get_Stock_Description()}"
                 f"\nStock Code       \t: {self.__stock_code}"
                 f"\nUnits in Stock   \t: {self.__stock_quantity}"
                 f"\nPrice Without VAT\t: RS.{self.__stock_price}"
                 f"\nPrice With VAT   \t: RS.{self.setstockprice_withvat()}")


    def get_quantity_to_increase(self):
        try:
            self.incamount = int(input("Enter the stock quantity you want to add: "))
            if 1 <= self.incamount <= 100:
                self.increase_stock()
                self.comment = f"Stock increased by {self.incamount}"
            else:
                print("Error! Please enter a quantity between 1-100.")
        except ValueError as e:
            print(f"Input Error: {e}")
            
        
            

    def get_quantitysold(self):
        if self._Stockitem__stock_quantity <= 0:
            print("Stock is empty! Please add some stock before selling again!")
            self.increase_stock_infile()
            return  
        
        try:
            self.decamount = int(input("Enter the stock quantity sold: "))
            if self.decamount <= 0:
                print("Error! Sold quantity must be greater than 0.")
            elif self.decamount <= self.__stock_quantity:
                self.decrease_stock()
                self.comment = f"Stock sold by {self.decamount}"
                print(f"\n\nDecreased {self.decamount} units of {self.get_stock_name()}.\nPrinting stock information...\n")
                self.save_data()
            else:
                print("Error! Sold quantity exceeds available stock.")
        except ValueError as e:
            print(f"Input Error: {e}")

    def get_new_price(self):
        try:
            self.new_price = float(input("\n\nEnter the new price of the item: "))
            self.comment= "Changed price "
        except ValueError as e:
            print(f"Input Error: {e}")
        else:
            self.update_price()

class NavSys(Stockitem):
    
    def __init__(self, code):
        super().__init__(code)
        self.__brand = "Starlink"

    def get_stock_name(self):
        return "Navigation System"

    def get_Stock_Description(self):
        return "Geovision Sat Nav"

    def save_data(self):
        filename = 'data.csv'
        try:
            if os.path.exists(filename):
                 mode = 'a'
                 
            else :
                 mode = 'w'
            with open(filename, mode, newline='') as f:
                writer = csv.writer(f)
                if mode == 'w':
                    writer.writerow(['Stock Code', 'Stock Brand', 'Stock Quantity', 'Stock Price', 'Comments'])
                writer.writerow([self._Stockitem__stock_code, self.__brand, self._Stockitem__stock_quantity, self._Stockitem__stock_price,self.comment])
                print("Data saved successfully.")
        except Exception as e:
            print(f"File Error: {e}")

    def load_data(self):
        filename = 'data.csv'
        try:
            with open(filename, "r", newline='') as f:
                reader = csv.reader(f)
                next(reader)  
                rows = list(reader)
                if rows:
                    x = rows[-1]
                    self._Stockitem__stock_code = x[0]
                    self.__brand = x[1]
                    self._Stockitem__stock_quantity = int(x[2])
                    self._Stockitem__stock_price = float(x[3])
                    print(self)
                else:
                    print("No data found in the file.")
        except FileNotFoundError:
            print("Data file not found.")
        except Exception as e:
            print(f"File Error: {e}")
    
    def check_data_exists(self):
        filename='data.csv'
        try:
            with open (filename,'r',newline='') as f :
                reader=csv.reader(f)
                next(reader)
                rows=list(reader)
                if rows:
                    x=rows[-1]
                    self._Stockitem__stock_code = x[0]
                    self.__brand = x[1]
                    self._Stockitem__stock_quantity = int(x[2])
                    self._Stockitem__stock_price = float(x[3])
                    return True
                
        except FileNotFoundError:
            return False  
        
        except Exception as e:
            print(f"File Error: {e}")
            return False 
        
        
        return False  
              

    def change_price_infile(self):
        try:
            self.get_new_price()
            self.save_data()
            print("Price updated in file.")
        except Exception as e:
            print(f"File Error: {e}")

    def increase_stock_infile(self):
        try:
            
            self.get_quantity_to_increase()
            if self.incamount > 0 and self.incamount<=100: 
                self.save_data()
                print(f"\n\nIncreased {self.incamount} units of {self.get_stock_name()}.")
            else:
                print("Error! Please enter a quantity greater than 0 and less than 100.")
                
           
        except Exception as e:
            print(f"File Error: {e}")
            

    def save_Data_infile_after_sell(self):
        try:
            self.get_quantitysold()
            
            print("Data saved after selling stock.")
        except Exception as e:
            print(f"File Error: {e}")

    def __str__(self):
        return super().__str__() + f"\nBrand Name      \t: {self.__brand} \n-----------------------------------------------------\n\n"

    def choosing_option(self):
        while True:
            try:
                self.option = int(input("Enter your choice (1-6):\n1. Create Stock\n2. Display Stock Information\n3. Increase Stock Quantity\n4. Sell Stock\n5. Set New Price for Stock\n6. Exit System\n\n"))
            except ValueError:
                print("Invalid input. Please enter a number between 1-6.")
                
            except Exception as e:
                print(f"Error {e}")

            else:

                if self.option == 1:
                    if self.check_data_exists():
                        print("Stock already esists adding to existing stock!!")
                        self.increase_stock_infile()
                        
                    else:
                        print("No previous stock exists so creating a new entry !!")
                        self.get_stock_quantity_and_price()
                        self.comment = "new stock entry"
                        self.save_data()
                        
                elif self.option == 2:
                    self.load_data()
                    
                    
                    
                elif self.option == 3:
                    self.incamount=0
                    self.increase_stock_infile()
                    
                    
                elif self.option == 4:
                    if self._Stockitem__stock_quantity<=0:
                        print("please increase stock first!!")
                        self.increase_stock_infile
                    else:
                        self.get_quantitysold()
                        
                        
                        
                elif self.option == 5:
                    self.change_price_infile()
                    
                    
                elif self.option == 6:
                    print("Exiting system...")
                    break
                else:
                    print("No such option exists!")


a = NavSys("NAVSYS-01")
a.choosing_option()