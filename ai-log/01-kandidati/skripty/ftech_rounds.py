import json,sys,time,urllib.request,urllib.parse
out=sys.argv[1]; allr=[]; after=None
while True:
    q={'country':'Czech Republic','from':'2025-01-01','to':'2026-12-31','limit':100}
    if after: q['after']=after
    u='https://funding.tech.eu/api/v1/rounds?'+urllib.parse.urlencode(q)
    with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'investori-databaze research'})) as r:
        j=json.load(r)
    allr+=j['data']; after=j.get('nextCursor')
    print(len(allr),after,file=sys.stderr)
    if not after or not j['data']: break
    time.sleep(1)
json.dump(allr,open(out,'w'),ensure_ascii=False,indent=1)
