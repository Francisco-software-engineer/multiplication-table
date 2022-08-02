import argparse
import math

def print_tabuada(select_tabuada):
    for tab in range(1, 11):
        produto = math.prod([tab, int(select_tabuada)])        
        print(f"{tab} X {select_tabuada}  =", produto)

def main():
    kwargs = {}
    parser = argparse.ArgumentParser()

    parser.add_argument("select_tabuada", help="Insira o número da tabuada que deseja")
    args = parser.parse_args()
    
    kwargs = vars(args)

    print_tabuada(**kwargs)


if __name__ == '__main__':
    main()
