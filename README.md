# same-ip-guardian
Verify that your phone and PC use the exact same public IP. One tap/one command sanity check for proxy/VPN setups. JSON report, leak hints, shareable badge.
Title + Badges
# same-ip-guardian
[![CI](https://github.com/<YOU>/same-ip-guardian/actions/workflows/ci.yml/badge.svg)](…)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Intro

A tiny tool to prove two devices/apps share the same egress IP.
Checks multiple endpoints (ifconfig/ipify), detects DNS leak hints, prints a neat JSON report and a copy-paste badge you can share.

Features

🔎 Same IP check (PC ↔ phone / browser ↔ app)

🌐 Multi-endpoint verify: compares 2–3 IP services to avoid false reads

🧪 DNS leak hints: warns if DNS resolver doesn’t match your proxy region

🧾 JSON/Markdown output for reports

🧰 Zero-config, works with SOCKS5/HTTP/VPN

Quick start
# 1) Клон
git clone https://github.com/<YOU>/same-ip-guardian && cd same-ip-guardian
# 2) Залежності
pip install -r requirements.txt
# 3) Запуск на ПК (через ваш проксі/ADS-профіль)
python -m guardian --json > pc.json

# На телефоні (через SocksDroid/Postern, той самий SOCKS5):
# відкрийте https://<YOU>.github.io/same-ip-guardian/quick (опц.) або
# запустіть quick_check на Android (Termux):
python scripts/quick_check.py --json > phone.json

# 4) Порівняти
python -m guardian --compare pc.json phone.json
