try:
    import os
    from tempfile import NamedTemporaryFile
    import pyautogui
    import time
    import pywhatkit as kit
    import keyboard
    import streamlit as st

    def text_image():
        st.set_page_config(
            page_title="Whatsapp Message Sending",
            page_icon="message_icon.ico",
            layout="wide"
        )
        
        
        st.sidebar.title("Choose Page:")
        st.sidebar.text("Text and Images")
        
        st.title("💬 Here You can Send Message and Image 📂")
        st.title("================================")
        
        file = st.file_uploader("Enter File", type=["jpg", "jpeg", "PNG"])
        
        
        if file:
            st.image(file)
            
        st.write("Write Your Caption Below")
        st.text("For bold anything write between ** without spacing for example (*WOW*)")
        st.text("For italic anything write between __ without spacing for example (_WOW_)")
        st.text("For line strike anything write between ~~ without spacing for example (~WOW~)")
        st.text("For dotted bullets use - then space for example (- WOW)")
        st.text("For number bullets use 1. then space for example (1. WOW)")
        
        
        my_caption = st.text_area("Enter Caption", height=100)
        
        
        if my_caption:
            # whatsapp_text = convert_html_to_whatsapp(contents)
            st.write("WhatsApp Message:")
            st.write(my_caption)
            
            
        if "list_of_num_for_text_images" not in st.session_state:
            st.session_state.list_of_num_for_text_images = []
            
            
        if "counter" not in st.session_state:
            st.session_state.counter = 0
            
            
        st.write("")
        st.info("Press Enter after add Number of each Member.")
        st.warning("""Warning! The Number should start with country code otherwise it will give an error (+92).""")
        st.write("Write Number of Members:")
        col1, col2, col3 = st.columns(3)
        
        
        with col1:
            num = st.text_input("Enter Number")
            if keyboard.is_pressed('enter'):
                if num.startswith("+92"):
                    if num not in st.session_state.list_of_num_for_text_images:
                        st.session_state.list_of_num_for_text_images.append(num)
                    
                    else:
                        st.error("Number already exist.")
                else:
                    st.exception("The Number should start from +92.")
                    
                    
        with col2:
            st.write("")
            st.write("")
            if st.button("Delete last Number", use_container_width=True):
                if st.session_state.list_of_num_for_text_images:
                    st.session_state.list_of_num_for_text_images.pop()
                    
                    
        with col3:
            st.write("")
            st.write("")
            if st.button("Delete all Numbers", use_container_width=True):
                st.session_state.list_of_num_for_text_images = []
                
                
        if "list_of_num_for_text_images" in st.session_state:
            for i in st.session_state.list_of_num_for_text_images:
                st.write(i)
                
                
        st.info("Make Sure Your Whatsapp is already LoggedIn in other tab.")
        st.warning("You should not Switch to Other Tab as long as the Message Sent to all Recipients.")
        st.warning("Your Internet Connection should be Fast.")
        st.warning("If you Enter Wrong Number by Mistake then Whatsapp will Give an Error Message but You should wait until the tab will Automatically Close.")

        
        emp = st.empty()
        st.session_state.counter = 0
            
        if st.button("Send Message"):
            if file:
                # Save uploaded file to a temporary location
                file_extension = os.path.splitext(file.name)[-1]
                
                with NamedTemporaryFile(delete=False, suffix=file_extension) as tmp:
                    tmp.write(file.getvalue())
                    temp_file_path = tmp.name
                    
                    
                for i in st.session_state.list_of_num_for_text_images:
                    try:
                        # Send image
                        time.sleep(2)
                        kit.sendwhats_image(f"{i}", temp_file_path, caption=my_caption, wait_time=20)
                        
                        time.sleep(2)
                        pyautogui.hotkey("enter")
                        
                        time.sleep(5)
                        pyautogui.hotkey("ctrl", "w")
                        
                        st.session_state.counter += 1
                        emp.write(f"The message sent to Recipient: {st.session_state.counter}")
                        
                        time.sleep(1)
                        
                    except Exception as e:
                        st.error(f"Could not send message to {i}. Error: {e}")
                        
                if len(st.session_state.list_of_num_for_text_images) == st.session_state.counter:
                    st.success("Congratulations! Your message has been sent to all Members.")
                
            else:
                st.error("Text or File is Missing.")

except Exception as e:
    st.write(e)
    
if __name__ == "__main__":
    text_image()
    


    
