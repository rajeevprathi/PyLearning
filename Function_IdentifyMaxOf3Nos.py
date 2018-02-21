def max_of_three(first_number,second_number,third_number):
    if first_number > second_number > third_number:
        return(first_number)
        
    if second_number > third_number > first_number:
        return(second_number)
    
    return(third_number)
    
print(max_of_three(19,7,20))

    