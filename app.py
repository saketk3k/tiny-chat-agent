import streamlit as st
import time

# Page config
st.set_page_config(page_title="Tiny Agent", page_icon="🤖")

st.title("🤖 Tiny Chat Agent")
st.caption("A simple rule-based agent demonstrating state management in Streamlit.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I am a tiny agent. Ask me about 'time', 'joke', or 'status'!"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is your command?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Agent Logic (Rule-based for POC)
    response = ""
    prompt_lower = prompt.lower()
    
    with st.spinner("Thinking..."):
        time.sleep(0.5) # Simulate latency
        
        if "time" in prompt_lower:
            from datetime import datetime
            response = f"The current system time is **{datetime.now().strftime('%H:%M:%S')}**."
        elif "joke" in prompt_lower:
            response = "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"
        elif "status" in prompt_lower:
            response = "All systems operational. CPU: 12% | RAM: 45%"
        elif "help" in prompt_lower:
            response = "I can help you with basic queries. Try asking for the **time**, a **joke**, or system **status**."
        else:
            response = "I'm a tiny agent and I didn't understand that. Try asking for 'help'."

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
