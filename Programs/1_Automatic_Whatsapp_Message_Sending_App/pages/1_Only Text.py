try:
    import time
    import streamlit as st
    import pywhatkit as kit
    import keyboard
    import pyautogui

    def onlytext():
        st.set_page_config(
            page_title="Whatsapp Message Sending",
            page_icon="message_icon.ico",
            layout="wide"
        )

        st.sidebar.title("Choose Page:")
        st.sidebar.text("Only text")

        st.title("💬 Here You can Send Only Message")
        st.title("===============================")

        st.write("Write Your Message Below:")

        st.text("For bold anything write between ** without spacing for example (*WOW*)")
        st.text("For italic anything write between __ without spacing for example (_WOW_)")
        st.text("For line strike anything write between ~~ without spacing for example (~WOW~)")
        st.text("For dotted bullets use - then space for example (- WOW)")
        st.text("For number bullets use 1. then space for example (1. WOW)")

        text = st.text_area("Enter text", height=100)

        if text:
            # whatsapp_text = convert_html_to_whatsapp(contents)
            st.write("WhatsApp Message:")
            st.write(text)


        if "list_of_num" not in st.session_state:
            st.session_state.list_of_num = []

        if "counter" not in st.session_state:
            st.session_state.counter = 0

        st.write("")

        st.info("Press Enter after add Number of each Student.")
        st.warning("""Warning! The Number should start with country code otherwise it will give an error (+92).""")

        st.write("Write Number of Students:")

        col1, col2, col3 = st.columns(3)
        with col1:
            num = st.text_input("Enter Number")
            if keyboard.is_pressed('enter'):
                if num.startswith("+92"):
                    if num not in st.session_state.list_of_num:
                        st.session_state.list_of_num.append(num)
                
                    else:
                        st.error("Number already exist.")
                else:
                    st.exception("The Number should start from +92.")

        with col2:
            st.write("")
            st.write("")
            if st.button("Delete last Number", use_container_width=True):
                if st.session_state.list_of_num:
                    st.session_state.list_of_num.pop()

        with col3:
            st.write("")
            st.write("")
            if st.button("Delete all Numbers", use_container_width=True):
                st.session_state.list_of_num = []

        if "list_of_num" in st.session_state:
            for i in st.session_state.list_of_num:
                st.write(i)

        st.info("Make Sure Your Whatsapp is already logged in in other tab.")
        st.warning("You should not Switch to Other Tab as long as the Message Sent to all Recipients.")
        st.warning("Your Internet Connection should be Fast.")
        st.warning("If you Enter Wrong Number by Mistake then Whatsapp will Give an Error Message but You should wait until the tab will Automatically Close.")

        emp = st.empty()

        if st.button("Send Message"):
            # quoted_message = urllib.parse.quote(whatsapp_text) # Encode the formatted text here
            if text:
                for i in st.session_state.list_of_num:
                    try:
                        kit.sendwhatmsg_instantly(f"{i}", text) # Send the formatted text directly
                        time.sleep(5)
                        pyautogui.hotkey("enter")
                        
                        time.sleep(10)
                        pyautogui.hotkey("ctrl", "w")
                        
                        st.session_state.counter += 1
                        emp.write(f"The message sent to student: {st.session_state.counter}")
                        time.sleep(5)
                    except Exception as e:
                        st.error(f"Could not send message to {i}. Error: {e}")

            if len(st.session_state.list_of_num) == st.session_state.counter:
                st.success("Congratulation! Your message has been sent to all Members.")

            st.session_state.counter = 0

    if __name__ == "__main__":
        onlytext()
        
        
except Exception as e:
    st.write(e)