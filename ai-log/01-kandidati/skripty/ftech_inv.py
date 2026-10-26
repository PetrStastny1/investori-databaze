import json,sys,time,urllib.request,urllib.parse,urllib.error
R=json.load(open(sys.argv[1])); out=sys.argv[2]
names=sorted({i for r in R for i in r['investors']})
prof={}
for n in names:
    u='https://funding.tech.eu/api/v1/investors/'+urllib.parse.quote(n,safe='')
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'investori-databaze research'})) as r:
            prof[n]={'status':r.status,'data':json.load(r)}
    except urllib.error.HTTPError as e:
        prof[n]={'status':e.code,'data':None}
    time.sleep(0.7)
json.dump(prof,open(out,'w'),ensure_ascii=False,indent=1)
for n,p in prof.items():
    d=p['data'] or {}
    print(p['status'],'|',n,'|',d.get('name'),'|',d.get('types'),'|',d.get('aliases'),'|',d.get('deals'),'|',[c['name'] for c in d.get('countries',[])][:4])
