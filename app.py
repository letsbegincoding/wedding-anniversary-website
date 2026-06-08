import streamlit as st
from PIL import Image
from datetime import date
import time
import streamlit.components.v1 as components

# Page Config
st.set_page_config(
    page_title="Forever Together ❤️",
    page_icon="❤️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background-color: transparent;
}

.title{
    text-align:center;
    font-size:72px;
    font-weight:bold;
    color:#d4af37;
    animation: glow 2s infinite alternate;
}

.subtitle{
    text-align:center;
    font-size:32px;
    color:#262730;
    font-weight:600;
}

.quote{
    text-align:center;
    font-size:22px;
    color:#31333F;
    font-style:italic;
}

.fade-in{
    animation: fadeIn 2s ease-in;
}

@keyframes glow{
    from{
        text-shadow:
        0 0 10px #ffd700,
        0 0 20px #ffd700;
    }

    to{
        text-shadow:
        0 0 20px #ffd700,
        0 0 40px #ffd700;
    }
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(30px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}

.anniversary-message{
    text-align:center;
    font-size:26px;
    color:#8b6914;
    font-weight:bold;
    margin-top:20px;
    margin-bottom:20px;
}
            
.counter-card{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,215,0,0.3);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(255,215,0,0.15);
}

.counter-number{
    font-size: 42px;
    font-weight: bold;
    color: #FFD700;
}

