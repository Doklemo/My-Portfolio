import re

with open('playground.html', 'r') as f:
    html = f.read()

# The top ring currently has `--ty: -280px; --tz: 500px;`
def reduce_diameter(match):
    # match.group(0) is the full match, but we only want to replace 500px with 450px
    return match.group(0).replace('500px', '450px')

html = re.sub(r'style="--ry: \d+deg; --ty: -280px; --tz: 500px;"', reduce_diameter, html)

with open('playground.html', 'w') as f:
    f.write(html)
