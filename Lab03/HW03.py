def main():
    print(IP_encode('2', '3232237069'))
    print(IP_encode('1', '10.28.4.2'))
    print(IP_encode('1', '0.0.0.1'))
    print(IP_encode('2', '100'))
    print(IP_encode('2', '20729'))
    print(IP_encode('2', '16414'))
    print(IP_encode('2', '4876'))
    print(IP_encode('1', '168.14.250.72'))
    print(IP_encode('1', '160.13.245.99'))
    print(IP_encode('2', '31367'))
    print(IP_encode('1', '170.33.51.11'))
    print(IP_encode('1', '114.64.37.54'))
    print(IP_encode('1', '79.162.1.208'))
    print(IP_encode('2', '26899'))
    print(IP_encode('2', '4995'))
    print(IP_encode('2', '12789'))
    print(IP_encode('1', '215.80.54.75'))
    print(IP_encode('2', '10122'))

def IP_encode(mode,text):
    if mode == '1':
        return 1
    else:
        return 0
if __name__ == '__main__':
    main()