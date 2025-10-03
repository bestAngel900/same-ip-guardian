import json, requests
urls = ["https://ifconfig.me/ip","https://api.ipify.org"]
vals = {}
for u in urls:
    try: vals[u] = requests.get(u, timeout=6).text.strip()
    except Exception: vals[u] = None
ips = [v for v in vals.values() if v]
ip = max(set(ips), key=ips.count) if ips else None
print(json.dumps({"ip": ip, "endpoints": vals}, indent=2))
