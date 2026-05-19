import re

# Update HTML
with open('playground.html', 'r') as f:
    html_content = f.read()

with open('scratch.html', 'r') as f:
    new_rings = f.read()

# The original ring items are bounded by <!-- Item 1 --> and <!-- Item 12 --> ... </div>
pattern = re.compile(r'          <!-- Item 1 -->.*?<!-- Item 12 -->.*?</div>\n', re.DOTALL)
html_content = pattern.sub(new_rings, html_content)

with open('playground.html', 'w') as f:
    f.write(html_content)

# Update CSS
with open('css/pages/playground.css', 'r') as f:
    css_content = f.read()

css_content = css_content.replace('height: 600px;', 'height: 800px;')

with open('css/pages/playground.css', 'w') as f:
    f.write(css_content)

