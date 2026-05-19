import re

with open('css/pages/playground.css', 'r') as f:
    css = f.read()

# Remove height lines inside media queries for canvas-card modifiers
css = re.sub(r'(\.canvas-card--(?:lg|md|sm|xs)\s*\{[^}]*?)\s*height:\s*\d+px;([^}]*?\})', r'\1\2', css)

with open('css/pages/playground.css', 'w') as f:
    f.write(css)
