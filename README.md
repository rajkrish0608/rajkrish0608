<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Raj Krish — Engineer | Builder | Visionary</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/matter-js/0.19.0/matter.min.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700&family=Syne:wght@700;800&display=swap');

  :root {
    --bg: #07080d;
    --surface: #0d1117;
    --surface2: #161b22;
    --border: rgba(255,255,255,0.06);
    --teal: #00d4aa;
    --orange: #f97316;
    --purple: #a78bfa;
    --blue: #60a5fa;
    --white: #f0f6fc;
    --muted: #8b949e;
    --glow-teal: 0 0 30px rgba(0,212,170,0.3);
    --glow-orange: 0 0 30px rgba(249,115,22,0.3);
  }

  * { margin:0; padding:0; box-sizing:border-box; }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--white);
    font-family: 'Space Grotesk', sans-serif;
    overflow-x: hidden;
  }

  /* ─── NOISE OVERLAY ─── */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 9999;
    opacity: 0.5;
  }

  /* ─── NAV ─── */
  nav {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 100;
    padding: 20px 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: linear-gradient(to bottom, rgba(7,8,13,0.95), transparent);
    backdrop-filter: blur(8px);
  }
  .nav-logo {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 800;
    background: linear-gradient(135deg, var(--teal), var(--blue));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
  }
  .nav-links { display: flex; gap: 32px; }
  .nav-links a {
    color: var(--muted);
    text-decoration: none;
    font-size: 13px;
    font-weight: 500;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    transition: color 0.2s;
  }
  .nav-links a:hover { color: var(--teal); }

  /* ─── HERO ─── */
  #hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
    padding: 100px 60px 60px;
  }
  .hero-bg {
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 80% 60% at 50% 50%, rgba(0,212,170,0.04) 0%, transparent 70%),
                radial-gradient(ellipse 40% 40% at 80% 20%, rgba(96,165,250,0.05) 0%, transparent 60%);
  }
  .hero-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: center;
    max-width: 1200px;
    width: 100%;
    position: relative;
    z-index: 1;
  }
  .hero-text { }
  .hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--teal);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 20px;
    opacity: 0;
    animation: fadeUp 0.8s 0.2s forwards;
  }
  .hero-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(52px, 6vw, 88px);
    font-weight: 800;
    line-height: 0.95;
    letter-spacing: -3px;
    margin-bottom: 16px;
    opacity: 0;
    animation: fadeUp 0.8s 0.4s forwards;
  }
  .hero-name span {
    background: linear-gradient(135deg, var(--teal) 0%, var(--blue) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .hero-tagline {
    font-size: 18px;
    color: var(--muted);
    font-weight: 400;
    line-height: 1.6;
    max-width: 420px;
    margin-bottom: 40px;
    opacity: 0;
    animation: fadeUp 0.8s 0.6s forwards;
  }
  .hero-tagline strong { color: var(--white); font-weight: 600; }
  .hero-cta {
    display: flex;
    gap: 16px;
    opacity: 0;
    animation: fadeUp 0.8s 0.8s forwards;
  }
  .btn {
    padding: 12px 28px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: 'Space Grotesk', sans-serif;
  }
  .btn-primary {
    background: var(--teal);
    color: #000;
    border: none;
  }
  .btn-primary:hover {
    background: #00f5c4;
    transform: translateY(-2px);
    box-shadow: var(--glow-teal);
  }
  .btn-ghost {
    background: transparent;
    color: var(--white);
    border: 1px solid var(--border);
  }
  .btn-ghost:hover {
    border-color: var(--teal);
    color: var(--teal);
    transform: translateY(-2px);
  }

  /* ─── STAT BADGES ─── */
  .stat-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-top: 48px;
    opacity: 0;
    animation: fadeUp 0.8s 1s forwards;
  }
  .stat-badge {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 12px;
    text-align: center;
    transition: border-color 0.3s;
  }
  .stat-badge:hover { border-color: var(--teal); }
  .stat-val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 22px;
    font-weight: 700;
    color: var(--teal);
  }
  .stat-val.orange { color: var(--orange); }
  .stat-val.purple { color: var(--purple); }
  .stat-val.blue { color: var(--blue); }
  .stat-label {
    font-size: 10px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 4px;
  }

  /* ─── GLOBE SECTION ─── */
  #globe-section {
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 60px;
    position: relative;
    overflow: hidden;
  }
  .section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 12px;
  }
  .section-label span { color: var(--teal); margin-right: 8px; }
  .section-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(36px, 4vw, 56px);
    font-weight: 800;
    letter-spacing: -2px;
    line-height: 1.05;
    margin-bottom: 12px;
  }
  .section-title .accent { color: var(--teal); }
  .section-sub {
    color: var(--muted);
    font-size: 15px;
    line-height: 1.6;
    max-width: 400px;
    margin-bottom: 40px;
  }

  .globe-layout {
    display: grid;
    grid-template-columns: 1fr 600px;
    gap: 60px;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    width: 100%;
  }
  .globe-left { }
  .globe-legend { display: flex; flex-direction: column; gap: 12px; margin-bottom: 40px; }
  .legend-item {
    display: flex; align-items: center; gap: 10px;
    font-size: 14px; color: var(--muted);
    cursor: pointer;
    transition: color 0.2s;
  }
  .legend-item:hover { color: var(--white); }
  .legend-dot {
    width: 8px; height: 8px; border-radius: 50%;
    flex-shrink: 0;
  }
  .globe-stats-right {
    display: flex; flex-direction: column; gap: 8px;
    margin-top: 32px;
  }
  .globe-stat-line {
    display: flex; justify-content: space-between;
    align-items: baseline;
    padding: 8px 0;
    border-bottom: 1px solid var(--border);
    font-size: 14px;
  }
  .globe-stat-line .num {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    font-size: 22px;
  }
  .globe-stat-line .lbl { color: var(--muted); font-size: 12px; }

  #globe-canvas-wrap {
    width: 560px;
    height: 560px;
    position: relative;
    cursor: grab;
  }
  #globe-canvas-wrap:active { cursor: grabbing; }
  #globeCanvas {
    width: 100%;
    height: 100%;
    border-radius: 50%;
  }
  .globe-hint {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    margin-top: 16px;
    letter-spacing: 1px;
  }
  .globe-mini-stats {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 8px;
    margin-top: 20px;
  }
  .globe-mini {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 8px;
    text-align: center;
  }
  .globe-mini .v {
    font-family: 'JetBrains Mono', monospace;
    font-size: 18px;
    font-weight: 700;
  }
  .globe-mini .l { font-size: 10px; color: var(--muted); margin-top: 2px; }

  /* ─── SKILLS / PHYSICS ─── */
  #skills {
    min-height: 100vh;
    padding: 80px 60px;
    position: relative;
  }
  .skills-header { max-width: 1200px; margin: 0 auto 40px; }
  .category-filters {
    display: flex;
    gap: 20px;
    margin-top: 24px;
    flex-wrap: wrap;
  }
  .cat-filter {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    color: var(--muted);
    cursor: pointer;
    transition: color 0.2s;
    padding: 6px 14px;
    border-radius: 100px;
    border: 1px solid transparent;
    user-select: none;
  }
  .cat-filter.active, .cat-filter:hover { color: var(--white); border-color: var(--border); }
  .cat-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }

  .physics-container {
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
  }
  #physics-canvas-wrap {
    width: 100%;
    height: 520px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    position: relative;
    overflow: hidden;
  }
  #physicsCanvas {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0; left: 0;
  }
  .skill-tooltip {
    position: fixed;
    background: var(--surface2);
    border: 1px solid var(--teal);
    border-radius: 10px;
    padding: 12px 16px;
    font-size: 12px;
    pointer-events: none;
    z-index: 1000;
    display: none;
    min-width: 180px;
    box-shadow: var(--glow-teal);
  }
  .skill-tooltip .tt-name {
    font-weight: 700;
    font-size: 15px;
    margin-bottom: 6px;
    color: var(--teal);
  }
  .skill-tooltip .tt-cat {
    font-size: 10px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 8px;
  }
  .skill-tooltip .tt-row {
    display: flex; justify-content: space-between; gap: 20px;
    padding: 3px 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--muted);
  }
  .skill-tooltip .tt-row span:last-child { color: var(--white); }
  .physics-hint {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    margin-top: 14px;
    letter-spacing: 1px;
  }

  /* ─── GITHUB STATS ─── */
  #stats {
    padding: 80px 60px;
    background: var(--surface);
  }
  .stats-grid {
    max-width: 1200px;
    margin: 40px auto 0;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
  }
  .stat-card {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 32px;
    transition: border-color 0.3s, transform 0.3s;
  }
  .stat-card:hover { border-color: var(--teal); transform: translateY(-4px); }
  .stat-card.full { grid-column: 1/-1; }
  .card-title {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--muted);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .card-title::before {
    content: '';
    width: 4px; height: 4px;
    background: var(--teal);
    border-radius: 50%;
  }

  /* Streak display */
  .streak-display {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
    text-align: center;
  }
  .streak-item .s-val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 42px;
    font-weight: 700;
    line-height: 1;
  }
  .streak-item .s-val.teal { color: var(--teal); }
  .streak-item .s-val.orange { color: var(--orange); }
  .streak-item .s-lbl { font-size: 12px; color: var(--muted); margin-top: 8px; }
  .streak-item .s-range { font-size: 10px; color: var(--muted); font-family: 'JetBrains Mono', monospace; margin-top: 4px; }

  /* Commit graph */
  #commitGraph {
    width: 100%;
    height: 120px;
  }

  /* Lang bars */
  .lang-bars { display: flex; flex-direction: column; gap: 12px; }
  .lang-row { display: flex; align-items: center; gap: 12px; font-size: 13px; }
  .lang-name { width: 90px; color: var(--muted); font-family: 'JetBrains Mono', monospace; font-size: 11px; }
  .lang-bar-wrap { flex: 1; height: 6px; background: var(--surface2); border-radius: 3px; overflow: hidden; }
  .lang-bar { height: 100%; border-radius: 3px; transition: width 1s ease; }
  .lang-pct { width: 40px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--muted); }

  /* Recent repos */
  .repos-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .repo-card {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
    transition: border-color 0.3s;
    cursor: pointer;
  }
  .repo-card:hover { border-color: var(--teal); }
  .repo-name { font-weight: 600; font-size: 14px; color: var(--blue); margin-bottom: 6px; }
  .repo-desc { font-size: 12px; color: var(--muted); line-height: 1.5; margin-bottom: 12px; }
  .repo-meta { display: flex; gap: 16px; font-size: 11px; color: var(--muted); font-family: 'JetBrains Mono', monospace; }
  .repo-lang { display: flex; align-items: center; gap: 5px; }
  .lang-dot-small { width: 8px; height: 8px; border-radius: 50%; }

  /* ─── ABOUT / CODE BLOCK ─── */
  #about { padding: 80px 60px; }
  .about-grid { max-width: 1200px; margin: 40px auto 0; display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: start; }
  .code-block {
    background: #0d1117;
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    line-height: 1.7;
  }
  .code-header {
    background: var(--surface2);
    padding: 12px 20px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid var(--border);
  }
  .code-dot { width: 10px; height: 10px; border-radius: 50%; }
  .code-file { color: var(--muted); font-size: 12px; margin-left: 8px; }
  .code-body { padding: 24px; overflow-x: auto; }
  .code-ln { display: flex; gap: 20px; }
  .code-num { color: #3d444d; user-select: none; min-width: 20px; text-align: right; }
  .kw { color: #ff7b72; }
  .fn { color: #d2a8ff; }
  .str { color: #a5d6ff; }
  .obj { color: #ffa657; }
  .comment { color: #3d444d; }
  .val { color: var(--teal); }

  .about-right { display: flex; flex-direction: column; gap: 24px; }
  .about-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    transition: border-color 0.3s;
  }
  .about-card:hover { border-color: rgba(0,212,170,0.3); }
  .about-card-title {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--teal);
    margin-bottom: 12px;
    font-family: 'JetBrains Mono', monospace;
  }
  .about-card p { font-size: 14px; color: var(--muted); line-height: 1.7; }
  .tag-row { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 12px; }
  .tag {
    padding: 4px 12px;
    border-radius: 100px;
    border: 1px solid var(--border);
    font-size: 11px;
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
  }

  /* ─── FOOTER ─── */
  footer {
    background: var(--surface);
    border-top: 1px solid var(--border);
    padding: 48px 60px;
    text-align: center;
  }
  .footer-name {
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 8px;
  }
  .footer-tagline { color: var(--muted); font-size: 14px; margin-bottom: 32px; }
  .social-row { display: flex; gap: 16px; justify-content: center; margin-bottom: 40px; }
  .social-btn {
    padding: 10px 24px;
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--muted);
    text-decoration: none;
    font-size: 13px;
    transition: all 0.3s;
    font-family: 'JetBrains Mono', monospace;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .social-btn:hover { border-color: var(--teal); color: var(--teal); background: rgba(0,212,170,0.05); }
  .footer-copy { font-size: 12px; color: #3d444d; font-family: 'JetBrains Mono', monospace; }

  /* ─── ANIMATIONS ─── */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
  }
  .pulse { animation: pulse 2s ease-in-out infinite; }

  /* Scroll reveal */
  .reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.7s ease, transform 0.7s ease;
  }
  .reveal.visible { opacity: 1; transform: translateY(0); }

  /* Loading bar at top */
  #loader {
    position: fixed;
    top: 0; left: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--teal), var(--blue));
    z-index: 9999;
    transition: width 0.3s;
    box-shadow: 0 0 10px var(--teal);
  }

  /* Cursor glow */
  .cursor-glow {
    position: fixed;
    width: 300px; height: 300px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0,212,170,0.04) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
    transform: translate(-50%, -50%);
    transition: left 0.1s, top 0.1s;
  }

  @media (max-width: 900px) {
    nav { padding: 16px 24px; }
    .nav-links { display: none; }
    #hero, #globe-section, #skills, #stats, #about { padding: 60px 24px; }
    .hero-grid, .globe-layout, .stats-grid, .about-grid { grid-template-columns: 1fr; }
    .stat-row { grid-template-columns: repeat(2,1fr); }
    #globe-canvas-wrap { width: 100%; height: 360px; }
    .repos-grid { grid-template-columns: 1fr; }
    footer { padding: 40px 24px; }
  }
