import streamlit as st
from datetime import date
import random

# 🎉 Page Config
st.set_page_config(page_title="Teachers' Day Surprise", page_icon="👩‍🏫", layout="centered")

# Quotes for surprise page
quotes = [
    "A teacher takes a hand, opens a mind, and touches a heart. ❤️",
    "Teachers plant seeds of knowledge that last a lifetime. 🌱",
    "Behind every successful person is a teacher who believed in them. 🌟",
    "Good teachers inspire; great teachers change lives. 🙌",
    "Teaching is the profession that creates all other professions. 🎓"
]

# Use session state to manage pages
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to go to surprise page
def go_to_surprise():
    st.session_state.page = "surprise"

# ------------------- HOME PAGE -------------------
if st.session_state.page == "home":
    st.title("🎉 Happy Teachers' Day! 🎉")
    st.subheader(f"Celebrating Teachers' Day - {date.today().strftime('%B %d, %Y')}")

    st.markdown("""
    👩‍🏫 Dear Teachers,  
    Today is all about **you** – the mentors, guides, and inspirations who make learning a beautiful journey. 🌸  
    """)
    
    st.markdown("### 👉 Click below to reveal your surprise 🎁")
    if st.button("✨ Reveal Surprise ✨"):
        go_to_surprise()

# ------------------- SURPRISE PAGE -------------------
elif st.session_state.page == "surprise":
    st.balloons()
    st.snow()

    st.title("🎉 A Big Thank You to All Teachers! 🙏❤️")
    st.subheader("You are the guiding light who shapes our future 🌟")

    st.markdown(f"""
    ### 💌 Special Message:
    Dear Teachers,  
    Thank you for your endless patience, kindness, and wisdom.  
    You inspire, guide, and empower students every single day.  
    Today, we celebrate **YOU**! 🎓🌸💖
    """)

    # Show a random inspirational quote
    st.info(random.choice(quotes))

    st.markdown("---")
    st.markdown("Made by Swalha Sakeer with ❤️")
