from Numbers import Numbers


require_once = "Numbers.py"
numbers = Numbers()
numbers.add(42)
numbers.add(100)
numbers.add(5)
print(str(numbers.get()) + str(),end="")
numbers.add(256)
print(str(numbers.get()) + str(),end="")
if (numbers.exists(2)) :
    print("Máme :)",end="")
else : 
    print("Nemáme :(",end="")