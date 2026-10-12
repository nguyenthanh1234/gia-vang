"""Lấy giá vàng/bạc thế giới + tỷ giá, thêm 1 điểm vào data/history.json.

GitHub Actions chạy script này định kỳ (xem .github/workflows/update.yml).
Chạy tay: python scripts/update.py
"""
import json
import os
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(ROOT, "data", "history.json")
MAX_POINTS = 40000          # ~2 năm với 1 điểm / 30 phút
RATES_TTL = 6 * 3600        # làm mới tỷ giá mỗi 6 giờ


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "hoc3giay-giavang"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r)


def main():
    try:
        with open(FILE, encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"points": [], "rates": None, "rates_t": 0}

    now = int(time.time())
    if not data.get("rates") or now - data.get("rates_t", 0) >= RATES_TTL:
        fx = get_json("https://open.er-api.com/v6/latest/USD")
        if fx.get("result") == "success":
            data["rates"], data["rates_t"] = fx["rates"], now

    gold = get_json("https://api.gold-api.com/price/XAU")
    try:
        silver = get_json("https://api.gold-api.com/price/XAG").get("price")
    except Exception:
        silver = None

    data["points"].append({
        "t": now * 1000,
        "xau": round(float(gold["price"]), 2),
        "xag": round(float(silver), 3) if silver else None,
        "vnd": round(float(data["rates"]["VND"]), 2),
    })
    data["points"] = data["points"][-MAX_POINTS:]

    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, separators=(",", ":"))
    print("points:", len(data["points"]), "last:", data["points"][-1])


if __name__ == "__main__":
    main()
