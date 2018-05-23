def main():
    list_x = [("11/1/1900", "Event A"), ("5/12/2001", "Event B"),
    ("5/12/2002", "Event C"), ("21/8/2008", "Event D"),
    ("9/3/2013", "Event E"), ("11/3/2017", "Event F"),
    ("7/5/2019", "Event G"), ("29/2/2032", "Event H"),
    ("9/11/2042", "Event I")]
    event = search_event(list_x, "29/02/2032")
    print("---")
    print(event)

def search_event(list_x,key):
    key = key.split('/')
    for i in range(len(key)):
        key[i] = int(key[i])
    for i in range(len(key)):
        key[i] = str(key[i])
    key= '/'.join(key)
    #print(key)

    dict = {}
    for i in range(len(list_x)):
        dict[list_x[i][0]] = list_x[i][1]

    try:
        result = (key,dict[key])
    except:
        result = None
    


    return result

if __name__ == '__main__':
    main()