

def justifytext(inp,maxw):
    count=0
    i,mylist,s1=0,[],""
    newlist=[]
    while len(inp) > 0:
        if len(s1+inp[i]+" ") <= maxw:
            s1=s1+inp[i]+" "
            inp=inp[i+1:]

        else:
            mylist.append(s1)
            s1=""
        if len(inp)==0:
            mylist.append(s1)
    print(mylist)
    
    for idx,m in enumerate(mylist):
        j=0
        flagbfs=False
        flagsp=False
        flagafs=False

        if not len(m)== maxw:
            mylist[idx]=m+" "*(maxw-len(m))

        newstring=list(m)
        while newstring[-1] == " ":
            if j==len(newstring):
                if flagafs:
                    break
                else:
                    j=0
            if not newstring[j] ==" ":
                if flagsp==True and flagbfs==True:
                    flagsp=False
                    flagbfs=False
                    flagafs=True
                    newstring.insert(j-1," ")  
                    newstring.pop() 
                    
                else:
                    flagbfs=True
                    flagafs=False
                 
            else:
                flagsp=True
         
            j=j+1
        newlist.append("".join(newstring))


    return newlist






inp=["this","is","an","example","of","text","justification."]
maxw=16
print(justifytext(inp,maxw))
