#!/usr/bin/env python3

def print_fibonacci(length):
    if length==0:
        print([])
        return
    elif length==1:
        print([0])
        return
    else:
        starting_sequence=[0,1]
        while len(starting_sequence)<length:
            next_number=starting_sequence[-1]+starting_sequence[-2]
            starting_sequence.append(next_number)
        print(starting_sequence)