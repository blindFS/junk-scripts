#!/usr/bin/python2
# -*- coding: UTF-8 -*-
import pycurl
import cStringIO
import re

buf = cStringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'http://www.bilibili.tv/video/bangumi-two-1.html')
c.setopt(c.ENCODING, 'utf8')
c.setopt(c.WRITEFUNCTION, buf.write)
c.setopt(c.CONNECTTIMEOUT, 5)
c.setopt(c.TIMEOUT, 8)
c.perform()

raw = buf.getvalue()
output = re.findall('<a [^>]* class="title">[^<]*</a>', raw)
for li in output:
    out = re.sub(r'<a href="', 'http://bilibili.tv', li)
    out = re.sub(r'".*class="title">', '', out)
    out = re.sub('</a>', '', out)
    if out:
        print(out)
buf.close()