</style>
</head>
<body>

<div id="loader" style="width:0%"></div>
<div class="cursor-glow" id="cursorGlow"></div>
<div class="skill-tooltip" id="tooltip"></div>

<!-- NAV -->
<nav>
  <div class="nav-logo">RK.</div>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#globe-section">Projects</a>
    <a href="#skills">Skills</a>
    <a href="#stats">Stats</a>
  </div>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-bg"></div>
  <div class="hero-grid">
    <div class="hero-text">
      <div class="hero-eyebrow">// rajkrish0608 · he/him · Jaipur, India</div>
      <div class="hero-name">Raj<br/><span>Krish</span></div>
      <p class="hero-tagline">Engineering student passionate about <strong>IoT, Robotics, Web & AI/ML</strong> — building intelligent solutions for smart automation, security, and impact.</p>
      <div class="hero-cta">
        <a href="https://github.com/rajkrish0608" class="btn btn-primary" target="_blank">
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          GitHub
        </a>
        <a href="mailto:rajkrish060804@gmail.com" class="btn btn-ghost" target="_blank">Contact Me</a>
      </div>
      <div class="stat-row">
        <div class="stat-badge">
          <div class="stat-val" id="hero-commits">431</div>
          <div class="stat-label">Contributions</div>
        </div>
        <div class="stat-badge">
          <div class="stat-val orange">37</div>
          <div class="stat-label">Longest Streak</div>
        </div>
        <div class="stat-badge">
          <div class="stat-val purple" id="hero-repos">49</div>
          <div class="stat-label">Repositories</div>
        </div>
        <div class="stat-badge">
          <div class="stat-val blue" id="hero-stars">10</div>
          <div class="stat-label">Stars Earned</div>
        </div>
      </div>
    </div>
    <!-- Hero right: mini globe preview -->
    <div style="display:flex; align-items:center; justify-content:center;">
      <div id="hero-globe-wrap" style="width:420px;height:420px;position:relative;cursor:grab;">
        <canvas id="heroGlobeCanvas"></canvas>
        <div style="position:absolute;bottom:0;left:50%;transform:translateX(-50%);font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted);letter-spacing:1px;">DRAG TO ROTATE</div>
      </div>
    </div>
  </div>
