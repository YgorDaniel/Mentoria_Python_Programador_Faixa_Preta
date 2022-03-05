def main():
    print("########### Break ############")
    i = 1
    while i < 5:
        print(i)
        i += 1 
        if i == 3:
            break
    print("########### Break ############")
    for j in range(10,20):
        print(j) 
        if j == 15: 
            break     
main()

print("##################################")

def main():
    print("########### Continue ############")
    i = 0
    while i < 6:
       
        i += 1
        if i == 3:
            continue
        print(i)
    print("########### Continue ############")
    for j in range(10,20):
        
        if j == 15: 
            continue
        print(j)     
main()