def main():
    print(permute('Cat'))

def permute(word):
    if not word:
        return [word] 
    else:
        temp = []
        for i in range(len(word)):
            part = word[:i] + word[i+1:]
            
            for j in permute(part):
                temp.append(word[i:i+1] + j)

        return list(set(temp))

if __name__ == '__main__':
    main()