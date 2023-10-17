import streamlit as st
import time

# Sample text for the typing test
sample_text = """
The quick brown fox jumps over the lazy dog. This is a sample sentence for the typing test. Type as fast as you can. The quick brown fox jumps over the lazy dog. This is a sample sentence for the typing test. Type as fast as you can.The quick brown fox jumps over the lazy dog. This is a sample sentence for the typing test. Type as fast as you can.
"""

def main():
    st.title("Typing Test App")
    
    st.write("Sample Text:")
    st.text_area("", sample_text, height=100, key="sample_text_area", disabled=True)
    
    st.write("Type the above text here:")
    user_input = st.text_area("", "", height=100, key="user_text_area")
    
    start_button = st.button("Start Test")
    stop_button = st.button("Stop Test")
    
    if start_button:
        st.write("Test started. You have 1 minute.")
        st.write("Timer:")
        with st.empty() as timer:
            for i in range(60, 0, -1):
                timer.write(f"{i} seconds left")
                time.sleep(1)
    
    if stop_button:
        st.write("Test stopped.")
        
        # Calculate typing speed and accuracy
        sample_words = sample_text.split()
        user_words = user_input.split()
        
        correct_count = sum(1 for a, b in zip(sample_words, user_words) if a == b)
        total_words = len(user_words)
        
        speed = total_words / 1  # Since the timer is 1 minute
        accuracy = (correct_count / len(sample_words)) * 100
        
        st.write(f"Typing Speed: {speed} WPM")
        st.write(f"Accuracy: {accuracy}%")

if __name__ == "__main__":
    main()
