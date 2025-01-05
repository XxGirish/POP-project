import csv
import os



class Stockitem:

    stock_category="Car acessories"

    def __init__(self,code):
        self.__stock_code=code
        self.__stock_quantity=""
        self.__stock_price=""

    def getStockQuantityandprice(self):
        self.__stock_quantity=int(input("Enter the Stock quantity"))
        self.__stock_price=float(input("Enter the price for the stock"))
        print(f"Created Stock with {self.__stock_quantity} units  {self.getstockname()}, price {self.__stock_price} each ,and code is{self.__stock_code}\n\n")
    
    def setstockprice_withvat(self):
        return self.__stock_price+(self.__stock_price*0.175)
        
    def getstockname(self):  
        return "Unknown Stock Name"

    def getStockDescription(self):
        return "Unknown Stock Description"  

    def increase_stock(self):
         self.__stock_quantity=self.__stock_quantity+self.incamount
         return self.__stock_quantity

    def decrease_stock(self):
         self.__stock_quantity=self.__stock_quantity-self.decamount
         return self.__stock_quantity

    

   
    def __str__(self):
        return (f"\nStock Category= {Stockitem.stock_category}"
                f"\nstock type={self.getstockname()}"
                f"\nDescription={self.getStockDescription()}"
                f"\nStock Code={self.__stock_code}"
                f"\nUnit in stock = {self.__stock_quantity}"
                f"\nPrice without VAT={self.__stock_price}"
                f"\nPrice with VAT={self.setstockprice_withvat()}")

    def get_quantity_to_increase(self):
        self.incamount=int(input("enter the stock quantity u want to add"))
        if (self.incamount<1 or self.incamount<100):
            
                 self.increase_stock()
                 print(f"\n\nIncreasing {self.incamount} units of  {self.getstockname()}\n Printing stock information\n")
                 print(a)

        else:
            print("Error!!(please enter quantity between 0-100)")
   

    def get_quantitysold(self):
        self.decamount=int(input("enter the stock quantity sold"))
        if (self.decamount<self.__stock_quantity ):
             self.decrease_stock()
             print(f"\n\nDecreasing{self.incamount} units of  {self.getstockname()}\n Printing stock information\n")
             print(a)
            

    def getnewprice(self):
        self.newprice=int(input("\n\nenter the new price of the item"))
        
       
        
        



class NavSys(Stockitem):

    def __init__(self,code):
        super().__init__(code)
        self.__brand="Starlink"

        
    def getstockname(self):
        return "Navigation System"

    def getstockStockDescription(self):
        return "Geovision Sat Nav"

    def save_data(self):
        filename='data.csv'
        if os.path.exists(filename):
            
            with open(filename,'a',newline='') as f:
                writer=csv.writer(f)
                
                writer.writerow([self._Stockitem__stock_code,self.__brand,self._Stockitem__stock_quantity,self._Stockitem__stock_price])
                print("data saved sucessfully")
        else:
            with open(filename,'w',newline='') as f:
                writer=csv.writer(f)
                writer.writerow(['Stock code','stock Brand','stock quantity','stock price'])
                writer.writerow([self._Stockitem__stock_code,self.__brand,self._Stockitem__stock_quantity,self._Stockitem__stock_price])
                print("created a data.scv file and saved data sucessfully")
            
    
    def load_data(self):
         
         filename='data.csv'
         with open (filename,"r",newline='') as f:
             read=csv.reader(f)
             next(read)
             rows=list(read)

             if rows:
                 f=rows[-1]
                 self._Stockitem__stock_code=f[0]
                 self.__brand=f[1]
                 self._Stockitem__stock_quantity=int(f[2])
                 self._Stockitem__stock_price=float(f[3])

             else:
                 
                 print("no data found")


    def change_price_infile(self):
        filename='data.csv'
        if os.path.exists(filename):
            with open(filename,'w',newline='') as f:
                next(read)
                rows=list(read)

            if rows:
                f=rows[-1]
                f[3]=self.newprice

            else:
                print("NO data in file")

        else:
            print("no file exists")
                
    def __str__(self):
        return super().__str__() +f"\nBrand name ={self.__brand}"
        
    def choosing_option(self):
        while True:
                self.option=int(input("Enter your choice :(1-6) \n1.Create stock \n2.Display stock information \n3.Increase Stock quantity \n4.Update quantity after sell \n5.Set new price for stock\n6.Exit system\n\n"))
    
            
    
                if self.option==1:
                    self.getStockQuantityandprice()
                    self.save_data()
                    
                if self.option==2:
                    
                    self.load_data()
                    self.setstockprice_withvat()
                    print("displaying stock information")
                    print(a)
                    
                elif self.option==3:
                    self.get_quantity_to_increase()
                    
                elif self.option==4:
                    self.get_quantitysold()
                
                elif self.option==5:
                    self.getnewprice()
                    self.change_price_infile()
    
                elif self.option==6:
                    print("Exiting system...")
                    break
                
                else:
                    print("no such option exists!!")
                    



a=NavSys("NAVSYS-01")
a.choosing_option()



       