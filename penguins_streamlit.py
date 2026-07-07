import streamlit as st

st.title("Deployment Test")

try:
    import seaborn
    st.success(f"Seaborn OK {seaborn.__version__}")
except Exception as e:
    st.error(e)

try:
    import matplotlib
    st.success(f"Matplotlib OK {matplotlib.__version__}")
except Exception as e:
    st.error(e)

try:
    import pandas
    st.success(f"Pandas OK {pandas.__version__}")
except Exception as e:
    st.error(e)

try:
    import sklearn
    st.success(f"Scikit-Learn OK {sklearn.__version__}")
except Exception as e:
    st.error(e)