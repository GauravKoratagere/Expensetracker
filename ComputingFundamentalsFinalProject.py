# In order for the graph function to work, matplotlib needs to be downloaded to your machine
# To download, type in the terminal: pip install matplotlib
#Test for Github

import matplotlib.pyplot as plt

monthlyReturnRate = 0.07/12
time = 30
#Task 1:
class monthly_Spending:
    def __init__ (self):
        self.housing= 0.0
        self.charges= 0.0
        self.utilities = 0.0
        self.transportation = 0.0
        self.food= 0.0
        self.neededTotal= 0.0
        self.salary= 0.0
        self.spending= 0.0
        self.savings= 0.0
    #Task 2:
    def input_values(self):
        print("For the expense tracker, it will need information about your monthly finances")
        self.salary = float(input("What is your monthly salary after tax: $"))
        self.housing =float(input("How much do you spend monthly on housing: $"))
        self.transportation = float(input("How much do you spend monthly on transportation (gas, buspass, ect.): $"))
        self.food = float(input("How much do you spend monthly on food: $"))
        self.utilities = float(input("How much do you spend monthly on utilites: $"))
        self.charges = float(input("How much do you spend monthly on other needed monthly expenses: $"))
        self.spending = float(input("How much do you use for nonessential monthly spending: $"))
        self.neededTotal= self.housing+self.charges+self.utilities+self.transportation+self.food
        self.savings= self.salary - self.neededTotal-self.spending
        print("Thank you for entering your information")
#Task 3:
    def checksavings(self):
        print("Your currently saving $", self.savings, " every month.")
        if self.savings <= 0:
            print("You are currently not saving any money.")
            if self.spending >= 0:
                print ("You might want to cut down on your nonessential spending.")
        else:
            print ("You are currently saving $", self.savings)
            wealth_Invested=round((self.savings)*((((1+(monthlyReturnRate))**(time*12))-1)/(monthlyReturnRate))*(1+(monthlyReturnRate)),2)
            print("You could make", monthly_Spending.add_commas(wealth_Invested), "$ over the course of 30 years if you put the money into an S&P 500 with roughly seven percent in annual returns.")
 #Task 4:       
    def graph_Investment(self):
     months = time * 12 
     investmentValues = []
     for month in range(1, months + 1): 
               currentValue = self.savings * ((((1 + monthlyReturnRate) ** month) - 1) / monthlyReturnRate) * (1 + monthlyReturnRate) 
               investmentValues.append(currentValue)

     monthsArray = list(range(1, months + 1))

     plt.plot(monthsArray, investmentValues) 
     plt.title("Investment Growth Over Time") 
     plt.xlabel("Months") 
     plt.ylabel("Investment Value ($)")
     plt.grid(True) 
     plt.show()

    @staticmethod
    def add_commas(number):
        return "{:,}".format(number)

#TO Test if it runs
def mainExpenceFunction():
    Expance1 = monthly_Spending()
    Expance1.input_values()
    Expance1.checksavings()
    Expance1.graph_Investment()
    
mainExpenceFunction()



