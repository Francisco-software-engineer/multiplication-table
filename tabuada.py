import argparse
import math

def print_table(select_table):
    for tab in range(1, 11):
        produto = math.prod([tab, int(select_table)])        
        print(f"{tab} X {select_table}  =", produto)

def main():
    kwargs = {}
    parser = argparse.ArgumentParser()

    parser.add_argument("select_table", help="Insert the wished number")
    args = parser.parse_args()
    
    kwargs = vars(args)

    print_table(**kwargs)


if __name__ == '__main__':
    main()
