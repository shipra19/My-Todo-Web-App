import streamlit as st
from PIL import Image

with st.expander("You want to start camera?"):
    pic = st.camera_input("Camera")

if pic:
    img=Image.open(pic)
    grey_img = img.convert("1")
    st.image(grey_img)