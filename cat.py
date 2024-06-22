#i = 1

#while i <= 3:
#    print("meow")
#    i += 1

#for i in [0,1,2]:
#    print("meow")

#for _ in range(3):
#    print("meow")

#print("meow\n" * 3, end="")

#n = int(input("What's n? "))
#while n <= 0:
#    n = int(input("What's n? "))
#print("meow\n" * n, end="")

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()