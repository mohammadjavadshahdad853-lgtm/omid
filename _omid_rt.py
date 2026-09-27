# -*- coding: utf-8 -*-
# _omid_rt.py — OMID::PROTECTED::V2 · generated · DO NOT EDIT
import sys as _s, base64 as _b, hashlib as _h, marshal as _m
from pathlib import Path as _P
from cryptography.hazmat.primitives.ciphers.aead import AESGCM as _A
_a6f3752db0 = bytes.fromhex("c515c2b6c332b49d325b78b5211ea0213b98e39af6e67d49990be1802200f41a")
_2248728274 = bytes.fromhex("7b647ab2c18c49f29d46e8706f83a45dafff8e431ee44cae29d1fe8a9957206f")
_6c056492dc = bytes(a ^ b for a, b in zip(_a6f3752db0, _2248728274))
def _916c0bff96():
    if _s.gettrace() is not None: raise SystemExit(1)
    if _s.version_info >= (3, 12):
        try:
            _mo = _s.monitoring
            if _mo.get_tool(_mo.DEBUGGER_ID) or _mo.get_tool(_mo.COVERAGE_ID): raise SystemExit(1)
        except AttributeError: pass
def _3ac05d5386(g, name, blob, is_bc, rt_sha):
    _916c0bff96()
    try:
        _d = _P(__file__).read_bytes().replace(b"\r\n", b"\n")
        if _h.sha256(_d).hexdigest() != rt_sha: raise SystemExit(1)
    except SystemExit: raise
    except Exception: raise SystemExit(1)
    key = _h.sha256(_6c056492dc + name.encode()).digest()
    raw = _b.b64decode(blob)
    try: pt = _A(key).decrypt(raw[:12], raw[12:], name.encode())
    except Exception: raise SystemExit(1)
    try: code = _m.loads(pt) if is_bc else compile(pt.decode("utf-8"), name, "exec")
    except SystemExit: raise
    except Exception: raise SystemExit("protected load failed")
    exec(code, g)
