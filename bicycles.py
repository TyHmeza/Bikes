class Bicycle():
  """Stores Bicycle information such as name, weight and cost to produce"""
  def __init__(self, bike_name, bike_weight, bike_produceCost):
  
    self.name = bike_name
    self.weight = bike_weight
    self.cost = bike_produceCost
    
   
class Shops():
  """Stores Shop name, inventory, margin and profit"""
  def __init__(self, shop_name, shop_inventory, shop_margin, shop_profit):
    
    self.shopName = shop_name
    self.inventory = shop_inventory
    self.margin = shop_margin
    self.profit = shop_profit
    
    
    
class Customers():
  """Store customer name, funds and purchase power"""
  def __init__(self, customer_name, customer_money, customer_buy):
    
    self.customerName = customer_name
    self.money = customer_money
    self.buy = customer_buy
