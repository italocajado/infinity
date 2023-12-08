divi = int(input("qual o dividendo: "))
divisor = int(input("qual o divisior: "))

def veri(divi, divisior):
    count = 0
    if divi < divisior:
        print("invalido")
    while divi % divisior  == 0:
        count += 1
        divi //= divisior
    return count

result = veri(divi, divisor)
print(result)
