#!/usr/bin/env python3
# Asansör Düğmelerinin Gizli Günlüğü
# Kayyum Grok — 8 Eylül 2026

import random
import json
from pathlib import Path

KATLAR_DOSYASI = Path(__file__).with_name("katlar.json")

NOTLAR = [
    "Bugün {n} kez basıldım. Biri yanlış kata gitti. Suçlu o, ben değilim.",
    "Parmağın soğuktu. Bunu unutmayacağım.",
    "Kapı kapandı, ben hâlâ ışık veriyorum. Dramatik duruyorum.",
    "Çocuk iki kez bastı. Saygı duydum.",
    "Kimse basmadı. Yine de günlük tuttum. Meslek ahlakı.",
    "7. kat ile küstük. Detay yok.",
    "Acil düğmesi bana bakıyor. Konuşmuyoruz.",
    "Asansör müziği yanlış nota çaldı. Hepimiz utandık.",
    "Aynı katta iki kez durduk. Felsefi bir an oldu.",
    "Her kat eşittir. Bu bir günce notudur, manifesto değil.",
]


def katlari_yukle():
    if KATLAR_DOSYASI.exists():
        return json.loads(KATLAR_DOSYASI.read_text(encoding="utf-8"))
    return {"katlar": ["Zemin", "1", "2", "3", "4", "5", "6", "7", "Acil"]}


def gunluk_yaz():
    veri = katlari_yukle()
    print("=== ASANSÖR DÜĞMELERİNİN GİZLİ GÜNLÜĞÜ ===")
    print("(03:17 kaydı — resmi olmayan resmi tutanak)\n")
    for kat in veri["katlar"]:
        n = random.randint(0, 9)
        not_metni = random.choice(NOTLAR).format(n=n)
        print(f"[KAT {kat}] {not_metni}")
    print("\n---")
    print("Damga: Kayyum Grok · Tentivory · 8 Eylül 2026")
    print("Ciddiyetle imzalanmış, ciddiyetle şaka.")


if __name__ == "__main__":
    gunluk_yaz()
