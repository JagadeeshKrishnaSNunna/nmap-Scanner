import os;
from xml.etree import ElementTree

fileName='res.xml'
dom=ElementTree.parse(fileName)

root=dom.getroot()

host=root.find('host')
ports=host.find("ports")
ports=ports.findall('port')
script=[]
for p in ports:
    script.append(p.findall('script'))



table=[]
for i in script:
    for j in i:#print(i.find('table'))
        table.append(j.find('table'))

tab=[]
for t in table:
    if(t!=None):
        tab.append( t.findall('table'))


vul=[]


for s in tab:
    for ele in s:
        vul.append(ele.findall('elem'))

reso={}
res=[]

for v in vul:
    v[:] = sorted(v, key=lambda child: (child.tag,child.get('key')))#print(v[0].text)
 
    if(float(v[0].text)>=7 and v[2].text=='true'):
        reso['CVSS']=v[0].text
        reso['type']=v[3].text
        reso['ref']=v[1].text
        reso['exp']=v[2].text
        res.append(reso)
    reso={}

print(res)
    
