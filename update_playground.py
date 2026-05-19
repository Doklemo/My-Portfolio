import re

# Update CSS
with open('css/pages/playground.css', 'r') as f:
    css = f.read()

# Replace sizes in CSS
css = re.sub(r'\.canvas-card--lg \{\s*width: \d+px;\s*height: \d+px;\s*\}', '.canvas-card--lg {\n  width: 220px;\n  height: 155px;\n}', css)
css = re.sub(r'\.canvas-card--md \{\s*width: \d+px;\s*height: \d+px;\s*\}', '.canvas-card--md {\n  width: 170px;\n  height: 120px;\n}', css)
css = re.sub(r'\.canvas-card--sm \{\s*width: \d+px;\s*height: \d+px;\s*\}', '.canvas-card--sm {\n  width: 120px;\n  height: 85px;\n}', css)
css = re.sub(r'\.canvas-card--xs \{\s*width: \d+px;\s*height: \d+px;\s*\}', '.canvas-card--xs {\n  width: 90px;\n  height: 65px;\n}', css)

# Make sure we don't need to replace media queries as they will just override to even smaller sizes (or we could just drop them if they match)

with open('css/pages/playground.css', 'w') as f:
    f.write(css)

# Update HTML for panning
with open('playground.html', 'r') as f:
    html = f.read()

# Add pan wrapper to HTML
if 'id="canvas-pan-layer"' not in html:
    html = html.replace('<!-- Scattered design cards', '<div id="canvas-pan-layer" style="position: absolute; inset: 0; transform-origin: 0 0; will-change: transform;">\n      <!-- Scattered design cards')
    html = html.replace('<!-- Hint pill -->', '</div>\n\n      <!-- Hint pill -->')

# Replace JS logic for dragging to support panning
js_to_replace = """      // ---- Drag Logic ----
      let dragCard = null;
      let dragOffsetX = 0;
      let dragOffsetY = 0;
      let dragStartX = 0;
      let dragStartY = 0;
      let dragDistance = 0;
      let hintHidden = false;

      function getPointer(e) {
        if (e.touches && e.touches.length) {
          return { x: e.touches[0].clientX, y: e.touches[0].clientY };
        }
        return { x: e.clientX, y: e.clientY };
      }

      function onDragStart(e) {
        // Don't drag if lightbox is open
        if (lightbox.classList.contains('is-open')) return;

        const card = e.target.closest('.canvas-card');
        if (!card) return;

        const pointer = getPointer(e);
        const rect = card.getBoundingClientRect();
        const canvasRect = canvas.getBoundingClientRect();

        dragCard = card;
        dragOffsetX = pointer.x - rect.left;
        dragOffsetY = pointer.y - rect.top;
        dragStartX = pointer.x;
        dragStartY = pointer.y;
        dragDistance = 0;

        // Bring to front
        topZ++;
        card.style.zIndex = topZ;
        card.classList.add('is-dragging');

        // Remove rotation while dragging for clean feel
        card.style.transform = 'rotate(0deg) scale(1.04)';

        if (e.type === 'mousedown') e.preventDefault();

        // Hide hint after first drag
        if (!hintHidden && hint) {
          hintHidden = true;
          hint.classList.add('is-hidden');
        }
      }

      function onDragMove(e) {
        if (!dragCard) return;

        const pointer = getPointer(e);
        const canvasRect = canvas.getBoundingClientRect();

        const x = pointer.x - canvasRect.left - dragOffsetX + canvas.scrollLeft;
        const y = pointer.y - canvasRect.top - dragOffsetY + canvas.scrollTop;

        dragCard.style.left = x + 'px';
        dragCard.style.top = y + 'px';

        dragDistance = Math.abs(pointer.x - dragStartX) + Math.abs(pointer.y - dragStartY);
      }

      function onDragEnd(e) {
        if (!dragCard) return;

        const card = dragCard;
        const rotate = parseFloat(card.dataset.rotate) || 0;

        card.classList.remove('is-dragging');
        card.style.transform = 'rotate(' + rotate + 'deg) scale(1)';

        // If barely moved, treat as click → open lightbox
        if (dragDistance < 6) {
          openLightbox(card);
        }

        dragCard = null;
      }"""

