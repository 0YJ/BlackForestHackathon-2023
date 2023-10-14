import streamlit as st

import cv2
import imagezmq

if 'image_hub' not in st.session_state:
    print('not image_hub')
    st.session_state['image_hub'] =  imagezmq.ImageHub()

def get_image():
    cam_id, frame = st.session_state.image_hub.recv_image()
    return frame

if 'camera_img' not in st.session_state:
    st.session_state['camera_img'] =  get_image()

if 'manueller_betrieb' not in st.session_state:
    st.session_state.manueller_betrieb = False

def manueller_betrieb_on_change():
    st.session_state.manueller_betrieb = not st.session_state.manueller_betrieb

st.toggle('Manueller Betrieb', value=st.session_state.manueller_betrieb, key=None, help=None, on_change=manueller_betrieb_on_change, disabled=False, label_visibility="visible")
values = st.slider('Power Fan', 0, 100, 25, disabled=not st.session_state.get("manueller_betrieb", True))

#st.session_state['camera_img'] = get_image()
#st.image(st.session_state['camera_img'], caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
FRAME_WINDOW = st.image([])

while True:
    frame = get_image()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')