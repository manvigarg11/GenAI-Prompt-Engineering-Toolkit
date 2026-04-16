# 🚀 GenAI Prompt Engineering Mini Project
# AI Assistant App using Streamlit + OpenAI API

# -----------------------------
# 📦 Installation
# -----------------------------
# pip install streamlit openai

# -----------------------------
# ▶️ Run the app
# -----------------------------
# streamlit run app.py

import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_API_KEY")

st.set_page_config(page_title="GenAI Assistant", page_icon="🤖")

# -----------------------------
# 🎯 UI Layout
# -----------------------------

st.title("🤖 GenAI Prompt Engineering Assistant")
st.markdown("Generate smart responses using structured prompts")

# Sidebar for mode selection
mode = st.sidebar.selectbox(
    "Choose Mode",
    [
        "General Chat",
        "Instagram Caption",
        "Code Generator",
        "Study Assistant",
        "Business Idea Generator"
    ]
)

user_input = st.text_area("Enter your prompt:")

# -----------------------------
# 🧠 Prompt Templates
# -----------------------------

def build_prompt(mode, user_input):
    if mode == "Instagram Caption":
        return f"""
        You are a social media expert.
        Write an engaging Instagram caption.
        Include emojis, hashtags, and a call-to-action.
        Topic: {user_input}
        """
    
    elif mode == "Code Generator":
        return f"""
        You are a senior software engineer.
        Write clean, optimized code with comments.
        Task: {user_input}
        """
    
    elif mode == "Study Assistant":
        return f"""
        You are a teacher.
        Explain the topic in simple terms with examples.
        Topic: {user_input}
        """
    
    elif mode == "Business Idea Generator":
        return f"""
        You are a startup expert.
        Generate innovative business ideas with brief explanations.
        Topic: {user_input}
        """
    
    else:
        return user_input

# -----------------------------
# ⚡ Generate Response
# -----------------------------

if st.button("Generate"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt")
    else:
        prompt = build_prompt(mode, user_input)
        
        with st.spinner("Generating response..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            output = response.choices[0].message.content
            
            st.subheader("✨ Output")
            st.write(output)

# -----------------------------
# 💡 Footer
# -----------------------------

st.markdown("---")
st.markdown("Made with ❤️ using Prompt Engineering")
