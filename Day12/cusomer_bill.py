val1 = "type:telecom|price:$500|name:hari|area:Kukatpally|country:India|state:Telangana|city:Hyderabad|pincode:500072"
val2 = "price:$800|name:hari|area:Kukatpally|country:India|state:Telangana|city:Hyderabad|pincode:500072"

def bill_of_customer(*args):
    for val in args:
        if val.split(':')[0] == 'price':
            print(val)

bill_of_customer(*val1.split('|'))
bill_of_customer(*val2.split('|'))