new_js = """      // ---- Drag & Pan Logic ----
      const panLayer = document.getElementById('canvas-pan-layer');
      let dragCard = null;
      let dragOffsetX = 0;
      let dragOffsetY = 0;
      
      let isPanning = false;
      let panStartX = 0;
      let panStartY = 0;
      let currentPanX = 0;
      let currentPanY = 0;
      
      let startPointerX = 0;
      let startPointerY = 0;
      let dragDistance = 0;
      let hintHidden = false;

      function getPointer(e) {
        if (e.touches && e.touches.length) {
          return { x: e.touches[0].clientX, y: e.touches[0].clientY };
        }
        return { x: e.clientX, y: e.clientY };
      }

      function onDragStart(e) {
        if (lightbox.classList.contains('is-open')) return;

        const pointer = getPointer(e);
        startPointerX = pointer.x;
        startPointerY = pointer.y;
        dragDistance = 0;
        
        const card = e.target.closest('.canvas-card');
        
        if (!card) {
          // Start panning
          isPanning = true;
          panStartX = pointer.x - currentPanX;
          panStartY = pointer.y - currentPanY;
          canvas.style.cursor = 'grabbing';
          if (e.type === 'mousedown') e.preventDefault();
          return;
        }

        // Start dragging card
        const rect = card.getBoundingClientRect();
        // Calculate offset relative to the card's visual top-left
        dragOffsetX = pointer.x - rect.left;
        dragOffsetY = pointer.y - rect.top;

        dragCard = card;

        // Bring to front
        topZ++;
        card.style.zIndex = topZ;
        card.classList.add('is-dragging');

        // Remove rotation while dragging for clean feel
        card.style.transform = 'rotate(0deg) scale(1.04)';

        if (e.type === 'mousedown') e.preventDefault();

        // Hide hint after first drag
        if (!hintHidden && hint) {
          hintHidden = true;
          hint.classList.add('is-hidden');
        }
      }

      function onDragMove(e) {
        if (!dragCard && !isPanning) return;

        const pointer = getPointer(e);
        dragDistance = Math.abs(pointer.x - startPointerX) + Math.abs(pointer.y - startPointerY);

        if (isPanning) {
          currentPanX = pointer.x - panStartX;
          currentPanY = pointer.y - panStartY;
          
          // Move the cards layer
          if (panLayer) panLayer.style.transform = `translate(${currentPanX}px, ${currentPanY}px)`;
          // Move the background dot grid
          canvas.style.backgroundPosition = `${currentPanX}px ${currentPanY}px`;
          return;
        }

        // Dragging card
        const canvasRect = canvas.getBoundingClientRect();

        // When placing a card, we need to factor out the current pan layer offset
        // so it stays exactly where the cursor is.
        const x = pointer.x - canvasRect.left - dragOffsetX - currentPanX + canvas.scrollLeft;
        const y = pointer.y - canvasRect.top - dragOffsetY - currentPanY + canvas.scrollTop;

        dragCard.style.left = x + 'px';
        dragCard.style.top = y + 'px';
      }

      function onDragEnd(e) {
        if (isPanning) {
          isPanning = false;
          canvas.style.cursor = 'default';
        }

        if (!dragCard) return;

        const card = dragCard;
        const rotate = parseFloat(card.dataset.rotate) || 0;

        card.classList.remove('is-dragging');
        card.style.transform = 'rotate(' + rotate + 'deg) scale(1)';

        // If barely moved, treat as click → open lightbox
        if (dragDistance < 6) {
          openLightbox(card);
        }

        dragCard = null;
      }"""

if "let isPanning = false;" not in html:
    html = html.replace(js_to_replace, new_js)

with open('playground.html', 'w') as f:
    f.write(html)
