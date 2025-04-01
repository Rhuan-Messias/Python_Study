#Consider an algorithm that takes as input a positive
#integer n. If n is even, the algorithm divides it by 
#three and adds one. The algorithm repeats this, until
#n is one. For example, the sequence for n = 3 is as 
#follows
#3 -> 10 -> 5 -> 16 -> 8-> 4 -> 2 -> 1
# output must be a line containing all the numbers during the algorithm 
integer = int(input("Type a number: "))
integer_list = [integer]

while integer != 1:
    if integer%2 == 0:
        integer = integer/2
        
    else:
        integer = integer*3+1
    
    integer_list.append(integer)

print(integer_list)