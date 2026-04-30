# -*- coding: utf-8 -*-
import csv, os, io, gzip, pickle
from collections import Counter
from pathlib import Path

DATA_DIR = Path("../../../assets/stu-data/")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def task1():
    inp = DATA_DIR / '113年新生資料庫.csv'
    out = OUTPUT_DIR / '113_star.txt'
    if not inp.exists(): return
    with open(inp, 'r', encoding='utf-8-sig') as f, open(out, 'w', encoding='utf-8') as of:
        reader = csv.DictReader(f)
        data = [f"{r['系所名稱']} | {r['學號']} | {r['畢業學校']}" for r in reader if r['入學方式'] == '繁星推甄']
        of.write('\n'.join(data) + f'\n共 {len(data)} 筆')

if __name__ == '__main__':
    task1()
