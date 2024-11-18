# In order for the graph function to work, matplotlib needs to be downloaded to your machine
# To download, type in the terminal: pip install matplotlib

import matplotlib.pyplot as plt

monthlyReturnRate = 0.07/12
time = 30

#Task 1:
class monthly_Spending:
            
    @staticmethod
    def add_commas(number):
        return "{:,}".format(number)
    
    def __init__ (self):
        self.__housing= 0.0
        self.__charges= 0.0
        self.__utilities = 0.0
        self.__transportation = 0.0
        self.__food= 0.0
        self.__neededTotal= 0.0
        self.__salary= 0.0
        self.__spending= 0.0
        self.__savings= 0.0
    #Task 2:
    def input_values(self):
        print("For the expense tracker, it will need information about your monthly finances")
        self.__salary = float(input("What is your monthly salary after tax: $"))
        self.__housing =float(input("How much do you spend monthly on housing: $"))
        self.__transportation = float(input("How much do you spend monthly on transportation (gas, buspass, ect.): $"))
        self.__food = float(input("How much do you spend monthly on food: $"))
        self.__utilities = float(input("How much do you spend monthly on utilites: $"))
        self.__charges = float(input("How much do you spend monthly on other needed monthly expenses: $"))
        self.__spending = float(input("How much do you use for nonessential monthly spending: $"))
        self.__neededTotal= self.__housing+self.__charges+self.__utilities+self.__transportation+self.__food
        self.__savings= self.__salary - self.__neededTotal-self.__spending
        print("Thank you for entering your information")

 #Task 3:       
    def graph_Investment(self):
     months = time * 12 
     investmentValues = []
     for month in range(1, months + 1): 
               currentValue = self.__savings * ((((1 + monthlyReturnRate) ** month) - 1) / monthlyReturnRate) * (1 + monthlyReturnRate) 
               investmentValues.append(currentValue)

     monthsArray = list(range(1, months + 1))

     plt.plot(monthsArray, investmentValues) 
     plt.title("Investment Growth Over Time") 
     plt.xlabel("Months") 
     plt.ylabel("Investment Value ($)")
     plt.grid(True) 
     plt.show()
#Task 4:
    def checksavings(self):
         if self.__savings <= 0:
             print("You are currently not saving any money.")
             if self.__spending >= 0:
                 print ("You might want to cut down on your nonessential spending.")
                 return (False)
         else:
             print ("You are currently saving $", self.__savings, " every month.")
             wealth_Invested=round((self.__savings)*((((1+(monthlyReturnRate))**(time*12))-1)/(monthlyReturnRate))*(1+(monthlyReturnRate)),2)
             print("You could make $",monthly_Spending.add_commas(wealth_Invested), " over the course of 30 years if you put the money into an S&P 500 with roughly seven percent in annual returns.")
             return (True)
#Task 5:
    def display_yearly(self):
        print("your yearly housing spending is about $", monthly_Spending.add_commas(12*self.__housing))
        print("your yearly nonessential spending is about $", monthly_Spending.add_commas(12*self.__spending))
        print("your yearly transportation spending is about $", monthly_Spending.add_commas(12*self.__transportation))

    
#TO Test if it runs
def mainExpenseFunction():
    x=0
    while x == 0:
        print ("""Would you like to use the Expence Tracker?
               1: Yes
               2: No""")
        y = int(input('Put in 1 or 2: '))
        if y == 1:
                   Expanse1 = monthly_Spending()
                   Expanse1.input_values()
                   Expanse1.display_yearly()
                   a = Expanse1.checksavings()
                   if a == True:
                       Expanse1.graph_Investment()
        elif y == 2 :
            print ("Thank you for your time")
            x += 1
        else:
            print ("It seems that your imput was not a 1, or a 2")
    
mainExpenseFunction()
