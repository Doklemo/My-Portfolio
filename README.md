# Ayodeji Lemo — Personal Portfolio

Welcome to the source code for the personal portfolio of **Ayodeji Lemo**, a Product Designer and AI Design Engineer based in Lagos, Nigeria. This portfolio showcases selected case studies, professional experience, and an interactive "Playground" featuring built-in web games.

## 🚀 Features

- **Responsive & Accessible Design**: Crafted carefully with vanilla CSS and semantic HTML to look stunning across desktop, tablet, and mobile devices.
- **Dynamic Projects**: A "Work" section featuring deep dives into SaaS, Fintech, and HR Tech projects (like Benmore Technologies, Goodtalent, and KeraShopper).
- **Interactive Playground**: A dedicated space for fun micro-experiences, including a fully-playable sliding tile Puzzle Game and a multi-level Word Cross game.
- **Dark Mode Optimised**: Beautiful dark UI elements, glassmorphism effects, and smooth micro-animations.

## 🛠️ Technology Stack

This project deliberately avoids heavy frameworks in favour of clean, maintainable web standards:
- **HTML5**: Semantic and accessible structure.
- **Vanilla CSS**: A custom design system built with CSS variables (`css/tokens.css`) handling responsive layouts, typography, and fluid spacing.
- **Vanilla JavaScript**: Lightweight DOM manipulation, custom cursor logic, and the complete logic for the Playground mini-games.

## 📂 Project Structure

```
.
├── about.html               # About page (Experience, Skills, Beliefs)
├── contact.html             # Get in Touch page
├── index.html               # Homepage / Landing
├── playground.html          # Entry point for mini-games
├── work.html                # Work / Portfolio overview
├── css/
│   ├── base.css             # Base element styling
│   ├── components.css       # Reusable UI components (buttons, cards)
│   ├── layout.css           # Grid systems and containers
│   ├── tokens.css           # Design system variables (colours, spacing)
│   └── pages/               # Page-specific stylesheets
├── js/
│   ├── main.js              # Global site logic (nav, custom cursor)
│   └── sounds.js            # Sound effects for games
├── games/                   
│   ├── crossword.html       # Multi-level Word Cross game
│   └── puzzle.html          # Sliding tile puzzle game
└── work/                    # Detailed case study pages
```

## 🎮 Playground Games

- **Word Cross:** A crossword puzzle game with multiple levels (Starter, Intermediate, Expert) and a dynamic responsive grid.
- **Puzzle:** A sliding image puzzle that scales dynamically based on device width to preserve perfect aspect ratios on mobile.

## 🌍 Live Site

The portfolio is hosted and deployed automatically via Vercel (or a similar hosting provider). 

---
*Designed, Built, and Shipped by Ayodeji Lemo*
