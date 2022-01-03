file = open('file.txt')
try:
    n = int(input())
    for i in range(n):
        print(file.readline().strip())
except Exception:
    print('Please enter an integer')
