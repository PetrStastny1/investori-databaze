import re,sys,json,html
S=sys.argv[1]
dec=json.JSONDecoder()
rows=[]
for line in open(S+'/pampam_todo.txt',encoding='utf-8'):
    key,href,_,name=line.rstrip('\n').split('\t')
    t=open(f'{S}/raw/pampam_places/{key}.html',encoding='utf-8').read()
    chunks=re.findall(r'self\.__next_f\.push\(\[1,"((?:[^"\\]|\\.)*)"\]\)',t,flags=re.S)
    data=''.join(json.loads('"'+c+'"') for c in chunks)
    ms=[m for m in re.finditer(r'"'+key+r'":\{',data)]
    obj={}
    for m in ms:
        o,_=dec.raw_decode(data,m.end()-1)
        if isinstance(o,dict) and ('t' in o or 'address' in o) and len(o)>len(obj): obj=o
    title=re.search(r'<title>([^<]*)',t)
    rows.append({'key':key,'href':href,'name':name,'t':obj.get('t'),'address':obj.get('address'),
                 'url':obj.get('url') or obj.get('link'),'Custom1':obj.get('Custom1'),'Custom2':obj.get('Custom2'),
                 'lat':obj.get('lat'),'lon':obj.get('lon'),'title':html.unescape(title.group(1)) if title else None,
                 'desc':obj.get('description')})
json.dump(rows,open(S+'/pampam_detail.json','w'),ensure_ascii=False,indent=1)
for r in rows: print(r['name'],'|',r['address'],'|',r['lat'],r['lon'],'|',r['url'])
