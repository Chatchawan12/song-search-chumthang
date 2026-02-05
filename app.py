import streamlit as st
import pandas as pd

# ----------------------
# Page config
# ----------------------
st.set_page_config(
    page_title="ตรวจสอบเพลงประกวด ชุมทางดาวทอง",
    page_icon="🎵",
    layout="centered"
)

# ----------------------
# Logo (ตรงกลาง)
# ----------------------
st.image("logo.png", width=220)

# ----------------------
# Title
# ----------------------
st.markdown(
    """
    <div style="
        border: 3px solid #FFD700;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 30px;
    ">
        ตรวจสอบว่าเพลงสามารถใช้ประกวดในรายการ<br>
        <span style="color:#FFD700">ชุมทางดาวทอง</span> ได้หรือไม่
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------
# Load data
# ----------------------
@st.cache_data
def load_data():
    return pd.read_csv("songs.csv")

df = load_data()

# ----------------------
# Search
# ----------------------
keyword = st.text_input("พิมพ์ชื่อเพลง หรือ ชื่อศิลปิน")

if keyword:
    result = df[
        df["เพลง"].astype(str).str.contains(keyword, case=False, na=False) |
        df["ศิลปิน"].astype(str).str.contains(keyword, case=False, na=False)
    ]

    if not result.empty:
        st.success("✅ คุณใช้เพลงนี้ประกวดได้")
        st.dataframe(result, use_container_width=True)
    else:
        st.error("❌ ขออภัยคุณไม่สามารถใช้เพลงนี้ประกวดได้ กรุณาเลือกเพลงใหม่")
else:
    st.info("กรุณาพิมพ์ชื่อเพลงหรือศิลปินเพื่อค้นหา")
