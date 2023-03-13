# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a,b=input().split()
for i in list (list(permutations(sorted(a),int(b)))):
    print(''.join(i))
