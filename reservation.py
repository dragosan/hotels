

class Reservation:

    """ create a reservation and adding it to the list as names of
     customer and hotel"""

    reservations_list=[]
    message=''

    def __init__(self,customer,hotel):
        self.customer=customer
        self.hotel=hotel

        Reservation.reservations_list.append([self.customer,self.hotel])       




    
#using classes
##    def __init__(self,customer,hotel):
##        self.customer=customer
##        self.hotel=hotel
##
##        Reservation.reservations_list.append([self.customer,self.hotel])


        



    


##    @classmethod
##    def return_res_list():
##                
##        return Reservation.reservations_list

##    def test():
##        return 2


    # something wrong here 
    def find_reservation(self,customer,hotel):
        for res in Reservation.reservations_list:
            
            if(type(self.customer is res[0]) and type(self.hotel is res[1])):
                return 'reservation found'
        return 'reservation not found'
    


    

        
        
    
