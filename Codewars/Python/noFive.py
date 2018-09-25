# Its mine Solution
def dont_give_me_five(start,end):
    arr = []
    num = start
    for i in range(start, end + 1):
        if num % 5 != 0 or num % 2 == 0:
            arr.append(num)
        num += 1
    n = len(arr)
    return n   # amount of numbers

#==================================
# Number 1 Solution according to upvotes
def dont_give_me_five(start, end):
    return sum('5' not in str(i) for i in range(start, end + 1))
#==================================


#==================================
# Number 2 Solution according to upvotes
def dont_give_me_five(start,end):
    return len([num for num in range(start, end+1) if '5' not in str(num)])
#==================================

#==================================
# Easy and simple to understand
def dont_give_me_five(start,end):
    tick = 0
    for x in range(start, end+1):
        if '5' not in str(x):
            tick += 1
    print(tick)
    return tick
#==================================

dont_give_me_five(104, 148)
