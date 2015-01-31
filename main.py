import bicycles

separator = ("==" * 30)
separator1 = ("*=" * 30)

bike1 = bicycles.Bicycle("Giant Propel","10 lbs","200")

bike2 = bicycles.Bicycle("Giant Propel Advance Pro","20 lbs","1000")

bike3 = bicycles.Bicycle("Trek Madone","20 lbs","995")

bike4 = bicycles.Bicycle("Cannondale Supersix","20 lbs","500")

bike5 = bicycles.Bicycle("Cannondale 3","50 lbs","100")

bike6 = bicycles.Bicycle("Cannondale 7","40 lbs","150")

bikeList = [bike1.name, bike2.name, bike3.name, bike4.name, bike5.name, bike6.name]
bikeCost = [bike1.cost, bike2.cost, bike3.cost, bike4.cost, bike5.cost, bike6.cost]

# Shops

store1 = bicycles.Shops("Xtra Bike", "6", "20 %","10 % profit")

# Customers

customer1 = bicycles.Customers("Hans","1,000","buy")

customer2 = bicycles.Customers("Nino","500","buy")

customer3 = bicycles.Customers("Roy","200","buy")

# Customer List

customerList = [customer1.customerName, customer2.customerName, customer3.customerName]
customerMoney = [customer1.money, customer2.money, customer3.money]

#Print the bike name

print separator

#Print the store name and inventory

print store1.shopName, "Store has", store1.inventory, "Bikes"
print separator1

for bikeList, bikeCost in zip(bikeList, bikeCost):
    print '{0} costs --> $ {1}'.format(bikeList, bikeCost)

# print questions

print separator

client = int(input("Enter Budget: $ "))

if client <= 1000:
    print "Available bikes: ", bike1.name,"," ,bike2.name,"," ,bike3.name,"," ,bike4.name, ",",bike5.name, "," ,bike6.name
elif client <= 900:
    print "Available bikes: ", "," , bike1.name, "," , bike4.name, "," , bike5.name, "," , bike6.name
elif client <= 800:
    print "Available bikes: ", bike1.name, "," ,bike4.name, "," , bike5.name, "," ,bike6.name
elif client <= 700:
    print "Available bikes: ", bike1.name, "," ,bike4.name, "," ,bike5.name, "," ,bike6.name
elif client <= 600:
    print "Available bikes: ", bike1.name, "," ,bike4.name, "," ,bike5.name, "," ,bike6.name
elif client <= 500:
    print "Available bikes: ", bike1.name, "," , bike5.name, "," ,bike6.name
elif client <= 400:
    print "Available bikes: ", bike1.name,"," ,bike5.name, "," ,bike6.name
elif client <= 300:
    print "Available bikes: ", bike1.name,"," ,bike5.name, "," ,bike6.name
elif client <= 200:
    print "Available bikes: ", bike1.name,"," ,bike5.name, "," ,bike6.name
else:
    print "There is no bike on that price range"


#Print customer list   
print separator

for customerList, customerMoney in zip( customerList, customerMoney):
    print '{0} has $ {1} to buy a bike'.format(customerList, customerMoney) 

print separator

