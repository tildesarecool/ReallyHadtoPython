def purchase(price, money_available):

    balance = float(money_available - price)
    try:        
        if balance >= 0:
            print(f"under try balance is {balance}")
            return balance
        else:
            print(f"under else, balance is {balance}")
            raise Exception("not enough money")
            return "not enough money"
            #return balance
            #return 
        
    except:
        print(f"under except, balance is {balance}")
        return "not enough money"
        pass
        
        
        ##if balance > 0:
        #
        #raise Exception("not enough money")
        #
            
#    pass
