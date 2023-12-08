import streamlit as st

st.set_page_config(page_title="Jervymy Bernardo website",page_icon=":tada:", layout="wide")

with st.container():
    st.subheader("Programming Logic and Design  Project")
    st.title("Welcome to Jervymy website")
    st.write("Hi, I am Jervymy B. Bernardo. 19 years a 1st computer Engineering students at Surigao Del Norte State University")

with st.container():
    st.write("---")
    left_column, rigth_column = st.columns(2)
    with left_column:
        st.subheader("More information about Me:")
        st.write("##")
        st.write(
            """
            - live at  Barangay Poblacion Tubod Surigao Del Norte
            - Birth Date: September 15, 2004  
            - Fathers Name: Gerardo Bernardo 
            - Mothers Name: Myren Bernardo
            - 5 siblings namely; Jeremy, Jersymy, Jerlymy, Jerpymy, and Jertymy Bernardo
            
            """
        )

    st.subheader("Hobbies:")
    st.write("##")
    st.write(
        """
        - love watching Anime
        - Drawing
        - Photography
        - Reading Wattpad
        """
    )

with st.container():
    st.subheader("This is my social media account if you want to know more about me:")
    st.write("##")
    st.write(
        """
        - Facebook: https://www.facebook.com/jervymy.bernardo.7
    - Instagram: https://instagram.com/jerv.bb?igshid=NzZIODBkYWE4Ng==
        """
    ) 
    
with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")

    contact_form = """
    <from action="https://formsubmit.co/jervymybernardo@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textrarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, rigth_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with rigth_column:
        st.empty()




    