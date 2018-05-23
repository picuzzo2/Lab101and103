

def main():
    y = int(input())
    leap=kuy(y)
    print(leap)

def kuy(y):
    y=y
    def leap_year(y):
        if y % 4 == 0:
            year = 0
        if y % 4 == 1:
            year = 1
        return year
    year = leap_year(y+1)
    return year 


if __name__ == '__main__':
    main()