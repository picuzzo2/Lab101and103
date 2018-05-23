#600510532 SEC1

def main():
    line = input()
    print(uniform(line))

def uniform(line):
    upper = 0
    lower = 0
    for letter in line:
        if letter.islower():
            lower+=1
        elif letter.isupper():
            upper+=1
    if upper < lower:
        result = line.lower()
    elif lower < upper:
        result = line.upper()
    else:
        if line[0].isupper():
            result = line.upper()
        else:
            result = line.lower()
    return result
if __name__ == '__main__':
    main()
