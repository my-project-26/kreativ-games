import json, re, collections
P = "/home/claude/kreativ-games/ideen.js"

REGELN = {
    "winter": r"weihnacht|advent|nikolaus|tannenbaum|papiertanne|baumschmuck|schnee|engel|\bstern|kerze|winter|eisbär|pinguin|rentier|handschuh|weihnachtssocke|korkhaus|weihnachtskugel|geschenke basteln|valentin|fasching|karneval|clown|cowboy|krone|zepter|prinzessin|rapunzel|windlicht weihnachten",
    "frühling": r"oster|ostern|hase|hasen|kaninchen|küken|henne|huhn|hahn|frühling|tulpe|krokus|schneeglöckchen|gänseblümchen|lilie|\brose|rosen|blume|blüte|muttertag|frauentag|8\.? ?märz|marienkäfer|schmetterling|biene|raupe|schnecke|vogel|vögel|kresse|osternest|\bschaf|feldblumen|storch",
    "sommer": r"sommer|sonne|meer|fisch|qualle|krebs|\bwal\b|seerose|schildkröte|strand|seepferd|rochen|oktopus|krake|papierschiff|frosch|fußball|windlicht meer|windrad|luftballon|eis\b|ananas|\bgarten|insekt|vulkan|tipi|marterpfahl",
    "herbst": r"herbst|kastanie|eichel|zapfen|igel|laterne|martin|halloween|kürbis|gespenst|geist|fledermaus|fledermäuse|spinne|totenkopf|papierdrachen|drachen basteln|drachen aus papier|drachen falten|bunte papierdrachen|apfel|birne|pilz|eule|fuchs|nuss|nüsse|rabe|krähe|erntedank|kartoffel",
}
AUS = {  # Fehltreffer: Name enthält Wort, ist aber nicht saisonal
    "winter": r"geburtstag|schneeglöckchen",
    "frühling": r"sonnenblume",
    "herbst": r"sonnenblume",
}

s = open(P).read()
arr = json.loads(s[s.index("["):s.rindex("]") + 1])
z = collections.Counter()
for i in arr:
    i.pop("zeit", None)
    if i["art"] != "Basteln":
        continue
    text = i["name"].lower()
    zeit = [k for k, rx in REGELN.items() if re.search(rx, text) and not (k in AUS and re.search(AUS[k], text))]
    i["zeit"] = zeit or ["ganzjährig"]
    z.update(i["zeit"])
print(z)
for k in ["winter", "frühling", "sommer", "herbst", "ganzjährig"]:
    print("\n==", k, ":", " | ".join(i["name"] for i in arr if k in i.get("zeit", [])))
open(P, "w").write("const IDEEN = " + json.dumps(arr, ensure_ascii=False, indent=1) + ";\n")
