import argparse
import math
import re

def print_table(select_table):
    for tab in range(1, 11):
        multiple = math.prod([tab, int(select_table)])        
        print(f"{tab} X {select_table}  =", multiple)

def log():
    print("Err: Insert a single number between 0 and 999")        

def sanitize(select_table):
    #Accept only positive integers in range (0 to 999)
    regExPattern = re.compile("^[1-9]?[0-9]?[0-9]$")
    return re.match(regExPattern, select_table) 

def main():
    kwargs = {}
    parser = argparse.ArgumentParser()

    parser.add_argument("select_table", help="Insert the wished number")
    args = parser.parse_args()
    
    kwargs = vars(args)

    if sanitize(**kwargs) :
        print_table(**kwargs)
    else:
        log()        


if __name__ == '__main__':
    main()
