# using a memo to compute fibonnaci
def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by 
    recursive calls"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result
        return result
    
for i in range(121):
    print("(fib " + str(i) + ") :" , fastFib(i))
    
"""
When Does Dynamic programming Work?
- Optimal substructure: a globally optimal solution can be found by combining optimal solutions to local subproblems
    + For x > 1, fib(x) = fib(x - 1) + fib(x – 2)
- Overlapping subproblems: finding an optimal solution involves solving the same problem multiple times 
    + Compute fib(x) or many times
"""