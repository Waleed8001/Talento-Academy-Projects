import streamlit as st

def homepage():
    st.set_page_config(
        page_title="Whatsapp Message Sending",
        page_icon="message_icon.ico",
        layout="wide"
    )

    st.sidebar.title("Choose Page:")
    st.sidebar.text("Home")

    st.title("✉️ Welcome to our Automatic Whatsapp Sending App")
    st.title("=================================")

    st.markdown("""
In this App, We can send message to whatsapp to any recipient by entering his Phone Number along with country code.
\nIt will take 15 to 20 seconds to send message to each Person. For sending message to new person, new tab wil open every time. Similarly when sending a file, the file will send separately then message.
\n**The module use in this project:**

1. Streamlit
2. Pywhatkit
3. Time
4. Pyautogui
5. Pyinstaller
""")

if __name__== "__main__":
    homepage()


