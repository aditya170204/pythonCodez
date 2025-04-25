print("welcome to the theatre")
pizzaPrice=100
burgerPrice=80
colddrink=50
numpizza=int(input("enter the num of pizza you want"))
numburger=int(input("enter the num of burger you want"))
numdrink=int(input("enter the num of drink you want"))


print(f"your bill\npizza {numpizza*pizzaPrice}\nburger {numburger*burgerPrice}\ncolddrink {numdrink*colddrink}\nTotal Amount= {(numpizza*pizzaPrice)+(numburger*burgerPrice)+(numdrink*colddrink)}")