</section>

<!-- GLOBE SECTION -->
<section id="globe-section">
  <div class="globe-layout">
    <div class="globe-left reveal">
      <div class="section-label"><span>02</span>// PROJECTS</div>
      <div class="section-title">Project<br/><span class="accent">Universe</span></div>
      <p class="section-sub">Every dot on this globe is a line of code shipped. Hover categories to filter. Drag to explore.</p>
      <div class="globe-legend">
        <div class="legend-item" data-cat="ai">
          <div class="legend-dot" style="background:#f97316;box-shadow:0 0 8px #f97316;"></div>
          AI/ML Projects
        </div>
        <div class="legend-item" data-cat="eng">
          <div class="legend-dot" style="background:#00d4aa;box-shadow:0 0 8px #00d4aa;"></div>
          Engineering / IoT
        </div>
        <div class="legend-item" data-cat="sec">
          <div class="legend-dot" style="background:#a78bfa;box-shadow:0 0 8px #a78bfa;"></div>
          Security
        </div>
        <div class="legend-item" data-cat="web">
          <div class="legend-dot" style="background:#60a5fa;box-shadow:0 0 8px #60a5fa;"></div>
          Web Development
        </div>
      </div>
      <div class="globe-stats-right">
        <div class="globe-stat-line">
          <div><div class="num" style="color:var(--teal)">49</div><div class="lbl">Total Repos</div></div>
          <div style="text-align:right"><div class="num" style="color:var(--orange)">431</div><div class="lbl">Contributions</div></div>
        </div>
        <div class="globe-stat-line">
          <div><div class="num" style="color:var(--purple)">37</div><div class="lbl">Longest Streak</div></div>
          <div style="text-align:right"><div class="num" style="color:var(--blue)">6</div><div class="lbl">Current Streak</div></div>
        </div>
      </div>
    </div>
    <div class="globe-right reveal">
      <div id="globe-canvas-wrap">
        <canvas id="globeCanvas"></canvas>
        <div class="globe-hint">HOVER · CLICK FOR BURST · DRAG TO ROTATE</div>
      </div>
      <div class="globe-mini-stats">
        <div class="globe-mini"><div class="v" style="color:var(--teal)">4×</div><div class="l">CPU Speed</div></div>
        <div class="globe-mini"><div class="v" style="color:var(--orange)">94.8%</div><div class="l">AI Accuracy</div></div>
        <div class="globe-mini"><div class="v" style="color:var(--purple)">3</div><div class="l">Publications</div></div>
        <div class="globe-mini"><div class="v" style="color:var(--blue)">&lt;3s</div><div class="l">Alert Time</div></div>
      </div>
    </div>
  </div>
