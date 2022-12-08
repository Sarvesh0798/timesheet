class Solution:
    def fullJustify(self,inp,maxw):
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

        for idx,m in enumerate(mylist):
            if not len(m)==maxw:
                mylist[idx]=m+" "*(maxw-len(m))

        for m in (mylist):
            j=0
            flagbfs=False
            flagsp=False
            flagafs=False


            newstring=list(m)
            mcopy=m.strip()
            copylist=list(mcopy)
            count=0
            while newstring[-1] == " ":
                if j==len(newstring):
                    if flagafs:
                        break
                    elif len(list(m)) == len(newstring):
                        newlist.append(newstring)
                        break
                    else:
                        j=0
                        count=count+1
                        flagbfs=False
                        flagsp=False
                if not newstring[j] ==" ":
                    if flagsp==True and flagbfs==True:
                        flagsp=False
                        flagbfs=False
                        flagafs=True
                        copylist.insert(j+count," ")  
                        newstring.pop() 

                    else:
                        flagbfs=True
                        flagafs=False

                else:
                    flagsp=True

                j=j+1

            newlist.append("".join(copylist))


        return newlist
    
