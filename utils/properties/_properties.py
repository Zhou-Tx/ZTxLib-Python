#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :  2021/3/24
# @Author   :  ZhouTianxing
# @Software :  PyCharm Professional x64
# @FileName :  _properties.py
""""""
import codecs
from typing import IO
from typing import Union


class PropertiesDecodeError(ValueError):
    def __init__(self, msg, doc, pos):
        lineno = doc.count('\n', 0, pos) + 1
        colno = pos - doc.rfind('\n', 0, pos)
        errmsg = '%s: line %d column %d (char %d)' % (msg, lineno, colno, pos)
        ValueError.__init__(self, errmsg)
        self.msg = msg
        self.doc = doc
        self.pos = pos
        self.lineno = lineno
        self.colno = colno

    def __reduce__(self):
        return self.__class__, (self.msg, self.doc, self.pos)


def detect_encoding(b: bytes):
    if b.startswith((codecs.BOM_UTF32_BE, codecs.BOM_UTF32_LE)):
        return 'utf-32'
    if b.startswith((codecs.BOM_UTF16_BE, codecs.BOM_UTF16_LE)):
        return 'utf-16'
    if b.startswith(codecs.BOM_UTF8):
        return 'utf-8-sig'

    if len(b) >= 4:
        if not b[0]:
            # 00 00 -- -- - utf-32-be
            # 00 XX -- -- - utf-16-be
            return 'utf-16-be' if b[1] else 'utf-32-be'
        if not b[1]:
            # XX 00 00 00 - utf-32-le
            # XX 00 00 XX - utf-16-le
            # XX 00 XX -- - utf-16-le
            return 'utf-16-le' if b[2] or b[3] else 'utf-32-le'
    elif len(b) == 2:
        if not b[0]:
            # 00 XX - utf-16-be
            return 'utf-16-be'
        if not b[1]:
            # XX 00 - utf-16-le
            return 'utf-16-le'
    # default
    return 'utf-8'


def load(fp: IO, *args, **kwargs) -> dict:
    return loads(fp.read(), *args, **kwargs)


def loads(s: Union[str, bytes], *args, **kwargs) -> dict:
    result = dict()
    if isinstance(s, str):
        if s.startswith('\ufeff'):
            raise PropertiesDecodeError(
                "Unexpected UTF-8 BOM (decode using utf-8-sig)",
                s, 0)
    else:
        if not isinstance(s, (bytes, bytearray)):
            raise TypeError(f'the properties object must be str, bytes or bytearray, '
                            f'not {s.__class__.__name__}')
        s = s.decode(detect_encoding(s), 'surrogatepass')

    lines = [line.strip() for line in s.split('\n')]
    lines = [line.split('=') for line in lines if line.count('=') == 1]
    lines = [{
        'key': line[0].split('.'),
        'value': line[1]
    } for line in lines]
    for line in lines:
        obj = result
        for index, key in enumerate(line['key']):
            if index == len(line['key']) - 1:
                obj[key] = line['value']
            elif key not in obj.keys():
                obj[key] = dict()
                obj = obj[key]
            else:
                obj = obj[key]
    return result
