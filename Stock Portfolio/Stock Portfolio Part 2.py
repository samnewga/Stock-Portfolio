#################################################################################################
#Samael Newgate
#4/22/2018
#CSC102
#################################################################################################
#First, you will need to add the following function:
#
#GetSale - Finds the maximum expected value of selling a stock. The expected sale value of a stock is the current profit minus the future value of the stock:
#Expected Sale value = ( ( Current Price - Buy Price ) - Risk * CurrentPrice ) * Shares
#The GetSale function should calculate this value for each stock in the portfolio, and return the stock symbol with the highest expected sale value.
#Main - Change/update/add the main function. This should take no arguments, but present a menu item consisting of "1. Add Stock", "2. Recommend Sale" and "3. Exit". If the user selects '1,' the Add Stock function is called, and when it is complete, the menu is presented again. If the user selects '2,' the Symbol of the stock corresponding to the highest expected value (returned by GetSale) should be displayed, and the menu presented after completion. If the user selects '3', the program should end.
#Be sure to use comments for both structure of the program and documentation of the code.
#All code must completely be your own individual work product.
#################################################################################################
#creating Dictionaries
Name = dict()
Prices = dict()
Exposure = dict()
#addName function
def addName():
    stockSymbol = input("Please Enter Stock Symbol: ") #input
    stockName = input("Please Enter Stock Name: ") #input
    Name[stockSymbol] = stockName #adding to Name dictionary


def addPrices(stockSymbol):
    array = list() #Creating list to add in dict
    #taking input from user
    buyPrice = float(input("Please Enter Buying Price: "))
    currentPrice = float(input("Please Enter Current Price: "))
    #appending in array
    array.append(buyPrice)
    array.append(currentPrice)
    #adding in dict price
    Prices[stockSymbol] = array

def addExposure(stockSymbol):
    array = list() #Creating list to add in dict
    #taking input from user
    risk = float(input("Please Enter risk: "))
    totalShare = float(input("Please Enter total share amount: "))
    #appending in array
    array.append(risk)
    array.append(totalShare)
    #adding in dict price
    Exposure[stockSymbol] = array



def addStock():
    #calling functions
    print("-"*20)
    print("Adding new Stock")
    print("-"*20)
    addName()
    print("-"*20)
    stockSymbol = input("Please Enter stock Symbol: ")
    print("-"*20)
    addPrices(stockSymbol)
    print("-"*20)
    addExposure(stockSymbol)
    print("-"*20)

def GetSale():
    #o	Expected Sale value = ( ( Current Price - Buy Price ) - Risk * CurrentPrice ) * Shares
    getSale = dict()
    for Namekey,Namevalue in Name.items(): #printing values
        priceCheck = 0 #for printing right values
        exCheck = 0 #for printing right values
        for Priceskey,Pricesvalue in Prices.items():
            if(Priceskey==Namekey and priceCheck==0):
                priceCheck +=1
            for Exposurekey,Exposurevalue in Exposure.items():
                if(Exposurekey==Namekey and exCheck==0):
                    expectedSale = ((Pricesvalue[1]-Pricesvalue[0])-Exposurevalue[0]*Pricesvalue[1])*Exposurevalue[1] #calculating Expected Sale
                    getSale[Namekey]=expectedSale
                    exCheck+=1
    return getSale

def Main():
    while True:
        print("1. Add Stock \n2. Recommend Sale \n3. Exit")
        option = int(input("Please Enter Your Option: "))
        if(option==1):
            addStock()
        elif(option==2):
            key = 0
            value = 0
            Sale = GetSale()
            for k,v in Sale.items(): #loop to calculate max value
                if(v>value):
                    value = v
                    key = k
            print ("Highest expected value is of {} and value is {}".format(key,value))
            
        elif(option==3):
            break
    
Main()
