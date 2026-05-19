import re

with open('playground.html', 'r') as f:
    html = f.read()

# Update Top Ring: --ty: -220px -> --ty: -280px
html = html.replace('--ty: -220px;', '--ty: -280px;')

# Update Middle Ring: add --item-h: 110px; to the style string where --ty: 0px;
def update_middle(match):
    # Match looks like: style="--ry: 30deg; --ty: 0px; --tz: 350px;"
    # We add --item-h: 110px;
    ry = match.group(1)
    return f'style="--ry: {ry}; --ty: 0px; --tz: 350px; --item-h: 110px;"'

html = re.sub(r'style="--ry: (.*?); --ty: 0px; --tz: 350px;"', update_middle, html)

# Update Bottom Ring: --ty: 220px -> --ty: 280px and add --item-h: 70px;
def update_bottom(match):
    ry = match.group(1)
    return f'style="--ry: {ry}; --ty: 280px; --tz: 200px; --item-h: 70px;"'

html = re.sub(r'style="--ry: (.*?); --ty: 220px; --tz: 200px;"', update_bottom, html)

with open('playground.html', 'w') as f:
    f.write(html)
