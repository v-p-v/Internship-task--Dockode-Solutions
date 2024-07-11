r=int(input("Enter number of Rows:"))
c=int(input("Enter number of Columns:"))
c=5
for j in range(c-(c-r)):
    print(" ___    ",end="")
print()
    
for i in range(r):
    for j in range(c-(c-r)):
        print("/   \___",end="")
    print()

    for j in range(c-(c-r)):
        print("\___/   ",end="")
    print()
