#!/usr/bin/env python3
"""Sync local sample_bin.json to JSONBin v3.

Usage:
  - Set env JSONBIN_MASTER_KEY (preferred) or the script will try to extract from index.html.
  - Set env BIN_ID (optional) or the script will try to extract from index.html.
  - Run: python3 sync_sample_to_jsonbin.py
"""
import os, json, sys, re
from urllib import request, error

ROOT = os.path.dirname(__file__)
SAMPLE = os.path.join(ROOT, 'sample_bin.json')
INDEX = os.path.join(ROOT, 'index.html')

def extract_from_index():
    if not os.path.exists(INDEX):
        return None, None
    txt = open(INDEX, 'r', encoding='utf-8').read()
    mk = re.search(r"const MASTER_KEY\s*=\s*'([^']+)'", txt)
    bid = re.search(r"const BIN_ID\s*=\s*'([^']+)'", txt)
    return (mk.group(1) if mk else None, bid.group(1) if bid else None)

def load_sample():
    if not os.path.exists(SAMPLE):
        print('sample_bin.json not found')
        return None
    with open(SAMPLE,'r',encoding='utf-8') as f:
        return json.load(f)

def put_bin(bin_id, master_key, payload):
    url = f'https://api.jsonbin.io/v3/b/{bin_id}'
    data = json.dumps(payload).encode('utf-8')
    req = request.Request(url, data=data, method='PUT')
    req.add_header('Content-Type','application/json')
    req.add_header('X-Master-Key', master_key)
    req.add_header('X-Bin-Meta','false')
    try:
        with request.urlopen(req, timeout=30) as r:
            resp = r.read().decode('utf-8')
            print('PUT OK:', r.status)
            print(resp)
            return True
    except error.HTTPError as e:
        print('HTTPError', e.code, e.read().decode('utf-8'))
    except Exception as e:
        print('Error:', e)
    return False

def main():
    mk = os.environ.get('JSONBIN_MASTER_KEY')
    bid = os.environ.get('BIN_ID')
    if not (mk and bid):
        emk, ebid = extract_from_index()
        mk = mk or emk
        bid = bid or ebid
    if not (mk and bid):
        print('Missing MASTER_KEY or BIN_ID. Provide via env or in index.html')
        sys.exit(2)
    payload = load_sample()
    if payload is None:
        sys.exit(1)
    ok = put_bin(bid, mk, payload)
    if not ok:
        print('Sync failed (403 or network). Keep sample_bin.json for later retries.')
        sys.exit(3)
    print('Sync completed successfully.')

if __name__ == '__main__':
    main()