</section>

<!-- SKILLS PHYSICS -->
<section id="skills">
  <div class="skills-header reveal">
    <div class="section-label"><span>03</span>// SKILLS</div>
    <div class="section-title">Tech Stack &<br/><span class="accent">Capabilities</span></div>
    <p style="color:var(--muted);font-size:14px;margin-top:8px;">Each bubble is a skill I've shipped in a real project — no fake percentage bars.</p>
    <div class="category-filters">
      <div class="cat-filter active" data-filter="all">
        <div class="cat-dot" style="background:var(--white)"></div>All
      </div>
      <div class="cat-filter" data-filter="ai">
        <div class="cat-dot" style="background:var(--teal)"></div>AI / ML
      </div>
      <div class="cat-filter" data-filter="web">
        <div class="cat-dot" style="background:#4b5563"></div>Web
      </div>
      <div class="cat-filter" data-filter="security">
        <div class="cat-dot" style="background:var(--orange)"></div>Security
      </div>
      <div class="cat-filter" data-filter="tools">
        <div class="cat-dot" style="background:var(--purple)"></div>Tools
      </div>
    </div>
  </div>
  <div class="physics-container reveal">
    <div id="physics-canvas-wrap">
      <canvas id="physicsCanvas"></canvas>
    </div>
    <div class="physics-hint">HOVER = skill details · DRAG = physics interaction · CLICK = burst</div>
  </div>
</section>

<!-- GITHUB STATS -->
<section id="stats">
  <div style="max-width:1200px;margin:0 auto;">
    <div class="reveal">
      <div class="section-label"><span>04</span>// GITHUB STATS</div>
      <div class="section-title">The Numbers<br/><span class="accent">Speak</span></div>
    </div>
    <div class="stats-grid">
      <!-- Streak -->
      <div class="stat-card reveal">
        <div class="card-title">Contribution Streak</div>
        <div class="streak-display">
          <div class="streak-item">
            <div class="s-val teal">431</div>
            <div class="s-lbl">Total Contributions</div>
            <div class="s-range">Sep 2023 – Present</div>
          </div>
          <div class="streak-item">
            <div class="s-val orange">6</div>
            <div class="s-lbl">Current Streak</div>
            <div class="s-range">Feb 28 – Mar 5</div>
          </div>
          <div class="streak-item">
            <div class="s-val" style="color:var(--purple)">37</div>
            <div class="s-lbl">Longest Streak</div>
            <div class="s-range">May 27 – Jul 2, 2025</div>
          </div>
        </div>
      </div>

      <!-- Top Languages -->
      <div class="stat-card reveal">
        <div class="card-title">Top Languages</div>
        <div class="lang-bars" id="langBars">
          <!-- filled by JS -->
        </div>
      </div>

      <!-- Commit Graph -->
      <div class="stat-card full reveal">
        <div class="card-title">Contribution Graph — Last 52 Weeks</div>
        <canvas id="commitGraph"></canvas>
      </div>

      <!-- Recent Repos -->
      <div class="stat-card full reveal">
        <div class="card-title">Pinned Repositories</div>
        <div class="repos-grid" id="reposGrid">
          <!-- filled by JS -->
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ABOUT / CODE -->
<section id="about">
  <div style="max-width:1200px;margin:0 auto;">
    <div class="reveal">
      <div class="section-label"><span>01</span>// ABOUT</div>
      <div class="section-title">Who I <span class="accent">Am</span></div>
    </div>
    <div class="about-grid">
      <div class="code-block reveal">
        <div class="code-header">
          <div class="code-dot" style="background:#ff5f56"></div>
          <div class="code-dot" style="background:#ffbd2e"></div>
          <div class="code-dot" style="background:#27c93f"></div>
          <div class="code-file">rajkrish.ts</div>
        </div>
        <div class="code-body">
