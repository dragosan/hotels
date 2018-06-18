
import hotel
import customer
import reservation
import notification


# create  hotels and add them to hotels list 

rotana_hotel=hotel.Hotel(20,'Rotana','Cairo',200,30)
sheraton_hotel=hotel.Hotel(20,'Sheraton','Alex',300,40)
ramsis_hotel=hotel.Hotel(7,'Ramsis','Cairo',433,32)


# create customers and add them to list customers
hassan=customer.Customer(5,'hassan')
alaa=customer.Customer(6,'alaa')
ahmed=customer.Customer(5,'ahmed')

#create reservations and add them to list
hassan_rotana=reservation.Reservation(hassan,rotana_hotel)
alaa_sheraton=reservation.Reservation(alaa,sheraton_hotel)
ahmed_ramsis=reservation.Reservation(ahmed,ramsis_hotel)

def start_app():    

    print ' test hotel class : '
    print '-----------------------------'
    print " List of Hotels : "
    print hotel.Hotel.hotels

    print

    print " look if hotel in list : "
    if(sheraton_hotel.find_hotel()):
        print(" hotel found in list")

    print ' List of Hotels : '
    print rotana_hotel.list_hotels()
    print
    print 'list of hotels in a city : '
    print rotana_hotel.list_hotels_in_city('Cairo')
    


    print " delete one hotel from hotel list : "
    sheraton_hotel.delete_hotel()
    
    print " List of Hotels after deleting one hotel : "
    print hotel.Hotel.hotels
    print '_________________________________'
    


start_app()



def cust_operations():
    
    print ' test cusomer class '
    print 
    print "customers list after adding customers : "
    print customer.Customer.customers

    print alaa.find_customer()

    print " customers list after remove item :"
    alaa.delete_customer()
    print customer.Customer.customers
    print '_______________________________________'

cust_operations()



def find_reservation(res_list,customer,hotel):
    
    for res in res_list:
        if(res[0]==customer):
            if(res[1]==hotel):
                return 'reservation with this customer in this hotel found'
    return 'no reservation for this customer exist'

print ' test reservation class '
print find_reservation(reservation.Reservation.reservations_list,hassan,rotana_hotel)
print find_reservation(reservation.Reservation.reservations_list,ahmed,rotana_hotel)
print find_reservation(reservation.Reservation.reservations_list,hassan,ramsis_hotel)

#send message to client
notification.Notification('rotana','hassan')

# should change it to class method
##print 'test '
##
##for res in reservation.Reservation.reservations_list:
##    print res[0],res[1]









