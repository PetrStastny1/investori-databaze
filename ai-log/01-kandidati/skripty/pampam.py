import re,sys,json
t=open(sys.argv[1],encoding='utf-8').read()
# Next.js flight chunks: self.__next_f.push([1,"..."])
chunks=re.findall(r'self\.__next_f\.push\(\[1,"((?:[^"\\]|\\.)*)"\]\)',t,flags=re.S)
data=''.join(json.loads('"'+c+'"') for c in chunks)
dec=json.JSONDecoder()
places={}
for m in re.finditer(r'"([A-Za-z0-9]{20})":\{"t":',data):
    try:
        obj,_=dec.raw_decode(data,m.end()-len('{"t":'))
    except Exception as e:
        continue
    places.setdefault(m.group(1),obj)
print(len(places),file=sys.stderr)
out=[]
for k,o in places.items():
    out.append({'key':k,'t':o.get('t'),'address':o.get('address'),'url':o.get('url') or o.get('link'),
                'parent':o.get('parent'),'display':o.get('display'),'keys':sorted(o.keys())})
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