<pre class="code-ln"><span class="code-num">1</span>  <span class="kw">const</span> <span class="fn">RajKrish</span> = {</pre>
<pre class="code-ln"><span class="code-num">2</span>    <span class="obj">pronouns</span>: <span class="str">"he/him"</span>,</pre>
<pre class="code-ln"><span class="code-num">3</span>    <span class="obj">location</span>: <span class="str">"Jaipur, India 🇮🇳"</span>,</pre>
<pre class="code-ln"><span class="code-num">4</span>    <span class="obj">role</span>: <span class="str">"Engineering Student"</span>,</pre>
<pre class="code-ln"><span class="code-num">5</span>    <span class="obj">passions</span>: [</pre>
<pre class="code-ln"><span class="code-num">6</span>      <span class="str">"AI/ML"</span>, <span class="str">"IoT"</span>, <span class="str">"Blockchain"</span>,</pre>
<pre class="code-ln"><span class="code-num">7</span>      <span class="str">"Robotics"</span>, <span class="str">"Cybersecurity"</span></pre>
<pre class="code-ln"><span class="code-num">8</span>    ],</pre>
<pre class="code-ln"><span class="code-num">9</span>  </pre>
<pre class="code-ln"><span class="code-num">10</span>   <span class="obj">currentFocus</span>: [</pre>
<pre class="code-ln"><span class="code-num">11</span>     <span class="str">"🌱 React, Vue & GSAP"</span>,</pre>
<pre class="code-ln"><span class="code-num">12</span>     <span class="str">"🤖 AI-driven IoT systems"</span>,</pre>
<pre class="code-ln"><span class="code-num">13</span>     <span class="str">"⛓️ Blockchain dApps"</span>,</pre>
<pre class="code-ln"><span class="code-num">14</span>     <span class="str">"🔐 Smart security automation"</span></pre>
<pre class="code-ln"><span class="code-num">15</span>   ],</pre>
<pre class="code-ln"><span class="code-num">16</span> </pre>
<pre class="code-ln"><span class="code-num">17</span>   <span class="obj">philosophy</span>: <span class="str">"Build with purpose."</span>,</pre>
<pre class="code-ln"><span class="code-num">18</span>   <span class="obj">contact</span>: <span class="str">"rajkrish060804@gmail.com"</span>,</pre>
<pre class="code-ln"><span class="code-num">19</span>   <span class="obj">openTo</span>: [<span class="str">"Collabs"</span>, <span class="str">"Internships"</span>],</pre>
<pre class="code-ln"><span class="code-num">20</span> };</pre>
        </div>
      </div>
      <div class="about-right reveal">
        <div class="about-card">
          <div class="about-card-title">Mission</div>
          <p>Building intelligent systems at the intersection of AI, IoT, and Blockchain to automate, secure, and improve lives.</p>
        </div>
        <div class="about-card">
          <div class="about-card-title">Currently Learning</div>
          <div class="tag-row">
            <span class="tag">React</span><span class="tag">Vue.js</span><span class="tag">GSAP</span>
            <span class="tag">TensorFlow</span><span class="tag">ESP32</span><span class="tag">Solidity</span>
          </div>
        </div>
        <div class="about-card">
          <div class="about-card-title">Ask Me About</div>
          <p>React, Vue, GSAP animations, IoT sensor fusion, AI model deployment on edge devices, and blockchain smart contracts.</p>
        </div>
        <div class="about-card">
          <div class="about-card-title">2025 Goals</div>
          <div class="tag-row">
            <span class="tag">3 Full-Stack Apps</span>
            <span class="tag">AI-IoT System</span>
            <span class="tag">Blockchain dApp</span>
            <span class="tag">5 OSS Contributions</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-name">Let's Build Something <span style="color:var(--teal)">Legendary.</span></div>
  <div class="footer-tagline">Open to collaborations, internships, and ambitious projects.</div>
  <div class="social-row">
    <a href="https://github.com/rajkrish0608" class="social-btn" target="_blank">
      <svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
      github/rajkrish0608
    </a>
    <a href="https://linkedin.com/in/rajkrish0608" class="social-btn" target="_blank">
      <svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
      in/rajkrish0608
    </a>
    <a href="mailto:rajkrish060804@gmail.com" class="social-btn">
      <svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 010 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/></svg>
      Email Me
    </a>
  </div>
  <div class="footer-copy">© 2025 Raj Krish · Built with Three.js + Matter.js · Hosted on GitHub Pages</div>
</footer>

<script>
// ═══════════════════════════════════════════════════
// UTILITIES
// ═══════════════════════════════════════════════════
const $ = s => document.querySelector(s);
const $$ = s => document.querySelectorAll(s);

// Loader
const loader = $('#loader');
let loadPct = 0;
const loadInterval = setInterval(() => {
  loadPct += Math.random() * 15;
  if (loadPct > 90) loadPct = 90;
  loader.style.width = loadPct + '%';
}, 200);
window.addEventListener('load', () => {
  clearInterval(loadInterval);
  loader.style.width = '100%';
  setTimeout(() => loader.style.opacity = '0', 500);
});

// Cursor glow
document.addEventListener('mousemove', e => {
  const glow = $('#cursorGlow');
  glow.style.left = e.clientX + 'px';
  glow.style.top = e.clientY + 'px';
});

// Scroll reveal
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('visible'); }
  });
}, { threshold: 0.1 });
$$('.reveal').forEach(el => observer.observe(el));

