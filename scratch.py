html = []

# Ring 1 (Top)
html.append("          <!-- Ring 1 (Top) -->")
for i in range(12):
    angle = i * 30
    img_num = i + 2
    html.append(f'          <div class="ring-anchor" style="transform: rotateY({angle}deg) translateY(-220px) translateZ(500px);">\n            <div class="ring-item"><img src="img/mockup_{img_num}.png" alt="Design mockup"></div>\n          </div>')

# Ring 2 (Middle)
html.append("\n          <!-- Ring 2 (Middle) -->")
for i in range(12):
    angle = i * 30
    img_num = i + 2
    html.append(f'          <div class="ring-anchor" style="transform: rotateY({angle}deg) translateY(0px) translateZ(350px);">\n            <div class="ring-item"><img src="img/mockup_{img_num}.png" alt="Design mockup"></div>\n          </div>')

# Ring 3 (Bottom)
html.append("\n          <!-- Ring 3 (Bottom) -->")
for i in range(12):
    angle = i * 30
    img_num = i + 2
    html.append(f'          <div class="ring-anchor" style="transform: rotateY({angle}deg) translateY(220px) translateZ(200px);">\n            <div class="ring-item"><img src="img/mockup_{img_num}.png" alt="Design mockup"></div>\n          </div>')

with open("scratch.html", "w") as f:
    f.write("\n".join(html) + "\n")
