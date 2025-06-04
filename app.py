import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🎬 TikTok Script Generator Bot")

topic = st.text_input("Enter a TikTok topic or niche:")

if st.button("Generate Script"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating..."):
            prompt = f"""
Create a viral TikTok video script for the topic: "{topic}".

Include:
1. A short, attention-grabbing hook (max 12 words)
2. A simple 3-5 line script, engaging and casual
3. End with a strong CTA (call to action)

Output format:
Hook:
Script:
CTA:
"""
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.8,
                    max_tokens=300
                )
                st.subheader("Your TikTok Script:")
                st.text(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
