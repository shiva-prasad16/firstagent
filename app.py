import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

# Load API Key
load_dotenv()

from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Streamlit Page
st.set_page_config(
    page_title="AI Text Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Text Generation")

st.markdown("---")

# Sidebar
st.sidebar.header("Generation Settings")

temperature = st.sidebar.slider(
    "Temperature",
    0.0,
    2.0,
    1.0,
    0.1
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
    100,
    4096,
    1024,
    100
)

top_p = st.sidebar.slider(
    "Top P",
    0.1,
    1.0,
    1.0,
    0.1
)

# Prompt
prompt = st.text_area(
    "Enter your Prompt",
    height=220,
    placeholder="Example: Explain Retrieval Augmented Generation..."
)

if st.button("🚀 Generate Text", use_container_width=True):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:

        with st.spinner("Generating..."):

            try:

                completion = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=temperature,
                    top_p=top_p,
                    max_tokens=max_tokens,
                    stream=False
                )

                response = completion.choices[0].message.content

                st.success("Generation Completed!")

                st.subheader("Generated Text")

                st.write(response)

            except Exception as e:
                st.error(f"Error: {e}")
