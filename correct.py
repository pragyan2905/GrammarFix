import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")


model = load_model()

st.title("📝 AI Grammar Corrector")
st.write("Enter a sentence below and get the grammar-corrected version.")

user_input = st.text_area("Type your sentence here:", height=150)

if st.button("Correct Grammar"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        with st.spinner("Correcting..."):
            output = model(user_input, max_length=100)
            corrected = output[0]['generated_text']
            st.success("✅ :")
            st.write(corrected)




