import streamlit as st
paginas = [
st.Page("src/atv1.py", title="Atv 1"),
st.Page("src/atv2.py", title="Atv 2"),
st.Page("src/atv3.py", title="Atv 3"),
st.Page("src/atv4.py", title="Atv 4"),

]
st.navigation(paginas).run()