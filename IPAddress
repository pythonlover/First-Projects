def addresses():
    c = 0
    list = []
    while c <= 255:
        ip = '192.168.0.%d' %c
        c += 1
        list.append(ip)
    return list
    
def text(list):
    list = list
    file = open('IP List.txt', 'w')
    for address in list:
        file.write(address + '\n')
        
def main():
    list = addresses()
    text(list)
        
if __name__ == '__main__':
    main()
