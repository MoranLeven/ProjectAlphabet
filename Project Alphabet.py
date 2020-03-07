string = input("Enter the alphabet whose pattern you wanna print on screen with its code\n")
if string =="A" or string == "a":
    for i in range(7):
        for j in range(5):
            if (i+j==2) or ((i>0 and i<3) and j-i==2)or((i>=3 and i<=6) and (j==0 or j==4)) or ((i==4 and j>=1) and j<4):
                print("@",end="")
            else:
                print(" ",end="")
        print()

elif string =="B" or string == "b":
    row = [1,2,4,5] # for different approach (maverick way)
    for i in range(7):
        for j in range(5):
            if (j==0 and (i<=6)) or ((j>=1 and j<=3) and i%3==0) or (j==4 and (i in row)):
                print("$",end="")
            else:
                print(" ",end="")
        print()

elif string == "C" or string =="c":
    for i in range(7):
        for j in range(5):
            row = [1,5]
            if (j==0 and (i>=1 and i<=5)) or ((j>=1 and j<=3) and (i%6==0)) or (j==4 and (i in row)):
                print("#",end="")
            else:
                print(" ",end="")
        print()
elif string =="D" or string=="d":
    for i in range(7):
        for j in range(5):
            row = [1,2,3,4,5]
            if (j==0 and (i<=6)) or ((j>=1 and j<=3) and (i%6==0)) or (j == 4 and (i in row)):
                print("%",end="")
            else:
                print(" ",end="")
        print()
elif string =='E' or string == 'e':
    for i in range(7):
        for j in range(5):
            if((j==0 and i<=6) or (i%3==0 and  (i in (0,6))) and (j<=4)) or (i==3 and j<=3):
                print("#",end="")
            else:
                print(" ",end="")
        print()
elif string =='F' or string == 'f':
    for i in range(7):
        for j in range(5):
            if(((i==0 and j<=4) or (j == 0 and i<=6))or(i==3 and j<=3)):
                print("#",end="")
            else:
                print(' ',end="")
        print()
elif string == 'G' or string == 'g':
    for i in range(7):
        for j in range(5):
            col = [1,4,5]
            if((j==0 and (i>=1 and i<=5)) or (i%6==0 and (j>=1 and j<=3)) or (j==4 and (i in col)) or (i==4 and (j==2 or j==3))):
                print("*",end='')
            else:
                print(" ",end="")
        print()
elif string == 'H' or string =='h':
    for i in range(7):
        for j in range(5):
            if((j%4==0 and i<=6) or (i==3 and j<=4)):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == 'I' or string == 'i':
    for i in range(7):
        for j in range(5):
            if((i%6==0 and j<=4) or (j==2 and i<=6)):
                print("*",end='')
            else:
                print(" ",end="")
        print()
elif string == "J" or string == "j":
    J = ''
    for i in range(7):
        for j in range(5):
            if((i==0 and j<=4) or (j==3 and i<=5) or (j==0 and (i==4 or i==5)) or (i==6 and (j==1 or j==2))):
                J = J + "*"
            else:
                J = J + " "
        J = J + '\n'
    print(J)
elif string == "K" or string == "k":
    k = ''
    for i in range(7):
        for j in range(5):
            if((j==0 and i<=6) or (i+j==4 or i-j==2)):
                k = k+'*'
            else:
                k = k+" "
        k = k + '\n'
    print(k)
elif string == 'L' or string == 'l':
    L = ''
    n = 7
    for i in range(n):
        for j in range(n):
            if((j == 0 and i<=n) or (i==n-1 and j<=n-2)):
                L = L + "*"
            else:
                L = L + " "
        L = L + '\n'
    print(L)

elif string == "M" or string == "m":
    col = [0,1,2]
    for i in range(5):
        for j in range(5):
            if((j%4==0 and i<=4)or((i in col) and (i==j or i+j==4))):
                print("*",end="")
            else:
                print(" ",end="")
        print()# half project done (*~~*)

elif string =="N" or string == "n":
    row = [1,2,3]
    for i in range(7):
        for j in range(5):
            if((j%4==0 and i<=4) or ((i in row) and (i==j))):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == "O" or string == 'o':
    for i in range(7):
        for j in range(5):
            if((j%4==0 and (i>=1 and i<=5)) or (i%6==0 and (j>=1 and j<=3))):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == 'P' or string == 'p':
    for i in range(7):
        for j in range(5):
            if((j==0 and i<=6) or (j<=2 and i/3 in [0,1]) or (j==3 and 1<=i<=2)):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == "Q" or string == 'q':
    for i in range(7):
        for j in range(5):
            if((j%3==0 and 1<=i<=4) or (i%5==0 and 1<=j<=2) or (i==6 and j==4)):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == "R" or string == "r":
    for i in range(7):
        for j in range(5):
            if((j==0 and i<=6) or (1<=j<=2 and i/3 in [0,1]) or (j==3 and 1<=i<=2) or ((4<=i<=6) and (i-j==3))):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string =="S" or string == "s":
    for i in range(7):
        for j in range(5):
            if((i%3==0 and 1<=j<=3) or ((i in [1,2,5]) and (j==0)) or ((i in [1,4,5]) and j==4)):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == 'T' or string == 't':
    for i in range(7):
        for j in range(5):
            if((i==0 and j<=4) or (j==2 and i<=4)):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == "U" or string == "u":
    for i in range(7):
        for j in range(5):
            if((j%4==0 and i<=4) or (i==5 and 1<=j<=3)):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == 'V' or string == 'v':
    for i in range(7):
        for j in range(5):
            if((j%4==0 and i<=4) or ((i in [5,6]) and (i-j==4)) or (j==3 and i==5)):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == 'W' or string == 'w':
    for i in range(7):
        for j in range(5):
            if((j%4==0 and i<=3) or (i==4 and (j in [1,3])) or (j==2 and (i in [2,3]))):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == "X" or string == 'x':
    for i in range(7):
        for j in range(5):
            if((j%4==0 and (i in (0,1,5,6))) or ((j in (1,3)) and (i in (2,4))) or (i==3 and j==2)):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == "Y" or string == "y":
    for i in range(7):
        for j in range(5):
            if((j%4==0 and (i<=1)) or (j==2 and (i in (3,4,5))) or (i==2 and j%2!=0)):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif string == "Z" or string == "z":
    for i in range(7):
        for j in range(5):
            if((i%6==0 and j<=4) or (i+j==5) or ((i in (1,)) and (j%4==0))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

else:
    alphabet_upper = 65
    alphabet_lower = 97
    print("[!] Enter an alphabet e.g. -->",end = "")
    for i in range(26):
        print(chr(alphabet_upper),end=' ')
        alphabet_upper = alphabet_upper + 1
    print(end=" ")
    for i in range(26):
        print(chr(alphabet_lower),end=" ")
        alphabet_lower = alphabet_lower + 1
print("thanks for using this program Regards ~M11")
