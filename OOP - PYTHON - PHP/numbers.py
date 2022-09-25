

from collections import OrderedDict

class Settlement :
    @staticmethod
    def default_key(d):
        result = 0
        for key, _ in d.items():

            if(type(key) is int and key >= result) :

                result = key + 1
        d[result] = OrderedDict()
        return result
    

class Numbers :

    numbers = None

    def __init__(this) :
        this.clear()
    
    def clear(this) :
        this.numbers = OrderedDict([])
    
    def add(this,int number) :
        k__1 = Settlement.default_key(this.numbers)
        this.numbers[k__1] = number
    
    def exists (this,int number) -> bool :
        for value in this.numbers.values() : 
            if (value == number) :
                return True
            
        
        return False
    
    def get(this) -> string :
        return implode(" ", this.numbers)

       