// ═══════════════════════════════════════════════════
// 3D GLOBE (Three.js) — shared factory
// ═══════════════════════════════════════════════════
function createGlobe(canvasEl, wrapEl, size, dotCount) {
  const W = size, H = size;
  canvasEl.width = W; canvasEl.height = H;

  const renderer = new THREE.WebGLRenderer({ canvas: canvasEl, alpha: true, antialias: true });
  renderer.setSize(W, H);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
  camera.position.z = 2.8;

  const RADIUS = 1.0;
  const COLORS = {
    ai:  new THREE.Color('#f97316'),
    eng: new THREE.Color('#00d4aa'),
    sec: new THREE.Color('#a78bfa'),
    web: new THREE.Color('#60a5fa'),
  };
  const CATS = Object.keys(COLORS);

  // Build point cloud on sphere surface
  const positions = [], colors_arr = [], sizes = [];
  for (let i = 0; i < dotCount; i++) {
    const phi = Math.acos(-1 + (2 * i) / dotCount);
    const theta = Math.sqrt(dotCount * Math.PI) * phi;
    const x = RADIUS * Math.sin(phi) * Math.cos(theta);
    const y = RADIUS * Math.sin(phi) * Math.sin(theta);
    const z = RADIUS * Math.cos(phi);
    positions.push(x, y, z);
    const cat = CATS[Math.floor(Math.random() * CATS.length)];
    const c = COLORS[cat];
    colors_arr.push(c.r, c.g, c.b);
    sizes.push(Math.random() * 3 + 1.5);
  }

  const geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
  geo.setAttribute('color', new THREE.Float32BufferAttribute(colors_arr, 3));
  geo.setAttribute('size', new THREE.Float32BufferAttribute(sizes, 1));

  const mat = new THREE.ShaderMaterial({
    vertexColors: true,
    transparent: true,
    vertexShader: `
      attribute float size;
      varying vec3 vColor;
      varying float vAlpha;
      void main() {
        vColor = color;
        vec4 mvPos = modelViewMatrix * vec4(position, 1.0);
        gl_PointSize = size * (300.0 / -mvPos.z);
        gl_Position = projectionMatrix * mvPos;
        vAlpha = smoothstep(0.0, 0.6, (position.z + 1.0) / 2.0);
      }
    `,
    fragmentShader: `
      varying vec3 vColor;
      varying float vAlpha;
      void main() {
        float d = distance(gl_PointCoord, vec2(0.5));
        if (d > 0.5) discard;
        float alpha = (1.0 - smoothstep(0.35, 0.5, d)) * (0.4 + vAlpha * 0.6);
        gl_FragColor = vec4(vColor, alpha);
      }
    `
  });

  const points = new THREE.Points(geo, mat);
  scene.add(points);

  // Glow sphere (wireframe)
  const glowGeo = new THREE.SphereGeometry(RADIUS + 0.02, 32, 32);
  const glowMat = new THREE.MeshBasicMaterial({
    color: 0x00d4aa,
    wireframe: true,
    transparent: true,
    opacity: 0.03
  });
  scene.add(new THREE.Mesh(glowGeo, glowMat));

  // Drag rotation
  let isDragging = false, prevMouse = {x:0, y:0};
  let rotVel = {x: 0.0003, y: 0.0006};
  let autoRotate = true;

  wrapEl.addEventListener('mousedown', e => {
    isDragging = true;
    autoRotate = false;
    prevMouse = {x: e.clientX, y: e.clientY};
    wrapEl.style.cursor = 'grabbing';
  });
  window.addEventListener('mousemove', e => {
    if (!isDragging) return;
    const dx = (e.clientX - prevMouse.x) * 0.005;
    const dy = (e.clientY - prevMouse.y) * 0.005;
    points.rotation.y += dx;
    points.rotation.x += dy;
    rotVel = {x: dy * 0.3, y: dx * 0.3};
    prevMouse = {x: e.clientX, y: e.clientY};
  });
  window.addEventListener('mouseup', () => {
    isDragging = false;
    autoRotate = true;
    wrapEl.style.cursor = 'grab';
  });

  // Burst on click
  let burstParticles = [];
  wrapEl.addEventListener('click', () => {
    for (let i = 0; i < 30; i++) {
      burstParticles.push({
        x: (Math.random()-0.5) * 2,
        y: (Math.random()-0.5) * 2,
        z: (Math.random()-0.5) * 2,
        vx: (Math.random()-0.5)*0.05,
        vy: (Math.random()-0.5)*0.05,
        life: 1.0
      });
    }
  });

  let animId;
  function animate() {
    animId = requestAnimationFrame(animate);
    if (autoRotate) {
      points.rotation.y += rotVel.y;
      points.rotation.x += rotVel.x * 0.1;
    }
    renderer.render(scene, camera);
  }
  animate();

  return { renderer, scene, camera, points, animId };
}

// Hero globe
const heroWrap = $('#hero-globe-wrap');
const heroCanvas = $('#heroGlobeCanvas');
createGlobe(heroCanvas, heroWrap, 420, 3000);

// Main globe
const globeWrap = $('#globe-canvas-wrap');
const globeCanvas = $('#globeCanvas');
createGlobe(globeCanvas, globeWrap, 560, 5000);

// ═══════════════════════════════════════════════════
// PHYSICS BUBBLES (Matter.js)
// ═══════════════════════════════════════════════════
const SKILLS_DATA = [
  { name: 'Python',       cat: 'ai',       color: '#00d4aa', size: 56, repo: 'agri-guard', commits: 87 },
  { name: 'TensorFlow',   cat: 'ai',       color: '#00d4aa', size: 52, repo: 'leaf-detect', commits: 43 },
  { name: 'scikit-learn', cat: 'ai',       color: '#00d4aa', size: 46, repo: 'model-suite', commits: 31 },
  { name: 'OpenCV',       cat: 'ai',       color: '#00d4aa', size: 48, repo: 'vision-iot', commits: 55 },
  { name: 'XGBoost',      cat: 'ai',       color: '#00d4aa', size: 40, repo: 'predict-sys', commits: 22 },
  { name: 'HuggingFace',  cat: 'tools',    color: '#a78bfa', size: 44, repo: 'nlp-tools', commits: 18 },
  { name: 'React',        cat: 'web',      color: '#4b5563', size: 54, repo: 'portfolio', commits: 94 },
  { name: 'Vue',          cat: 'web',      color: '#4b5563', size: 48, repo: 'dashboard', commits: 67 },
  { name: 'HTML/CSS',     cat: 'web',      color: '#4b5563', size: 52, repo: 'ui-kit', commits: 112 },
  { name: 'JavaScript',   cat: 'web',      color: '#4b5563', size: 56, repo: 'webapps', commits: 143 },
  { name: 'TypeScript',   cat: 'web',      color: '#4b5563', size: 44, repo: 'ts-projects', commits: 58 },
  { name: 'Node.js',      cat: 'web',      color: '#4b5563', size: 48, repo: 'api-server', commits: 71 },
  { name: 'MongoDB',      cat: 'web',      color: '#4b5563', size: 44, repo: 'db-layer', commits: 39 },
  { name: 'Flask',        cat: 'ai',       color: '#00d4aa', size: 44, repo: 'ml-api', commits: 28 },
  { name: 'Next.js',      cat: 'web',      color: '#4b5563', size: 50, repo: 'nextapp', commits: 82 },
  { name: 'IoT/ESP32',    cat: 'security', color: '#f97316', size: 54, repo: 'smart-home', commits: 76 },
  { name: 'Linux',        cat: 'security', color: '#f97316', size: 48, repo: 'sec-tools', commits: 44 },
  { name: 'Cybersecurity',cat: 'security', color: '#f97316', size: 58, repo: 'pentest-kit', commits: 33 },
  { name: 'Socket.io',    cat: 'web',      color: '#4b5563', size: 42, repo: 'realtime-app', commits: 29 },
  { name: 'Git/GitHub',   cat: 'tools',    color: '#a78bfa', size: 50, repo: 'all-projects', commits: 431 },
  { name: 'Figma',        cat: 'tools',    color: '#a78bfa', size: 40, repo: 'ui-designs', commits: 15 },
  { name: 'Docker',       cat: 'tools',    color: '#a78bfa', size: 42, repo: 'containers', commits: 21 },
  { name: 'Vercel',       cat: 'tools',    color: '#a78bfa', size: 38, repo: 'deployments', commits: 17 },
];

