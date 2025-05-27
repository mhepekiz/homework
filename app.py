
import streamlit as st
import openai


api_key = st.secrets["OPENAI_API_KEY"]
client = openai.OpenAI(api_key=api_key)


# Set page layout
st.set_page_config(layout="wide")

# Get prompt from URL
query_params = st.query_params
prompt = query_params.get("prompt", "")

st.title("🎯 Growth Gurus Agentic AI Response")

if prompt:
    st.markdown(f"### Prompt: `{prompt}`")

    with st.spinner("Calling Starship. Are you there Mr.Spock..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content
            st.success("Response received!")
            st.markdown(
    f"<div style='font-size:22px; line-height:1.6; color:#efefef;'>{reply}</div>",
    unsafe_allow_html=True
)
        except Exception as e:
            st.error(f"Error: {str(e)}")
else:
    st.warning("No prompt provided. Add `?prompt=your+question` to the URL.")
