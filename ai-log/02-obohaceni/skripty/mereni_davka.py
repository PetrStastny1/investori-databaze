import json,sys
from datetime import datetime
S,d,start,end=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
ids=sys.argv[5:]
klice=["WebSearch","WebFetch","WebFetch_neuspesne","ARES","fundingtecheu","jine_curl"]
zk={"WebSearch":"WS","WebFetch":"WF","WebFetch_neuspesne":"WFx","ARES":"ARES","fundingtecheu":"FTE","jine_curl":"curl"}
tot={k:0 for k in klice}; rad=[]
for i in ids:
    v=json.load(open(f"{S}/vysledky/{i}.json")); p=v.get("pozadavky") or {}
    for k in klice: tot[k]+=p.get(k,0)
    rad.append(f"  {i:38s}" + "".join(f"{p.get(k,0):>5d}" for k in klice) + f"  {v['vysledek']}")
f=lambda s:datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ")
m,s=divmod(int((f(end)-f(start)).total_seconds()),60)
print(f"Dávka {d} ({len(ids)} kandidátů)\n" + "-"*30)
print(f"  začátek {start}, konec {end}, doba {m} min {s} s")
print(f"  {'kandidát':38s}" + "".join(f"{zk[k]:>5s}" for k in klice))
print("\n".join(rad))
print(f"  {'celkem':38s}" + "".join(f"{tot[k]:>5d}" for k in klice) + f"  (celkem {sum(tot.values())-tot['WebFetch_neuspesne']} požadavků)")
print("  WS = WebSearch, WF = WebFetch, WFx = z toho neúspěšné WebFetch, FTE = funding.tech.eu API, curl = jiné stažení stránky")
