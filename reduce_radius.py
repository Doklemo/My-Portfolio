import re

with open('playground.html', 'r') as f:
    html = f.read()

# Reduce gap on Top Ring (Ring 1)
html = html.replace('--tz: 450px;', '--tz: 360px;')

# Reduce gap on Middle Ring (Ring 2)
html = html.replace('--tz: 350px;', '--tz: 260px;')

with open('playground.html', 'w') as f:
    f.write(html)
