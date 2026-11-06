# with open('notes.txt','a',encoding="utf-8") as f:
#     f.write("sameer is a good boy")
#     f.write("\n sameer is 25 year old")

# task=["pray","study","read"]
task=[1,2,3,4,5,6,7,8,9,10]

with open ("notes.txt",'w',encoding="utf-8") as f:
    for t in task:
        f.write(str(t) +"\n")
        
    

print('file operation successfully')