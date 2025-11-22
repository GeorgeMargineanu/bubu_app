import streamlit as st
import random
import base64
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(page_title="Magic Love App", page_icon="❤️", layout="wide")

st.title("💘 Magic Love App 💘")
st.write("Type a name and see what happens... 😉")

name = st.text_input("Enter a name:")


def get_img_base64(image_path: str) -> str:
    """Read image and return base64-encoded string."""
    img_bytes = Path(image_path).read_bytes()
    return base64.b64encode(img_bytes).decode("utf-8")


if name.strip().lower() == "bubu":
    # Encode the local image as base64 so we can embed it in the HTML
    img_b64 = get_img_base64("bubu.jpg")

    html = f"""
    <html>
    <head>
    <style>
      body {{
        margin: 0;
        overflow: hidden;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background: radial-gradient(circle at top, #1a1a2e 0, #000000 60%);
        color: #fff;
      }}

      #container {{
        position: relative;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
      }}

      canvas {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: block;
      }}

      .center-content {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 10;
        color: #ffe6f7;
        text-shadow: 0 0 12px rgba(255, 192, 203, 0.9);
      }}

      .center-content img {{
        border-radius: 20px;
        max-width: 280px;
        box-shadow: 0 0 30px rgba(255, 105, 180, 0.9);
        border: 3px solid rgba(255, 255, 255, 0.8);
      }}

      .title {{
        font-size: 2.3rem;
        margin-top: 18px;
      }}

      .subtitle {{
        font-size: 1.4rem;
        margin-top: 6px;
      }}

      .small-text {{
        font-size: 1rem;
        margin-top: 10px;
        opacity: 0.9;
      }}
    </style>
    </head>
    <body>
    <div id="container">
      <canvas id="fireworksCanvas"></canvas>
      <div class="center-content">
        <img src="data:image/jpeg;base64,{img_b64}" alt="Bubu" />
        <div class="title">💖 Bubu Detected 💖</div>
        <div class="subtitle">Romantic Fireworks Mode: <i>ON</i> 🎆</div>
        <div class="small-text">
          This show is dedicated 100% to Alina.<br/>
          Please enjoy unlimited fireworks, love, and sparkles. ✨
        </div>
      </div>
    </div>

    <script>
    const canvas = document.getElementById('fireworksCanvas');
    const ctx = canvas.getContext('2d');

    let w = window.innerWidth;
    let h = window.innerHeight;
    canvas.width = w;
    canvas.height = h;

    window.addEventListener('resize', () => {{
      w = window.innerWidth;
      h = window.innerHeight;
      canvas.width = w;
      canvas.height = h;
    }});

    // Utility for random numbers
    function rand(min, max) {{
      return Math.random() * (max - min) + min;
    }}

    const colors = [
      '#ff9a9e',
      '#fad0c4',
      '#fbc2eb',
      '#a18cd1',
      '#f6d365',
      '#fda085',
      '#84fab0',
      '#8fd3f4'
    ];

    class Particle {{
      constructor(x, y, color) {{
        this.x = x;
        this.y = y;
        const angle = rand(0, Math.PI * 2);
        const speed = rand(2, 6);
        this.vx = Math.cos(angle) * speed;
        this.vy = Math.sin(angle) * speed;
        this.alpha = 1;
        this.decay = rand(0.01, 0.03);
        this.color = color;
        this.size = rand(2, 4);
        this.gravity = 0.05;
      }}

      update() {{
        this.vy += this.gravity;
        this.x += this.vx;
        this.y += this.vy;
        this.alpha -= this.decay;
      }}

      draw(ctx) {{
        ctx.save();
        ctx.globalAlpha = this.alpha;
        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }}

      isDead() {{
        return this.alpha <= 0;
      }}
    }}

    class Firework {{
      constructor() {{
        this.x = rand(w * 0.1, w * 0.9);
        this.y = h + 10;
        this.targetY = rand(h * 0.2, h * 0.5);
        this.speed = rand(7, 10);
        this.color = colors[Math.floor(Math.random() * colors.length)];
        this.exploded = false;
        this.particles = [];
      }}

      update() {{
        if (!this.exploded) {{
          this.y -= this.speed;
          if (this.y <= this.targetY) {{
            this.exploded = true;
            // create particles
            const count = 80;
            for (let i = 0; i < count; i++) {{
              this.particles.push(new Particle(this.x, this.y, this.color));
            }}
          }}
        }} else {{
          this.particles.forEach(p => p.update());
          this.particles = this.particles.filter(p => !p.isDead());
        }}
      }}

      draw(ctx) {{
        if (!this.exploded) {{
          ctx.save();
          ctx.beginPath();
          ctx.fillStyle = this.color;
          ctx.arc(this.x, this.y, 3, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();
        }}
        this.particles.forEach(p => p.draw(ctx));
      }}

      isDone() {{
        return this.exploded && this.particles.length === 0;
      }}
    }}

    let fireworks = [];
    let lastLaunch = 0;
    const launchInterval = 600; // ms

    function animate(timestamp) {{
      requestAnimationFrame(animate);

      // Clear with slight trail
      ctx.fillStyle = 'rgba(0, 0, 0, 0.20)';
      ctx.fillRect(0, 0, w, h);

      // Launch new fireworks
      if (!lastLaunch) lastLaunch = timestamp;
      const elapsed = timestamp - lastLaunch;
      if (elapsed > launchInterval) {{
        fireworks.push(new Firework());
        fireworks.push(new Firework());
        lastLaunch = timestamp;
      }}

      // Update & draw all fireworks
      fireworks.forEach(fw => {{
        fw.update();
        fw.draw(ctx);
      }});

      // Remove dead fireworks
      fireworks = fireworks.filter(fw => !fw.isDone());
    }}

    requestAnimationFrame(animate);
    </script>
    </body>
    </html>
    """

    # Render the whole fireworks scene as a component
    components.html(html, height=700, width=None)

else:
    st.write("Write **'Bubu'** to unleash REAL fireworks and true magic 💘")
