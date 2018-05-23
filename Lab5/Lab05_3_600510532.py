 แแแ  
# keattisak wongsathan
# 600510532
# Lab 05
# Problem 3
# 204111 SEC 001

def main():
    d,m,y = map(int,input().split())
    print(count_down_to_songkran(d,m,y))

def count_down_to_songkran(d, m, y):              #check leap year
    y=y
    def leap_year(y):
        if y % 4 == 0:
            if y % 400 == 0:
                return 29
            elif y % 100 == 0:
                return 28
            else:
                return 29
        else:
            return 28
    leap=leap_year(y)                   #use for this year fabr
    next_leap=leap_year(y+1)             #use for next year fabr

    def count_down(leap):              #cal from month to day
        if m==1:
            date=d
        if m==2:
            date=31+d
        if m==3:
            date=31+leap+d
        if m==4:
            date=31+leap+31+d
        if m==5:
            date=31+leap+31+30+d
        if m==6:
            date=31+leap+31+30+31+d
        if m==7:
            date=31+leap+31+30+31+30+d
        if m==8:
            date=31+leap+31+30+31+30+31+d
        if m==9:
            date=31+leap+31+30+31+30+31+31+d
        if m==10:
            date=31+leap+31+30+31+30+31+31+30+d
        if m==11:
            date=31+leap+31+30+31+30+31+31+30+31+d
        if m==12:
            date=31+leap+31+30+31+30+31+31+30+31+30+d
        return date
    date=count_down(leap)

    def past_songkran(date,leap,next_leap):                
        if date<=75+leap :                  #before songkran
            count_down=(31+leap+31+13)-date             #songkran - date
        if date>75+leap :                  #after songkran
            count_down=(31+leap+31+30+31+30+31+31+30+31+30+31)-(date)+(31+next_leap+31+13)  #year-date+songkran next year
        return count_down
    count_down=past_songkran(date,leap,next_leap)

    return count_down


    

if __name__ == '__main__':
    main()
