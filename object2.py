#!/usr/bin/env python3


subs = {
    "sandwich_type":"pastrami",
    "sandwich_price":"5.00",
    "sandwich_condiments":"mustard_mayo",
    "sandwich_seasoning":"salt_pepper",
    
    
},
{
    "sandwich_type":"italian",
    "sandwich_price":"6.00",
    "sandwich_condiments":"vinvinaigrette",
    "sandwich_seasoning":"salt_pepper_garlic_salt",
},
{
    "sandwich_type":"turkey_avacado",
    "sandwich_price":"7.00",
    "sandwich_condiments":"chipotle_sauce",
    "sandwich_seasoning":"salt_pepper_red_pepper",    
     
},  
{
    "sandwich_type":"meatball",
    "sandwich_price":"4.99",
    "sandwich_condiments":"marinara_sauce",
    "sandwich_seasoning":"basil_parsley",    
     
},  
{
    "sandwich_type":"hot_roastbeef",
    "sandwich_price":"8.50",
    "sandwich_condiments":"au_jus_dipping_sauce",
    "sandwich_seasoning":"black_pepper",    
     
},  


for item in subs:
    if item['sandwich_seasoning'] == "salt_pepper":
        print(item)