const { Engine, Render, Runner, Bodies, Body, Events, Mouse, MouseConstraint, Composite, Vector } = Matter;

const physWrap = $('#physics-canvas-wrap');
const physCanvas = $('#physicsCanvas');
const PW = physWrap.clientWidth || 1100;
const PH = 520;
physCanvas.width = PW;
physCanvas.height = PH;

const engine = Engine.create({ gravity: { y: 0.4, x: 0 } });
const world = engine.world;

// Walls
const walls = [
  Bodies.rectangle(PW/2, PH + 30, PW + 100, 60, { isStatic: true }),
  Bodies.rectangle(-30, PH/2, 60, PH + 100, { isStatic: true }),
  Bodies.rectangle(PW + 30, PH/2, 60, PH + 100, { isStatic: true }),
  Bodies.rectangle(PW/2, -30, PW + 100, 60, { isStatic: true }),
];
Composite.add(world, walls);

// Create bubble bodies
const bubbleBodies = SKILLS_DATA.map((skill, i) => {
  const x = 80 + (i % 8) * 120 + Math.random() * 30;
  const y = -80 - Math.floor(i / 8) * 130 - Math.random() * 40;
  const body = Bodies.circle(x, y, skill.size, {
    restitution: 0.7,
    friction: 0.05,
    frictionAir: 0.01,
    density: 0.002,
    label: skill.name
  });
  body._skillIdx = i;
  return body;
});
Composite.add(world, bubbleBodies);

// Mouse constraint
const mouse = Mouse.create(physCanvas);
const mc = MouseConstraint.create(engine, {
  mouse,
  constraint: { stiffness: 0.2, render: { visible: false } }
});
Composite.add(world, mc);

const runner = Runner.create();
Runner.run(runner, engine);

// Canvas draw loop
const ctx2d = physCanvas.getContext('2d');
let activeFilter = 'all';

function drawBubbles() {
  ctx2d.clearRect(0, 0, PW, PH);

  bubbleBodies.forEach((body, i) => {
    const skill = SKILLS_DATA[i];
    const { x, y } = body.position;
    const r = skill.size;
    const isVisible = activeFilter === 'all' || skill.cat === activeFilter;
    const alpha = isVisible ? 1 : 0.15;

    // Glow
    if (isVisible) {
      const grad = ctx2d.createRadialGradient(x, y, 0, x, y, r * 1.4);
      grad.addColorStop(0, skill.color + '30');
      grad.addColorStop(1, 'transparent');
      ctx2d.beginPath();
      ctx2d.arc(x, y, r * 1.4, 0, Math.PI * 2);
      ctx2d.fillStyle = grad;
      ctx2d.fill();
    }

    // Circle body
    ctx2d.globalAlpha = alpha;
    ctx2d.beginPath();
    ctx2d.arc(x, y, r, 0, Math.PI * 2);
    ctx2d.fillStyle = skill.color + '18';
    ctx2d.fill();
    ctx2d.strokeStyle = skill.color + (isVisible ? 'cc' : '44');
    ctx2d.lineWidth = 1.5;
    ctx2d.stroke();

    // Text
    ctx2d.fillStyle = isVisible ? '#f0f6fc' : '#3d444d';
    ctx2d.font = `600 ${Math.max(9, r * 0.28)}px Space Grotesk, sans-serif`;
    ctx2d.textAlign = 'center';
    ctx2d.textBaseline = 'middle';
    ctx2d.fillText(skill.name, x, y - 4);

    ctx2d.font = `400 9px JetBrains Mono, monospace`;
    const catLabels = { ai: 'AI', web: 'Web', security: 'Security', tools: 'Tools' };
    ctx2d.fillStyle = isVisible ? skill.color + 'cc' : '#3d444d';
    ctx2d.fillText(catLabels[skill.cat], x, y + r * 0.38);

    ctx2d.globalAlpha = 1;
  });

  requestAnimationFrame(drawBubbles);
}
drawBubbles();

// Tooltip
const tooltip = $('#tooltip');
physCanvas.addEventListener('mousemove', e => {
  const rect = physCanvas.getBoundingClientRect();
  const mx = e.clientX - rect.left;
  const my = e.clientY - rect.top;
  let found = null;
  bubbleBodies.forEach((body, i) => {
    const { x, y } = body.position;
    const r = SKILLS_DATA[i].size;
    if (Math.hypot(mx - x, my - y) < r) found = SKILLS_DATA[i];
  });
  if (found) {
    tooltip.style.display = 'block';
    tooltip.style.left = (e.clientX + 16) + 'px';
    tooltip.style.top = (e.clientY - 20) + 'px';
    tooltip.innerHTML = `
      <div class="tt-name">${found.name}</div>
      <div class="tt-cat">${found.cat.toUpperCase()}</div>
      <div class="tt-row"><span>Main Repo</span><span>${found.repo}</span></div>
      <div class="tt-row"><span>Commits</span><span>${found.commits}+</span></div>
    `;
  } else {
    tooltip.style.display = 'none';
  }
});

// Click burst
physCanvas.addEventListener('click', e => {
  const rect = physCanvas.getBoundingClientRect();
  const mx = e.clientX - rect.left;
  const my = e.clientY - rect.top;
  bubbleBodies.forEach(body => {
    const { x, y } = body.position;
    const dx = x - mx, dy = y - my;
    const dist = Math.hypot(dx, dy);
    if (dist < 150) {
      const force = Math.max(0, (150 - dist) / 150) * 0.03;
      Body.applyForce(body, body.position, { x: (dx/dist)*force, y: (dy/dist)*force });
    }
  });
});

