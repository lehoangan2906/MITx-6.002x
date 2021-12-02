class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    
    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue() / self.getCost()
    
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'
    

def buildMenu(names, values, calories):
    """
        names, values, calories are lists of same length
        name is a list of strings
        values and calories are lists of numbers
        returns list of Foods
    """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
        
    return menu

# implementation of Flexible Greedy

def greedy(items, maxCost, keyFunction):
    """
    Assumes items is a list, maxCost >= 0
    keyFunction maps elements of items to numbers
    """
    itemsCopy = sorted(items, key = keyFunction, reverse = True)    # O(nlogn) where n is len(items)
    result = []
    totalValue, totalCost = 0.0, 0.0
    
    for i in range(len(itemsCopy)):     # O(n) where n is len(itemsCopy)
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)
    # total: O(nlogn + n) = O(nlogn)
    
    
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken = ', val)
    for item in taken:
        print('  ', item)
        
def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    
    print('\nUse greedy by cost to allocate ', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    
    print("\nUse greedy by density to allocate ", maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)
    
    
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)


"""
note:

    Python sorted() function returns a sorted list from the iterable object.

    Sorted() sorts any sequence (list, tuple) and always returns a list with the 
    elements in a sorted manner, without modifying the original sequence.
    
    syntax: sorted(iterable, key, reverse)
    
    Parameters: sorted takes three parameters from which two are optional. 

    Iterable : sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted.
    Key(optional) : A function that would server as a key or a basis of sort comparison.
    Reverse(optional) : If set true, then the iterable would be sorted in reverse (descending) order, by default it is set as false.
    
    sorted() function has an optional parameter called ‘key’ which takes a function as its value. This key function transforms each 
    element before sorting, it takes the value and returns 1 value which is then used within sort instead of the original value. 
    For example, if we pass a list of strings in sorted(), it gets sorted alphabetically. But if we specify key = len, i.e. give len 
    function as key, then the strings would be passed to len, and the value it returns, i.e. the length of strings will be sorted. 
    Which means that the strings would be sorted based on their lengths instead
    
    """