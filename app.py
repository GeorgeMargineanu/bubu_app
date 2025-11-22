import streamlit as st
import random

st.set_page_config(page_title="Magic Love App", page_icon="❤️", layout="wide")

st.title("💘 Magic Love App 💘")
st.write("Type a name and see what happens... 😉")

name = st.text_input("Enter a name:")

# ================== CSS for EPIC ANIMATIONS ==================
css = """
<style>
/* Nice gradient background */
.stApp {
  background: radial-gradient(circle at top, #ffdde1 0, #ee9ca7 35%, #4b134f 100%);
  color: white;
}

/* Center text nicely */
h1, h2, h3, p {
  text-align: center;
}

/* Floating hearts */
.heart {
  position: fixed;
  animation: floatUp 6s linear infinite;
  opacity: 0.9;
  z-index: 5;
}

@keyframes floatUp {
  0% { transform: translateY(0px) scale(1); opacity: 1; }
  100% { transform: translateY(-900px) scale(0.8); opacity: 0; }
}

/* Floating flowers */
.flower {
  position: fixed;
  animation: swayUp 8s ease-in-out infinite;
  opacity: 0.9;
  z-index: 4;
}

@keyframes swayUp {
  0%   { transform: translate(0px, 0px) rotate(0deg); opacity: 0; }
  20%  { opacity: 1; }
  50%  { transform: translate(-40px, -400px) rotate(-10deg); }
  100% { transform: translate(40px, -900px) rotate(10deg); opacity: 0; }
}

/* Fireworks */
.firework {
  position: fixed;
  bottom: 0;
  font-size: 30px;
  animation: explode 3.5s ease-out infinite;
  z-index: 6;
}

@keyframes explode {
  0%   { transform: translateY(0px) scale(0.2); opacity: 0; }
  20%  { opacity: 1; }
  50%  { transform: translateY(-250px) scale(1.6); opacity: 1; }
  100% { transform: translateY(-450px) scale(0.2); opacity: 0; }
}
</style>
"""

# ================== HTML GENERATORS ==================
def generate_hearts(num=25):
    hearts_html = ""
    for _ in range(num):
        x = random.randint(0, 100)   # horizontal position
        delay = random.uniform(0, 4) # seconds
        size = random.randint(24, 50)
        hearts_html += f"""
        <div class="heart" style="
            left: {x}%;
            animation-delay: {delay}s;
            font-size: {size}px;
        ">❤️</div>
        """
    return hearts_html

def generate_flowers(num=18):
    flowers_html = ""
    flower_emojis = ["🌸", "🌹", "🌷", "💐", "🌺"]
    for _ in range(num):
        x = random.randint(0, 100)
        delay = random.uniform(0, 5)
        size = random.randint(26, 46)
        emoji = random.choice(flower_emojis)
        flowers_html += f"""
        <div class="flower" style="
            left: {x}%;
            animation-delay: {delay}s;
            font-size: {size}px;
        ">{emoji}</div>
        """
    return flowers_html

def generate_fireworks(num=10):
    fw_html = ""
    emojis = ["🎆", "🎇", "✨"]
    for _ in range(num):
        x = random.randint(5, 95)
        delay = random.uniform(0, 3)
        size = random.randint(26, 40)
        emoji = random.choice(emojis)
        fw_html += f"""
        <div class="firework" style="
            left: {x}%;
            animation-delay: {delay}s;
            font-size: {size}px;
        ">{emoji}</div>
        """
    return fw_html

# ================== APP LOGIC ==================
if name.strip().lower() == "bubu":
    # Inject CSS
    st.markdown(css, unsafe_allow_html=True)

    # Main layout
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("bubu.jpg", caption="💖 Bubu, the One and Only 💖", use_column_width=True)

        st.markdown(
            """
            <h1 style='color:#ffebfb; margin-top: 10px;'>
                💖 Bubu Detected 💖
            </h1>
            <h2 style='color:#ffe6f7;'>
                Premium Romantic Mode: <i>ACTIVATED</i> 💘
            </h2>
            <p style='font-size:20px;'>
                You have unlocked:<br>
                🌹 Infinite love<br>
                🎆 Lifetime fireworks<br>
                💐 Unlimited flowers<br><br>
                Warning: screen may now contain<br>
                excessive levels of cuteness. 🥹💞
            </p>
            """,
            unsafe_allow_html=True
        )

    # Overlay animations
    st.markdown(generate_hearts(30), unsafe_allow_html=True)
    st.markdown(generate_flowers(20), unsafe_allow_html=True)
    st.markdown(generate_fireworks(12), unsafe_allow_html=True)

else:
    st.write("Write **'Bubu'** to unleash flowers, fireworks and true magic 💘")
