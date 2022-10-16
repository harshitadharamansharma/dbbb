# abhishek's earlier Models are on based other Old versions of ER did some alterations
#did some aterations

from email.headerregistry import Address
from email.mime import image
from ssl import VERIFY_CRL_CHECK_LEAF
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 122)
    phone =  models.CharField(max_length= 122)
    email =  models.CharField(max_length = 12)
    text =  models.TextField()
    def __str__(self):
        return self.name
    
class Donator(models.Model):
    Donator_Id = models.IntegerField(primary_key=True,null=False)
    Don_Name = models.CharField(max_length = 100)
    Donator_Type =  models.CharField(max_length = 100) # Individual/ Society/ office #will choose from option 1 , 2, 3
    Don_ph_no = models.CharField(max_length = 20)  # phone no should always in varchar ie CharField
    Don_Address = models.CharField(max_length = 100)   #sub_attributes:- line1, lin2 , district, Pin (subtree)   #as per the fields sneha made in the donator form

    Don_Email = models.CharField(max_length = 50)
    Don_location = models.CharField(max_length = 100)   
    Don_Ver_Proof = models.IntegerField() # valid Aadhaar # not using right now? 

    # Ewaste_Id = models.ForeignKey()
    
class Collector(models.Model):
    JC_Id = models.IntegerField(primary_key=True,null=False)
    JC_Name = models.CharField(max_length = 100)
    JC_ph_no = models.CharField(max_length = 20)
    JC_Address = models.CharField(max_length = 100)
    JC_Email = models.CharField(max_length = 50)
    JC_Location = models.CharField(max_length = 100)
    JC_Ver_Proof =  models.IntegerField()   # valid Aadhaar # not using right now? 
    JC_Vehicle = models.CharField(max_length = 100)
    JC_Vehicle_Type = models.CharField(max_length = 100) #cycle;truck;cycle  --> can contain moe than 1 value
     
     # Ewaste_Id = models.ForeignKey()   Not Using it

class Dealer(models.Model):
    JD_Id =  models.IntegerField(primary_key=True,null=False)
    JD_Name = models.CharField(max_length = 100)
    JD_ph_no = models.CharField(max_length = 20)
    JD_Address = models.CharField(max_length = 100)
    JD_Email = models.CharField(max_length = 50)
    JD_Location = models.CharField(max_length = 100)
    JD_Ver_Proof =  models.IntegerField()
    JD_Vehicle = models.CharField(max_length = 100)
    JD_Location_Shop = models.CharField(max_length = 100) #
    JD_Shop_Regno = models.CharField(max_length = 100)
    
    # Ewaste_Id = models.ForeignKey() #remove this

class Recycle_Plant(models.Model):
    RP_Id =  models.IntegerField(primary_key=True,null=False)
    RP_Name =  models.CharField(max_length = 100)
    RP_ph_no =  models.CharField(max_length = 100)
    RP_Adress =  models.CharField(max_length = 100)
    RP_Email =  models.CharField(max_length = 100)
    RP_Location =  models.CharField(max_length = 100)
    RP_Ver_Proof = models.IntegerField()
    RP_Vehicle =  models.CharField(max_length = 100)
   # RP_Location =  models.CharField(max_length = 100)

class Ewaste(models.Model):
    Ewaste_Id = models.IntegerField(primary_key=True,null=False)
    Name = models.CharField(max_length = 100)
    # Dimensions = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 100)
    Qty = models.IntegerField(max_lenght= 1000 )
    Size = models.CharField(max_length = 100)
    Weight = models.CharField(max_length = 100)
    image01_St0 = models.ForeignKey()  # from donor form as sneha created                       # models.CharField(max_length=2083) #2083=ideal url lenght
    image02_St0 = models.ForeignKey()                          # models.CharField(max_length=2083) #2083=ideal url lenght
    image03_St0 = models.ForeignKey()                          # models.CharField(max_length=2083) #2083=ideal url lenght
    Donator_Id =models.ForeignKey()
    Booking_Id_St0 =  models.ForeignKey()         # models.CharField(max_length=20)
    JC_Id =models.ForeignKey()
    Booking_Id_St1 = models.ForeignKey()       # these foriegn key values ideally should not be null; but we neesd to keep degfault value null as if it gets dismentalled in between (before reaching to the plant ) 
    JD_Id = models.ForeignKey()
    Booking_Id_St2 = models.ForeignKey()
    RP_Id = models.ForeignKey()
    Ewaste_Status = models.CharField(max_length = 20)   # 12 status decided

# pickup booking is same as the donor form wi=hich sneha created 
# bcz most of the data will get stored at the time of filling the pickup form
# ideally it should be link this 
class Pickup_Schedule_St0(models.Model):
     Booking_Id_St0 =  models.IntegerField(primary_key=True,null=False)
     Pickup_loc_St0 = models.CharField(max_length = 100)
     image01_St0 = models.CharField(max_length=2083) #2083=ideal url length
     image02_St0 = models.CharField(max_length=2083) #2083=ideal url lenght
     image03_St0 = models.CharField(max_length=2083) #2083=ideal url lenght
     Booking_Status_St0 =  models.CharField(max_length = 20)
    # Startof_pickup_St0 = models.CharField(max_length = 100)
    # Endof_Pickup_St0 = models.CharField(max_length = 100)
     Collectioncomplete_time_St0 = models.DateTimeField()
     St0_request_status = models.CharField(max_length=20)  #acccepted,denied,booked....

#other models should be Pickup_Schedule_St1; Pickup_Schedule_St2 :- refers to the booking happens between cololedctor and dealer; and then dealer to rp

   # and other tabes in the er are the tuples ; drop down values 
     #______________________

     #present models in the project:- 
     # or thwere might be slight changes as per the latest model idk


        # where is the login form model 
        # hello , is it there

from math import degrees
from django.db import models
from django.contrib.auth.forms import User

class extendeduser(models.Model):
     name = models.CharField(max_length=20)
     aadhaar_no = models.CharField(max_length=20, null = True)
     email =  models.CharField(max_length = 12,null= True)
     password = models.CharField(max_length = 20,null = True)
     username = models.CharField(max_length = 20,null = True)
     def __str__(self):
        return self.username

class Donor_form(models.Model):
    email =models.CharField(max_length = 122)
    address1=models.CharField(max_length= 122)
    address2 = models.CharField(max_length = 122)
    district = models.CharField(max_length = 122)
    city = models.CharField(max_length = 122)
    state = models.CharField(max_length = 122)
    pincode = models.CharField(max_length = 122)
    contact_no =models.CharField(max_length = 12)
    size = models.CharField(max_length = 122)
    quantity = models.CharField(max_length = 122)
    date_s = models.CharField(max_length = 122)
    time = models.CharField(max_length = 122)
    e_img = models.FileField(upload_to='', storage=None, max_length=100)
    date = models.DateField()


# error possibilities ; - header libraries import
                      # - datatype 