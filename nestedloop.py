# for i in range(5):
#     for j  in range(i):
#         print(j,end=" ")
#     print()
    
# for i in range(5):
#     for j in range(5):
#         print(i,end=" ")
#     print()

# for i in range(5):
#     for j in range(i):
#         print(j,end=" ")
#     print()

# x=5
# for i in range(3):
#     for j in range(3):
#         print(x,end=" ")
#         x+=5
#     print()

# x=1
# for i in range (5):
    # for j in range (i):
    #     print(x,end=" ") 
    #     x+=1
    # print()
    

x=1
for i in range (10):
    for j in range (i):
        if j%2==0:
            print("0",end=" ")
        else:
            print('1',end=" ")
    print()            
        
        