from datetime import  datetime
import pandas as pd

file1=open("data.txt","a")

#file1.write("Date\t\tVPN-e\t\tVPN-o\t\tOfc-e\t\tOfc-o\t\tVPN-T\t\tOfc-T\t\tTotal")

dt=datetime(2022,10,1)
dtt=dt.date()

ve=input("vpn entry")
vo=input("vpn out")
oe=input("office entry")
oo=input("office out")

vte=datetime.strptime(ve,"%H:%M")
vto=datetime.strptime(vo,"%H:%M")
ote=datetime.strptime(oe,"%H:%M")
oto=datetime.strptime(oo,"%H:%M")

vT=vto-vte
oT=oto-ote
T=vT+oT

try:
    print(str(vT).split(",")[1])
    vT=str(vT).split(",")[1]
except:
    print(str(vT).split(",")[0])
    vT=str(vT).split(",")[0].strip()

try:
    print(str(oT).split(",")[1])
    oT=str(oT).split(",")[1].strip()
except:
    print(str(oT).split(",")[0])
    oT=str(oT).split(",")[0].strip()  

try:
    print(str(T).split(",")[1])
    T=str(T).split(",")[1].strip()
except:
    print(str(T).split(",")[0])
    T=str(T).split(",")[0].strip()  

file1.write("\n%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s"%(dtt,ve,vo,oe,oo,vT,oT,T))
file1.close()
#file1.write("Date\t\tVPN-e\t\tVPN-o\t\tOfc-e\t\tOfc-o\t\tVPN-T\t\tOfc-T\t\tTotal")


df = pd.read_table('data.txt',sep="\t\t",engine='python')
df.to_excel('output.xlsx', 'Sheet1')