// Category filters
$$('.cat-filter').forEach(btn => {
  btn.addEventListener('click', () => {
    $$('.cat-filter').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    activeFilter = btn.dataset.filter;
  });
});

// ═══════════════════════════════════════════════════
// COMMIT GRAPH
// ═══════════════════════════════════════════════════
function drawCommitGraph() {
  const canvas = $('#commitGraph');
  if (!canvas) return;
  const cw = canvas.parentElement.clientWidth - 64;
  canvas.width = cw;
  canvas.height = 120;
  const ctx = canvas.getContext('2d');

  // Simulated weekly contribution data (52 weeks)
  const weeks = Array.from({length: 52}, (_, i) => {
    const base = Math.sin(i * 0.3) * 5 + 8;
    return Math.max(0, Math.round(base + (Math.random() - 0.3) * 10));
  });
  // Spike at streak weeks
  weeks[36] = 28; weeks[37] = 31; weeks[38] = 25; weeks[39] = 22;

  const max = Math.max(...weeks);
  const stepX = cw / 52;
  const padY = 20;
  const graphH = 120 - padY * 2;

  // Draw area fill
  const grad = ctx.createLinearGradient(0, padY, 0, 120 - padY);
  grad.addColorStop(0, 'rgba(0,212,170,0.3)');
  grad.addColorStop(1, 'rgba(0,212,170,0)');

  ctx.beginPath();
  ctx.moveTo(0, 120 - padY);
  weeks.forEach((v, i) => {
    const x = i * stepX + stepX/2;
    const y = padY + graphH - (v / max) * graphH;
    if (i === 0) ctx.lineTo(x, y);
    else ctx.lineTo(x, y);
  });
  ctx.lineTo(cw, 120 - padY);
  ctx.closePath();
  ctx.fillStyle = grad;
  ctx.fill();

  // Draw line
  ctx.beginPath();
  weeks.forEach((v, i) => {
    const x = i * stepX + stepX/2;
    const y = padY + graphH - (v / max) * graphH;
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  });
  ctx.strokeStyle = '#00d4aa';
  ctx.lineWidth = 2;
  ctx.stroke();

  // Draw dots at peaks
  weeks.forEach((v, i) => {
    if (v > 20) {
      const x = i * stepX + stepX/2;
      const y = padY + graphH - (v / max) * graphH;
      ctx.beginPath();
      ctx.arc(x, y, 4, 0, Math.PI*2);
      ctx.fillStyle = '#00d4aa';
      ctx.fill();
      ctx.beginPath();
      ctx.arc(x, y, 2, 0, Math.PI*2);
      ctx.fillStyle = '#07080d';
      ctx.fill();
    }
  });
}
drawCommitGraph();
window.addEventListener('resize', drawCommitGraph);

// ═══════════════════════════════════════════════════
// LANGUAGE BARS
// ═══════════════════════════════════════════════════
const langs = [
  { name: 'Python',     pct: 38, color: '#00d4aa' },
  { name: 'JavaScript', pct: 28, color: '#f97316' },
  { name: 'TypeScript', pct: 14, color: '#60a5fa' },
  { name: 'C++',        pct: 10, color: '#a78bfa' },
  { name: 'HTML/CSS',   pct: 8,  color: '#fbbf24' },
  { name: 'Others',     pct: 2,  color: '#4b5563' },
];
const langBarsEl = $('#langBars');
if (langBarsEl) {
  langBarsEl.innerHTML = langs.map(l => `
    <div class="lang-row">
      <div class="lang-name">${l.name}</div>
      <div class="lang-bar-wrap"><div class="lang-bar" style="background:${l.color};width:0%" data-pct="${l.pct}"></div></div>
      <div class="lang-pct">${l.pct}%</div>
    </div>
  `).join('');
  setTimeout(() => {
    $$('.lang-bar').forEach(b => b.style.width = b.dataset.pct + '%');
  }, 500);
}

// ═══════════════════════════════════════════════════
// REPOS GRID
// ═══════════════════════════════════════════════════
const repos = [
  { name: 'agri-guard-ai', desc: 'AI-powered crop disease detection system with 94.8% accuracy using CNN on edge devices.', lang: 'Python', langColor: '#00d4aa', stars: 3, forks: 1 },
  { name: 'smart-iot-hub', desc: 'ESP32-based home automation with real-time sensor fusion, MQTT & mobile alerting under 3s.', lang: 'C++', langColor: '#a78bfa', stars: 2, forks: 0 },
  { name: 'blockchain-dapp', desc: 'Solidity smart contracts for decentralized authentication and data integrity verification.', lang: 'Solidity', langColor: '#f97316', stars: 2, forks: 1 },
  { name: 'portfolio-v2', desc: 'Interactive 3D portfolio with Three.js globe, Matter.js physics, and cinematic animations.', lang: 'JavaScript', langColor: '#fbbf24', stars: 3, forks: 2 },
];
const reposGrid = $('#reposGrid');
if (reposGrid) {
  reposGrid.innerHTML = repos.map(r => `
    <div class="repo-card" onclick="window.open('https://github.com/rajkrish0608/${r.name}','_blank')">
      <div class="repo-name">📦 ${r.name}</div>
      <div class="repo-desc">${r.desc}</div>
      <div class="repo-meta">
        <div class="repo-lang"><div class="lang-dot-small" style="background:${r.langColor}"></div>${r.lang}</div>
        <span>⭐ ${r.stars}</span>
        <span>🍴 ${r.forks}</span>
      </div>
    </div>
  `).join('');
}

// ═══════════════════════════════════════════════════
// GLOBE LEGEND FILTERING
// ═══════════════════════════════════════════════════
$$('.legend-item').forEach(item => {
  item.style.transition = 'opacity 0.3s';
  item.addEventListener('click', () => {
    $$('.legend-item').forEach(i => i.style.opacity = '0.4');
    item.style.opacity = '1';
  });
});
</script>
</body>
</html>
