#task9-10
from restaurant import IcreamStand

    
icecream_1 = IcreamStand("Yum", "Ice Cream")
icecream_1.show_flavours()
icecream_1.show_number_served()

icecream_1.set_number_served(10)
icecream_1.show_number_served()

icecream_1.increment_number_served(35)
icecream_1.show_number_served()