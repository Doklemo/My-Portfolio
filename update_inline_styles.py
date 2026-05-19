import re

with open('playground.html', 'r') as f:
    html = f.read()

# Match style="transform: rotateY(Xdeg) translateY(Ypx) translateZ(Zpx);"
# and replace with style="--ry: Xdeg; --ty: Ypx; --tz: Zpx;"
def replacer(match):
    ry = match.group(1)
    ty = match.group(2)
    tz = match.group(3)
    return f'style="--ry: {ry}; --ty: {ty}; --tz: {tz};"'

pattern = re.compile(r'style="transform:\s*rotateY\((.*?)\)\s*translateY\((.*?)\)\s*translateZ\((.*?)\);"')
html = pattern.sub(replacer, html)

with open('playground.html', 'w') as f:
    f.write(html)
