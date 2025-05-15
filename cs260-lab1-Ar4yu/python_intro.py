'''
Description: intro to python code
Author: Aaryaman Jaising
Date: January 21, 2025
'''

# TODO add imports here
import random

################################################################################
# MAIN
################################################################################

def main():
    '''
    Test each function with representative examples.
    '''
    # Test movie_ticket_cost
    print("Testing movie_ticket_cost:")
    movie_ticket_cost()  # Run interactively

    # Test shuffle functions
    print("\nTesting shuffle_in_place and shuffle_out_of_place:")
    lst = [1, 2, 3, 4, 5]
    print("Original list:", lst)
    shuffle_in_place(lst)
    print("In-place shuffled list:", lst)

    lst = [1, 2, 3, 4, 5]
    print("Original list:", lst)
    shuffled_lst = shuffle_out_of_place(lst)
    print("Out-of-place shuffled list:", shuffled_lst)
    print("Original list after out-of-place shuffle:", lst)

    # Test Fibonacci function
    print("\nTesting Fibonacci function:")
    for i in range(10):
        print(f"fib({i}) =", fib(i))

    # Test binary search
    print("\nTesting binary search:")
    sorted_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Recursive binary search for 5:", binary_search_r(5, sorted_lst))
    print("Recursive binary search for 11:", binary_search_r(11, sorted_lst))
    print("Non-recursive binary search for 5:", binary_search_nr(5, sorted_lst))
    print("Non-recursive binary search for 11:", binary_search_nr(11, sorted_lst))
    pass

################################################################################
# FUNCTIONS
################################################################################

def movie_ticket_cost():
    '''
    Take age of individual and return cost of movie ticket accordingly
    Author: Aaryaman Jaising
    Date: 21 Jan, 2025
    '''
    age = int(input("Enter age: "))
    price = 0
    if age>=0 and age<=12:
        price = 8
    elif age>=13 and age<=64:
        price = 12
    elif age>=65:
        price = 8
    if price==0:
        print("Invalid age!")
    else:
        print(f"Ticket price is : ${price}")
    pass


def shuffle_in_place(lst):
    '''
    Uses rand function to make swaps in place for shuffling
    lst: input list to shuffle
    returns nothing
    Author: Aaryaman Jaising
    Date 01/21/2025
    '''
    for i in range(len(lst)):
        cur = random.randrange(len(lst))
        tmp = lst[cur]
        lst[cur] = lst[i]
        lst[i] = tmp
    pass

def shuffle_out_of_place(lst):
    '''
    Copies list and then uses rand function to make swaps in place for shuffling
    lst: input lst to shuffle
    return: seperate list that has been shuffled
    Author: Aaryaman Jaising
    Date 01/21/2025
    '''
    lst2 = lst.copy()
    for i in range(len(lst2)):
        cur = random.randrange(len(lst2))
        tmp = lst2[cur]
        lst2[cur] = lst2[i]
        lst2[i] = tmp

    return lst2

def fib(n):
    '''
    Calculates nth fibonacci number recursively
    n: non negative integer
    return: nth fibonacci number
    Author: Aaryaman Jaising
    Date 01/21/2025
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

def binary_search_r(query, lst,l=-1,r=-1): # recursive version
    '''
    Binary search recursively
    query: value being searched for
    lst: sorted list to search through
    returns index of element found or -1 if not found.
    Author: Aaryaman Jaising
    Date 01/21/2025
    '''
    if l==-1 and r==-1:
        l = 0
        r = len(lst)-1
    if l>r:
        return -1
    else:
        m = int((l+r)/2)
        if lst[m] == query:
            return m
        elif lst[m] > query:
            r = m-1
            return binary_search_r(query, lst,l,r)
        else:
            l = m+1
            return binary_search_r(query, lst,l,r)

def binary_search_nr(query, lst): # non-recursive version
    '''
    Binary search non recursively
    query: value being searched for
    lst: sorted list to search through
    returns index of element found or -1 if not found.
    Author: Aaryaman Jaising
    Date 01/21/2025
    '''
    l,r = 0,len(lst)-1
    while l<=r:
        m = int((l+r)/2)
        if lst[m] == query:
            return m
        elif query > lst[m]:
            l = m+1
        else:
            r = m-1
    return -1

if __name__ == "__main__":
    main()
