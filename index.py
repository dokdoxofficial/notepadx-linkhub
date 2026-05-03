import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="NotepadX LinkHub",
    page_icon="🔗",
)

st.title("🔗 NotepadX LinkHub")
st.info("새로운 소식 또는 정보가 이 사이트를 통해 자동으로 업데이트 될 예정입니다!")

st.subheader("바로가기")
st.link_button("📝NotepadX 메모장", "https://notepadx.netlify.app")
st.link_button("🛡️개인정보 보호약관", "https://notepadxprivacy.netlify.app")


#그래프
st.subheader("추천하는 음악")
st.info("영상을 시청하는데 어려움이 있나요?직접 유튜브를 방문하여서 시청할수도 있습니다!")
st.video("https://www.youtube.com/watch?v=9voN0gkdlS4&list=RD9voN0gkdlS4&start_radio=1")
