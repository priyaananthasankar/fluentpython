from collections import deque
import os

# deque with a limit is useful as once the
# deque is full, stuff is popped out and it maintains a constant size

# Generalization of stacks and queues

def get_last(filename, n=3):
    try:
        print(os.getcwd())
        with open(filename) as f:
            return deque(f,n)
    except OSError:
        print("Error opening file: {}".format(filename))
        raise

print(get_last("collections/loremipsum.txt"))


# General purpose deque stuff

d = deque(list('superfluous'))
d.appendleft("woman")
d.append("super")
d.rotate(1)
print(d)
d.rotate(-1)
print(d)