# import streamlit as st
# from streamlit_google_auth import Authenticate

# st.title('AI Startup mentor & Co-Founder Match')

# authenticator = Authenticate(
#     secret_credentials_path = 'google_credentials.json',
#     cookie_name='my_cookie_name',
#     cookie_key='this_is_secret',
#     redirect_uri = 'https://kyroz.org'
# )

# # Catch the login event
# authenticator.check_authentification()

# # Create the login button
# authenticator.login()

# if st.session_state['connected']:
#     st.image(st.session_state['user_info'].get('picture'))
#     st.write('Hello, '+ st.session_state['user_info'].get('name'))
#     st.write('Your email is '+ st.session_state['user_info'].get('email'))
#     if st.button('Log out'):
#         authenticator.logout()



import streamlit as st
from streamlit_google_auth import Authenticate


page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://kyroz.org/images/innovation3.jpeg");
  background-size: cover;
}
</style>
"""
st.markdown(page_element, unsafe_allow_html=True)

st.title('Leon : AI Co-founder match powered by Gemini')

if 'connected' not in st.session_state:
    authenticator = Authenticate(
        secret_credentials_path = 'google_credentials.json',
        cookie_name='my_cookie_name',
        cookie_key='this_is_secret',
        redirect_uri = 'https://google.com',
    )
    st.session_state["authenticator"] = authenticator

# Catch the login event
st.session_state["authenticator"].check_authentification()

# Create the login button
st.session_state["authenticator"].login()

if st.session_state['connected']:
    st.image(st.session_state['user_info'].get('picture'))
    st.write('Hello, '+ st.session_state['user_info'].get('name'))
    st.write('Your email is '+ st.session_state['user_info'].get('email'))
    if st.button('Log out'):
        st.session_state["authenticator"].logout()