.counter-label{
    font-size: 18px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# Cover Image
cover = Image.open("images/cover.jpeg")
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    st.image(
        cover,
        width=1000
    )

# Main Heading
st.markdown("""
<div class="fade-in">
<p style="
text-align:center;
font-size:50px;
font-weight:bold;
color:#FFD700;
text-shadow:0 0 20px rgba(255,215,0,0.9);
">
Forever Together ❤️
</p>
</div>
""", unsafe_allow_html=True)

# Subtitle
st.markdown("""
<p style="
text-align:center;
font-size:28px;
font-weight:600;
color:white;
">
Happy Wedding Anniversary Mum & Pappa 💍❤️
</p>
""", unsafe_allow_html=True)

# Quote
st.markdown("""
<p style="
text-align:center;
font-size:18px;
font-style:italic;
color:#C0C0C0;
">
"A beautiful journey of love, trust, sacrifice and countless memories."
</p>
""", unsafe_allow_html=True)

# Anniversary Message
st.markdown("""
<div class="fade-in">

<h3 style='
text-align:center;
color:#FFD700;
font-size:24px;
font-weight:bold;
text-shadow:0 0 20px rgba(255,215,0,0.9);
line-height:2;
'>

💍 Two Hearts<br>

👫 One Journey<br>

❤️ Endless Love

</h3>

</div>
""", unsafe_allow_html=True)

# Golden Divider
st.markdown(
    "<hr style='border:2px solid gold;'>",
    unsafe_allow_html=True
)


st.markdown("""
<h1 style='text-align:center;color:#FFD700;'>
🎵 Song for You 
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;font-size:20px;'>
A melody that makes this celebration even more special ❤️
</p>
""", unsafe_allow_html=True)

audio_file = open(
    "music/Inkem Inkem Inkem Kaavaale.mp3",
    "rb"
)

audio_bytes = audio_file.read()

st.audio(
    audio_bytes,
    format="audio/mp3"
)


# Golden Divider
st.markdown(
    "<hr style='border:2px solid gold;'>",
    unsafe_allow_html=True
)


# Welcome Section
st.markdown("""
<div style="
max-width:800px;
margin:auto;
background:rgba(255,215,0,0.05);
border:2px solid rgba(255,215,0,0.3);
border-radius:25px;
padding:35px;
box-shadow:0 0 25px rgba(255,215,0,0.15);
">

<h1 style="
text-align:center;
color:#FFD700;
margin-bottom:25px;
font-size:32px;
">
❤️ Welcome ❤️
</h1>

<p style="
font-size:15px;
line-height:1.8;
text-align:center;
">
Today we celebrate a beautiful journey built on love, trust,
patience, sacrifice, and togetherness.
</p>

<p style="
font-size:15px;
line-height:1.8;
text-align:center;
">
This website is a small gift dedicated to the two people
who taught us the meaning of family.
</p>

<hr style="border:1px solid rgba(255,215,0,0.3);">

<p style="font-size:15px;">
💖 Thank you for building a home filled with love.
</p>

<p style="font-size:15px;">
💖 Thank you for supporting each other through every challenge.
</p>

<p style="font-size:15px;">
💖 Thank you for being our inspiration every day.
</p>

<p style="font-size:15px;">
💖 Thank you for giving us countless memories to cherish forever.
</p>

</div>
""", unsafe_allow_html=True)

# Golden Divider
st.markdown(
    "<hr style='border:2px solid gold;'>",
    unsafe_allow_html=True
)


st.markdown("## ⏳ Your Journey in Real Time ❤️")

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>

.timer-container{
    text-align:center;
    padding:20px;
}

.timer-title{
    font-size:32px;
    font-weight:bold;
    color:#FFD700;
    margin-bottom:20px;
}

.timer{
    display:flex;
    justify-content:center;
    flex-wrap:wrap;
    gap:15px;
}

.box{
    background:rgba(255,215,0,0.08);
    border:1px solid rgba(255,215,0,0.4);
    border-radius:15px;
    padding:15px;
    min-width:120px;
    box-shadow:0 0 10px rgba(255,215,0,0.2);
}

.number{
    font-size:32px;
    font-weight:bold;
    color:#FFD700;
}

.label{
    font-size:16px;
    color:white;
}

</style>
</head>

<body>

<div class="timer-container">

<div class="timer-title">
💍 Together Since 08 June 2003
</div>

<div class="timer">

<div class="box">
<div id="years" class="number">0</div>
<div class="label">Years</div>
</div>

<div class="box">
<div id="months" class="number">0</div>
<div class="label">Months</div>
</div>

<div class="box">
<div id="days" class="number">0</div>
<div class="label">Days</div>
</div>

<div class="box">
<div id="hours" class="number">0</div>
<div class="label">Hours</div>
</div>

<div class="box">
<div id="minutes" class="number">0</div>
<div class="label">Minutes</div>
</div>

<div class="box">
<div id="seconds" class="number">0</div>
<div class="label">Seconds</div>
</div>

</div>
</div>

<script>

const weddingDate = new Date("2003-06-08T00:00:00");

function updateTimer() {

    const now = new Date();

    let years = now.getFullYear() - weddingDate.getFullYear();
    let months = now.getMonth() - weddingDate.getMonth();
    let days = now.getDate() - weddingDate.getDate();

    if (days < 0) {
        months--;

        const lastMonth = new Date(
            now.getFullYear(),
            now.getMonth(),
            0
        );

        days += lastMonth.getDate();
    }

    if (months < 0) {
        years--;
        months += 12;
    }

    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();

    document.getElementById("years").innerHTML = years;
    document.getElementById("months").innerHTML = months;
    document.getElementById("days").innerHTML = days;
    document.getElementById("hours").innerHTML = hours;
    document.getElementById("minutes").innerHTML = minutes;
    document.getElementById("seconds").innerHTML = seconds;
}

updateTimer();
setInterval(updateTimer, 1000);

</script>

</body>
</html>
""", height=320)


st.markdown("""
<h1 style='text-align:center;color:#FFD700;'>
💍 Your Journey Through The Years
</h1>
""", unsafe_allow_html=True)


# Golden Divider
st.markdown(
    "<hr style='border:2px solid gold;'>",
    unsafe_allow_html=True
)

st.markdown("""
<h1 style='text-align:center;
color:#FFD700;
font-size:50px;'>
📸 Your Beautiful Memories ❤️
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;
font-size:22px;'>
Every picture tells a story, every memory holds a piece of our hearts.
</p>
""", unsafe_allow_html=True)

image_files = [
    "photo1.jpeg",
    "photo2.jpeg",
    "photo3.jpeg",
    "photo4.jpeg",
    "photo5.jpeg",
    "photo6.jpeg",
    "photo7.jpeg",
    "photo8.jpeg",
    "photo9.jpeg",
    "photo10.jpeg",
    "photo11.jpeg",
    "photo12.jpeg",
    "photo13.jpeg",
    "photo14.jpeg",
    "photo15.jpeg",
    "photo16.jpeg",
    "photo17.jpeg",
    "photo18.jpeg",
    "photo19.jpeg",
    "photo20.jpeg",
    "photo21.jpeg",
    "photo22.jpeg",
    "photo23.jpeg",
    "photo24.jpeg"
]

cols = st.columns(4)

for index, image_name in enumerate(image_files):

    image = Image.open(f"images/{image_name}")

    with cols[index % 4]:
        st.image(
            image,
            width=300
        )


# Golden Divider
st.markdown(
    "<hr style='border:2px solid gold;'>",
    unsafe_allow_html=True
)

st.markdown("""
<h1 style='text-align:center;
color:#FFD700;
font-size:50px;'>
💌 A Letter From our Heart 
</h1>
""", unsafe_allow_html=True)


try:
    with open("message.txt", "r", encoding="utf-8") as file:
        letter = file.read()

    st.markdown(f"""
    <div style="
        background:rgba(255,215,0,0.08);
        border:1px solid rgba(255,215,0,0.4);
        border-radius:20px;
        padding:30px;
        margin:20px auto;
        max-width:800px;
        font-size:18px;
        line-height:2;
        box-shadow:0 0 20px rgba(255,215,0,0.15);
    ">
        {letter}
    </div>
    """, unsafe_allow_html=True)

except:
    st.warning("Please add your message inside message.txt")


# Golden Divider
st.markdown(
    "<hr style='border:2px solid gold;'>",
    unsafe_allow_html=True
)



st.markdown("""
<div style="
max-width:900px;
margin:auto;
padding:20px;
">

<div style="
border-left:4px solid #FFD700;
padding-left:25px;
margin-bottom:25px;
">
<h3 style="color:#FFD700;">💍 08 June 2003</h3>
<p>Wedding Day ❤️</p>
</div>

<div style="
border-left:4px solid #FFD700;
padding-left:25px;
margin-bottom:25px;
">
<h3 style="color:#FFD700;">🏡 Family Journey</h3>
<p>Started building a beautiful life together.</p>
</div>

<div style="
border-left:4px solid #FFD700;
padding-left:25px;
margin-bottom:25px;
">
<h3 style="color:#FFD700;">📸 Countless Memories</h3>
<p>Years filled with happiness, love and unforgettable moments.</p>
</div>

<div style="
border-left:4px solid #FFD700;
padding-left:25px;
">
<h3 style="color:#FFD700;">🎉 08 June 2026</h3>
<p>Celebrating 23 Years Together ❤️</p>
</div>

</div>
""", unsafe_allow_html=True)




# Golden Divider
st.markdown(
    "<hr style='border:2px solid gold;'>",
    unsafe_allow_html=True
)

st.markdown("""
<h1 style='text-align:center;color:#FFD700;'>
❤️ Forever Together ❤️
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;font-size:22px;'>
The most beautiful love story I have ever witnessed is yours.
</h3>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;font-size:24px;'>
💍 Happy 23rd Wedding Anniversary 💍
</p>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;font-size:22px;'>
With Love,<br>
Snoova, Bittu, Tanu ❤️
</p>
""", unsafe_allow_html=True)


st.markdown("""
<h2 style='text-align:center;color:#FFD700;'>
🌹 08 June 2003 → 08 June 2026 🌹
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;font-size:22px;'>
23 Years of Love, Trust, Sacrifice and Togetherness ❤️
</h3>
""", unsafe_allow_html=True)


