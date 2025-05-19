import streamlit as st
import openai
import os
from openai import OpenAI

# Use API key from secrets or environment
api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
if not api_key:
    st.error("Missing OpenAI API key. Add it to .streamlit/secrets.toml or your environment.")
    st.stop()

# Create OpenAI client
client = OpenAI(api_key=api_key)

st.title("Joke Explainer")

user_joke = st.text_area("Enter your joke here:")

if st.button("Submit"):
    if not user_joke.strip():
        st.warning("Please enter a joke.")
    else:
        with st.spinner("Explaining your joke..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",  # or "gpt-4" if supported
                    messages=[
                        {"role": "system", "content": "You explain jokes in a simple and clear way."},
                        {"role": "user", "content": f"Explain this joke simply:\n\n{user_joke}"}
                    ],
                    temperature=0.7,
                    max_tokens=200
                )
                explanation = response.choices[0].message.content.strip()
                st.success("Here's the explanation:")
                st.write(explanation)
            except Exception as e:
                st.error(f"Error: {e}")

