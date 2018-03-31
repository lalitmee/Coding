import atexit
import io
import sys
 
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
 
 
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
 
T = int(input())
for  i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Alice = sum(A) - max(A)
    Bob = sum(B) - max(B)
    if Alice < Bob:
        print("Alice")
    elif Alice == Bob:
        print("Draw")
    else:
        print("Bob")