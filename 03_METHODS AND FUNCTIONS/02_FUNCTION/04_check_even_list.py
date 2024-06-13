''' ** Wrong Approach ** '''
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # This is WRONG! This returns False at the very first odd number!
        # It doesn't end up checking the other numbers in the list!
        else:
            return False
# UH OH! It is returning False after hitting the first 1
print(check_even_list([1,2,3]))

''' ** Correct Approach: We need to initiate a return False AFTER running through the entire loop** '''

def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return False

print(check_even_list([2,4,6]))