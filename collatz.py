"""
Created on Mon Oct 15 23:29:42 2018

@author: andrewkrier
"""

def test_collatz(num, tested):
    if num in tested: # Checks if value has already been checked
        print('Testing: {}'.format(num))
        print('{} failed'.format(num))
        return 0
    else:
        print('Testing: {}'.format(num))
        while (num != 1) and (num not in tested):
            num = iterate_collatz(num)
            #print(num)
        print('{} failed'.format(num))
        return 0
    
def iterate_collatz(num):
    if num % 2 == 0:
        return int(num / 2)
    else:
        return 3 * num + 1
    
if __name__ == '__main__': # If this code ever stalls at any number, the number is a counterexample
    tested = []
    for k in range(0, 100000): # The in functon approaches O(N)
        test_collatz(k + 1, tested)
        tested += [k + 1] # Add the value to array of already tested