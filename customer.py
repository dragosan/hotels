class Customer:

    """ create an instance of class customer and add it to list customers"""

    customers=[]

    def __init__(self,customer_number,customer_name):
        self.customer_number=customer_number
        self.customer_name=customer_name

        Customer.customers.append([self.customer_number,self.customer_name])


    def find_customer(self):
        for cust in Customer.customers:
            if(self.customer_name in cust):
                return True
        return False


    def delete_customer(self):
        for cust in Customer.customers:
            if(self.customer_name in cust):
                Customer.customers.remove(cust)

    def display_name(self):
        return self.customer_name


