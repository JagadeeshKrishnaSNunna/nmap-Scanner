import os;
from xml.etree import ElementTree

fileName='example.xml'
#fileName='res.xml'
dom=ElementTree.parse(fileName)
#service=dom.findall('table')
root=dom.getroot()
"""
host=root[4]
ports=host[3]
ports=ports[1:]
"""
host=root.find('host')
#print("hosts--->  ",host)
ports=host.find("ports")
ports=ports.findall('port')
#print("ports=> ",ports)
#------------------------------------------
script=[]
for p in ports:
    script.append(p.findall('script'))



table=[]
#print("script==> ",script)
for i in script:
    for j in i:#print(i.find('table'))
        table.append(j.find('table'))

#print("table==> ",table)
tab=[]
for t in table:
    if(t!=None):
        tab.append( t.findall('table'))

#print(tab[0][0].find('elem').get('key'))
#print("tab===>",tab)

#script=(ports[1][-1])
#table=script[0]
#for i in table:
#    print(i.tag)



#print(tab)


#-----------------------------
"""
script=(ports[1][-1])
table=script[0]

"""
vul=[]


for s in tab:
    for ele in s:
        vul.append(ele.findall('elem'))

#print("vul====>",vul)
reso={}
res=[]

for v in vul:
    v[:] = sorted(v, key=lambda child: (child.tag,child.get('key')))#print(v[0].text)
    #print("---------------------------------------------",v[0].text)
    if(float(v[0].text)>=7 and v[2].text=='true'):
        reso['CVSS']=v[0].text
        reso['type']=v[3].text
        reso['ref']=v[1].text
        reso['exp']=v[2].text
        res.append(reso)
    reso={}

print(res)
    #for e in v:
        #print(e.text)#if(float(e.text)>=7 and e.text=='true'):
            #reso['CVSS']=e[0].text
            #print(e.text)




"""
for e in vul:
    print(e.get("id"))

    if(float(e[0].text)>=7 and e[2].text=='true'):
        reso['CVSS']=e[0].text
        reso['type']=e[3].text
        reso['ref']=e[1].text
        reso['exp']=e[2].text
        res.append(reso)
    reso={}
print(res)
#    for el in e:
#        print(el.attrib)


"""