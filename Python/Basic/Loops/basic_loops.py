def main():
    x = 0

    # define a while loop
    # while (x<5):
    #     print(x)
    #     x = x+1
    
    # Defines loop and loops through the numbers between 5 - 10
    # for x in range(5, 10):
    #     print(x)

    # loop that iterates through all the days of the week
    # days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # for d in days:
    #     print (d)
    
    # Loops through numbers 5 - 10 but breaks at 7 thus printing only 5 - 6
    # for x in range(5,10):
    #     # break function stops the loop from looping further
        # if (x==7): break
    #     # Takes x divided by 2 and if the left over value is 0 
    #     # continue essentially is skipping the rest of the execution for the loop and start back at the top
        # if (x % 2 == 0): continue
        # print(x)

    days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):
        print (i,d)

if __name__ == "__main__":
  main()