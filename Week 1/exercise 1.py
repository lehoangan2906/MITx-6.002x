import random

# generate all combinations of N items

def powerSet(items):
    N = len(items)
    #enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            #test bit jth of integer i
            if (i >> j) % 2 == 1:   # same as i//(2**j) = 1
                combo.append(items[j])
        yield combo
        
"""
So what does the code says ? First, it iterates through all 2**N possible combinations (possible binary numbers) Second, for each combination of them (represented in its binary form) check for the 1's inside the number and add the corresponding items to the combo list. But how does it do it ? In a very smart way.

The shift operator >> shifts all digits to the right X times, where X is the number on the right of the >> operator. For example, 8 (which is equal to 1000) >> 1, will shift the 4 digits 1 step to the right to be (0100) which is equal to 4. Even numbers in binary always have 0 as the first digit on the right whereas odd numbers have 1 as the first number on the right. So, 8 (1000) has 0 on the right .. when we shift it right by 1 .. 4(0100) has 0 on the right, 2(0010) has 0 on the right .. 1(0001) has 1 on the right. So, if we check if the number is odd or not, we can know if there is 1 on the right or not.

Using this idea, the code tries to shift each different combination by numbers from 0 to N, each time it checks if it's odd or not by checking if there's a remainder of 1 (if (i >> j) % 2 == 1) .. if so, then the number of times we shifted the current combination (j in this case) is the original position of the 1 in the combination .. which we can use as an index for the corresponding item we want to take.

So if the current combination is 1000 (8) and by shifting it 3 times to the right we have 0001 which is odd, we know that 1 in 1000 is the 3rd bit (starting from 0 from the right to the left). if the list of items are [rice, meat, egg, juice] then items[3] is juice.

So, for each different combination, we use the binary representation of that combination and use the previous method to search for the 1's in the number and add the corresponding items to the list of the items to be taken.

It's quite long and complex especially for those who never got exposed to binary numbers before .. but this is the trick.

"""
 
 
"""
As above, suppose we have a generator that returns every combination of objects in one bag. 
We can represent this as a list of 1s and 0s denoting whether each item is in the bag or not.

Write a generator that returns every arrangement of items such that each is in one or none of 
two different bags. Each combination should be given as a tuple of two lists, the first being 
the items in bag1, and the second being the items in bag2.
"""
 
        
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    #enumerate over 3**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # Dividing by 3**j removes the last j digits in base 3, and n % 3 is the last digit of n in base 3.
            if (i // 3**j) % 3 == 0:
                bag1.append(items[j])
            elif (i // 3**j) % 3 == 1:
                bag2.append(items[j])
        yield (bag1, bag2)
                
"""
>>> 12345 % 10
5
>>> 12345 // 10
1234
>>> (12345 // 10) % 10
4
>>> 12345 // 10**2
123
>>> (12345 // 10**2) % 10
3
>>> (12345 // 10**3) % 10
2
>>> (12345 // 10**4) % 10
1
Dividing by b**k removes the last k digits in base b, and n % b is the last digit of n in base b.
"""
 
 
 
                
# ====================================================================================================
# tester

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'


def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]
    

def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))for i in range(n)]

items = buildItems()
combos = yieldAllCombos(items)