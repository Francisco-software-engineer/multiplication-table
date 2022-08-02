import math

def print_tabuada(select_tabuada):
    for tab in range(1, 11):
        produto = math.prod([tab, int(select_tabuada)])        
        print(f"{tab} X {select_tabuada}  =", produto)