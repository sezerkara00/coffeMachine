WATER = 890
MILK = 2450
COFFEE = 200
MONEY = 0


kahveler = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.5,
    },

    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5,
    },

    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0,
    }
}


def report():
    print()
    print("-"*20)
    print(f"Water: {WATER}ml")
    print(f"Milk: {MILK}ml")
    print(f"Coffee: {COFFEE}g")
    print(f"Money: ${MONEY}")
    print("-"*20)
    print()

def make_coffee(secim):
    global WATER, MILK, COFFEE, MONEY
    WATER -= kahveler[secim]["water"]
    MILK -= kahveler[secim]["milk"]
    COFFEE -= kahveler[secim]["coffee"]
    MONEY += kahveler[secim]["cost"]
    report()

def check_resources(secim):
    if WATER < kahveler[secim]["water"]:
        print("Sorry, there is not enough water.")
        return False
    elif MILK < kahveler[secim]["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    elif COFFEE < kahveler[secim]["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    return True

def para_odeme():
    odenen = 0
    para_birimleri = {
        "1": ("ceyrek", 0.25),
        "2": ("on cent", 0.10),
        "3": ("5 cent", 0.05),
        "4": ("1 cent", 0.01),
        "5": ("1 dolar", 1.00)
    }
    
    while True:
        # Para seçeneklerini göster
        for secim, (isim, miktar) in para_birimleri.items():
            print(f"{isim}({miktar:.2f}): {secim}")
        print("Devam etmek icin 6")
        
        secim_para = input("Odeme yapiniz: ")
        
        if secim_para == "6":
            print(f"Toplam odenen para: ${odenen:.2f}")
            break
        elif secim_para in para_birimleri:
            odenen += para_birimleri[secim_para][1]
        else:
            print("Invalid input. Please try again.")
            
    return odenen

while True:
    secim = input("What would you like? (espresso/latte/cappuccino): ")

    if secim == "espresso" or secim == "latte" or secim == "cappuccino":
        if check_resources(secim):
            print(f"Here is your {secim}. Enjoy!")
            print(f"Odenecek miktar: ${kahveler[secim]['cost']}")
            odenen = para_odeme()
            if odenen >=kahveler[secim]["cost"]:
                para_ustu = odenen - kahveler[secim]["cost"]
                print(f"Odeme basarili. Para ustu: ${para_ustu:.2f}")
                make_coffee(secim)
            else:
                print("Odeme basarisiz")
        else:
            print("Sorry, there is not enough resources.")

    elif secim == "report":
        report()

    elif secim == "off":
        break

    else:
        print("Invalid input. Please try again.")

