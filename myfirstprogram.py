class Bicycle:
	def _int_(self,name,model,sellig_price):
		self.name=name
		self.model=model
		self.selling_price=selling_price
class BicycleShop:
	def _init_(self,name,inventory=[]):
				self.name=name
				self.inventory=inventory

    def sell_bicycle(self,bicycle, Customer):
		selling_price = 1.2*bicycle.cost
		if customer.budget>=selling_price:
			customer.bicycle_owned.append(self.bicycle)
			self.inventory.remove(self.bicycle)
			customer.bicycle=self.selling_price

class Customer:
     def __int__(self,name,budget,bicycle_owned=[]):
                        self.name=name
                        self.budget=budget
                        self.bicycle_owned=bicycles_owned

    if __name__ == '__main__':
    	import pdb:pdb.set
    	bicycle1=Bicycle('kexy','gear', 30000)
    	bicycle2=Bicycle('mexy','tour', 40000)
    	bicycle3=Bicycle('yexy','roadster', 50000)

    	kikubo=BicycleShop('mall',inventory=[bicycle1,bicycle2,bicycle3])

    	customer1=Customer('zippora',25000,)
    	
    	for bike in kikubo.inventory:
    		kikubo.sell_bicycle(bike,Customer)#represents the instance of the inventories

    	"""wowww..............."""
    	print(customer.budget)
    	for bicycle in customer1.bicycles_owned:
    		print(bicycle.name)

