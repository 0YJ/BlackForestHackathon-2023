import streamlit as st

st.camera_input('paltzhalter', key=None, help=None, on_change=None, disabled=False, label_visibility="visible")

if 'manueller_betrieb' not in st.session_state:
    st.session_state.manueller_betrieb = False

def manueller_betrieb_on_change():
    st.session_state.manueller_betrieb = not st.session_state.manueller_betrieb

st.toggle('Manueller Betrieb', value=st.session_state.manueller_betrieb, key=None, help=None, on_change=manueller_betrieb_on_change, disabled=False, label_visibility="visible")
values = st.slider('Power Fan', 0, 130, 25, disabled=not st.session_state.get("manueller_betrieb", True))





#def click_button():
#    st.session_state.button_manueller_betrieb = not st.session_state.button_manueller_betrieb

#st.button('Manueller Betrieb', on_click=click_button)

#if st.session_state.button_manueller_betrieb:
#    # The message and nested widget will remain on the page
#    st.write('Button is on!')
#    st.slider('Select a value')
#else:
#    st.write('Button is off!')