numbers = [2,4,6,8]

def add_list():
    add = 0
    for number in numbers:
        add += number
    return(add)



def multiply_list():
    product = 1
    for number in numbers:
        product *= number
    return(product)
        
print(add_list())
print(multiply_list())
    