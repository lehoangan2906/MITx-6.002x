import random

class Food(object):
    def __init__ (self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    
    def getValue(self):
        return self.value

    def getCalories(self):
        return self.calories
    
    def density(self):
        return self.getValue() / self.getCalories()
    

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

def maxVal(toConsider, avail):
    """
    Assumes toConsider is a list of items, avail is a eight
    Returns a tuple of the total weight of a solution to the 
    0/1 knapsack problem and the items of that solution
   """
    if toConsider == [] or avail == 0:
       result = (0, ())
       
    elif toConsider[0].getCalories() > avail:
        # explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        
        # explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCalories())
        withVal += nextItem.getValue()
        
        # explore the right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        
        # choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def buildLargeMenu(numItems, maxVal, maxCalories):
    items = []
    for i in range(numItems):
        items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCalories)))
    return items

def fastMaxVal(toConsider, avail, memo = {}):
    """
    Assumes toConsider is a list of subjects,m avail is a weight, memo supplied by recursive valls
    Returns a tuple of the total value of a solution to the 0/1 knapsack problem and the subjects of that solution
    """
    if(len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
        
    elif toConsider == [] or avail == 0:
       result = (0, ())
       
    elif toConsider[0].getCalories() > avail:
        # explore right branch only
        result = fastMaxVal(toConsider[1:], avail)
        
    else:
        nextItem = toConsider[0]
        
        # explore left branch
        withVal, withToTake = fastMaxVal(toConsider[1:], avail - nextItem.getCalories()) 
        withVal += nextItem.getValue()
        
        # explore the right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail)
        
        # choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
        
    return result

def testMaxVal(foods, maxUnits, algorithm, printItems = True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print('   ', item)
            
for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, fastMaxVal, False)
    