import hashlib

def md5(s):
    return hashlib.md5(str(s).encode('utf-8')).hexdigest()
    
def main(s):
    for i in range(1, 99999999):
        if md5(i)[0:6] == str(s):
            print(i)
            exit()

if __name__ == '__main__':
    main('4c4efa')