# hiistr="Mayur gorane you are great"
# print(len(hiistr))
# #following given are standard for any line
# #print(hiistr[0:26:1])
# # string[start:end:step] # thIS is formula of string slicing
# #print(hiistr.capitalize())
# #print(hiistr.replace("are","she"))

# qes on stack and price
# data on process
# | Stock | Prices |
# | ------- | ---------- |
# | info | [600, 630, 620] |
# | ril | [1430, 1490, 1567] |
# | mtl | [234, 180, 160] |
import statistics
market = {"info" : [600, 630, 620],"ril" : [1430, 1490, 1567],"mtl" : [234, 180, 160]}
print(market)

def print_on():
    for stock,price in market.items():
        ave = statistics.mean(price)
        print(stock ,"==>",market[stock],"==>  average =",ave)

def add():
    stock = input("Enter stack name -")
    stock.lower()
    if stock in market:
        print("you entered stack entity are already on our data if you want to add new price value so can add it or it ")
        delete_keys = market.pop(stock)
        price_value = int(input('ENTER YOUR STOCK VALUE -'))
        market[stock]= price_value
        market.update()
        print(market)
        return
    price_value = (input("enter your stock value -"))
    price_value2 = int(price_value)
    market[stock] = price_value
    # market.update({stock:price_value})
    print(market)
    return

def main():
    while(True):
        user = input("enter want kind of activity you want to perform i.e add/print - ")
        user.lower()
        if user == "add":
            add()
        elif user == "print":
            print_on()
        elif user == "q":
            print("program are quit")
            break
        else:
            print("wrong input")



if __name__ == '__main__':
    main()




