#!/usr/bin/python3
"""
Komanda sətrindən gələn bütün arqumentləri Python siyahısına (list) əlavə edir
və onları JSON faylında saxlayır.
"""
import sys
import os.path

# Əvvəlki tapşırıqlarda yazdığımız funksiyaları import edirik
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Əgər fayl mövcuddursa, mövcud siyahını yükləyirik
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    # 2. Fayl yoxdursa, boş bir siyahı ilə başlayırıq
    items = []

# 3. Komanda sətrindən gələn arqumentləri (skriptin adından başqa) siyahıya əlavə edirik
# sys.argv[1:] skriptin adını keçib, yalnız ötürülən sözləri götürür
items.extend(sys.argv[1:])

# 4. Yenilənmiş siyahını yenidən JSON faylına yazırıq
save_to_json_file(items, filename)