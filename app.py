import streamlit as st       

st.title('Streamlit layers and containers')

tab1,tab2,tab3,tab4=st.tabs(["Cat","Dog","Owl","Lion"])

with tab1:
    st.header("This is Cat tab")     


with tab2:
    st.header("This is Dog tab")     
    

with tab3:
    st.header("This is Owl tab")     


with tab4:
    st.header("This is Lion tab")   
    
    
col1,col2=st.columns(2)
with col1:
    b1=st.button("submit") 

b2=st.sidebar.button("login")

b3=st.sidebar.button("logout")

with st.expander("Open me"):
    st.image(r"E:\PROJECT\PYTHON\ML\Streamlit\nit.jpg") 
