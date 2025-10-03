import argparse, json, socket
import requests

ENDPOINTS = [
    "https://ifconfig.me/ip",
    "https://api.ipify.org",
]

def get_public_ip():
    vals = {}
    for url in ENDPOINTS:
        try:
            ip = requests.get(url, timeout=6).text.strip()
            vals[url.split("//")[1].split("/")[0]] = ip
        except Exception:
            vals[url] = None
    # найчастіше значення
    ips = [v for v in vals.values() if v]
    majority = max(set(ips), key=ips.count) if ips else None
    return majority, vals

def dns_hint():
    try:
        # пробуємо резолвнути популярний хост і взяти resolver з socket.getaddrinfo не можна,
        # тому просто даємо підказку користувачу що перевірити
        # (dnspython можна використати для реального резолвера)
        return "Check: Settings → Private DNS OFF; Socks app: DNS via proxy ON"
    except Exception:
        return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="print JSON report")
    ap.add_argument("--compare", nargs=2, metavar=("A.json","B.json"),
                    help="compare two JSON reports")
    args = ap.parse_args()

    if args.compare:
        a, b = (json.load(open(x)) for x in args.compare)
        same = a.get("ip") == b.get("ip") and a.get("ip") is not None
        out = {"same_ip": same, "ip_a": a.get("ip"), "ip_b": b.get("ip")}
        print(json.dumps(out, indent=2))
        return

    ip, matrix = get_public_ip()
    rep = {
        "endpoints": matrix,
        "dns_hint": dns_hint(),
        "same_ip": True,  # сам по собі цей звіт не знає, порівнюємо потім
        "ip": ip,
        "advice": [] if ip else ["No public IP read. Check proxy/VPN connectivity."]
    }
    if args.json:
        print(json.dumps(rep, indent=2))
    else:
        print(f"IP: {ip} | endpoints={matrix}")

if __name__ == "__main__":
    main()
