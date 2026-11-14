import json,re
P="/home/claude/kreativ-games/ideen.js"
s=open(P).read();arr=json.loads(s[s.index("["):s.rindex("]")+1])
tk=json.load(open("bilder_tk.json"));ks=json.load(open("bilder_ks.json"))
TK="https://www.tutkit.com/storage/media/help/";KS="https://www.kinderspiele-welt.de/wp-content/uploads/"
def klein(p):
    m=re.match(r"(.*)-(\d+)x(\d+)(\.\w+)$",p)
    if not m: return None
    w,h=int(m[2]),int(m[3])
    if max(w,h)<=420: return None
    nw,nh=(400,round(400*h/w)) if w>=h else (round(400*w/h),400)
    return f"{m[1]}-{nw}x{nh}{m[4]}"
n=0
for i in arr:
    i.pop("foto",None);i.pop("fotoGross",None)
    if i["id"] in tk: i["foto"]=TK+tk[i["id"]];n+=1
    elif i["id"] in ks:
        p=ks[i["id"]];k=klein(p)
        if k: i["foto"]=KS+k;i["fotoGross"]=KS+p
        else: i["foto"]=KS+p
        n+=1
b=[i for i in arr if i["art"]=="Basteln"]
print(n,"Fotos;",len(b),"Basteln; ohne:",len([i for i in b if "foto" not in i]))
print([i["anleitung"] for i in b if "foto" not in i and "tutkit" in i["anleitung"]])
open(P,"w").write("const IDEEN = "+json.dumps(arr,ensure_ascii=False,indent=1)+";\n")
