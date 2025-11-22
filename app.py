import streamlit as st
import random

st.set_page_config(page_title="Magic Love App", page_icon="❤️")

st.title("💘 Magic Love App 💘")

name = st.text_input("Enter a name:")

# CSS animation for floating hearts
css = """
<style>
.heart {
  position: fixed;
  animation: floatUp 4s linear infinite;
  font-size: 30px;
  opacity: 0.8;
}

@keyframes floatUp {
  0% { transform: translateY(0px); opacity: 1; }
  100% { transform: translateY(-800px); opacity: 0; }
}
</style>
"""

# Generate random heart positions
def generate_hearts(num=30):
    hearts_html = ""
    for _ in range(num):
        x = random.randint(0, 100)
        delay = random.uniform(0, 3)
        size = random.randint(20, 50)
        hearts_html += f"""
        <div class="heart" style="
            left: {x}%;
            animation-delay: {delay}s;
            font-size: {size}px;
        ">❤️</div>
        """
    return hearts_html


if name.strip().lower() == "bubu":
    st.markdown(css, unsafe_allow_html=True)
    st.markdown(generate_hearts(35), unsafe_allow_html=True)

    st.markdown(
        """
        <h1 style='text-align: center; color: #FF1493;'>
            💖 Bubu Detected 💖
        </h1>

        <h2 style='text-align: center; color: #ff4d6d;'>
            Congratulations! You've unlocked the *Premium Romantic Mode 💘*
        </h2>

        <p style='text-align: center; font-size: 20px;'>
            Your screen is now officially<br>
            100% <strong>cuter</strong>, <strong>funny</strong>, and <strong>more romantic</strong>.<br><br>
            Please enjoy your infinite waterfall of hearts! 💞💞💞
        </p>
        """,
        unsafe_allow_html=True
    )

else:
    st.write("Write 'Bubu' to unlock Romantic Turbo Mode 💘")
