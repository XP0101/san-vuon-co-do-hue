"""Kiểm tra cấu trúc, liên kết và dữ liệu SEO của bản xuất HTML."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.ids=[];self.links=[];self.h1=0;self.imgs=[];self.scripts=[];self.capture=False;self.buf='';self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id'in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='a':self.links.append(a.get('href',''))
        if tag=='img':self.imgs.append(a)
        if tag=='script' and a.get('type')=='application/ld+json':self.capture=True;self.buf=''
    def handle_data(self,data):
        if self.capture:self.buf+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.capture:self.scripts.append(json.loads(self.buf));self.capture=False
root=Path(__file__).parent/'dist';pages={f.name:Page(f.read_text()) for f in root.glob('*.html')};fail=[];links=0
for name,page in pages.items():
    if page.h1!=1:fail.append(f'{name}: h1={page.h1}')
    if len(page.ids)!=len(set(page.ids)):fail.append(f'{name}: id trùng')
    if not page.scripts:fail.append(f'{name}: thiếu schema')
    for im in page.imgs:
        if not im.get('alt'):fail.append(f'{name}: thiếu alt')
    for link in page.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        links+=1;target=u.path or name
        if target not in pages:fail.append(f'{name}: thiếu {target}')
        elif u.fragment and u.fragment not in pages[target].ids:fail.append(f'{name}: thiếu neo {link}')
assert not fail,'\n'.join(fail)
print(f'ĐẠT: {len(pages)} trang; {links} liên kết nội bộ; mỗi trang đúng 1 H1; không trùng ID; alt và JSON-LD hợp lệ.')
