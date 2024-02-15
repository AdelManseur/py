import streamlit as st
from websiteBackend import initialize_streamlit, process_query
import base64


def main():
    initialize_streamlit()

    st.title('🦜🔗 Chat With Maktaba')
    st.subheader('Ask questions and receive answers directly from Maktaba\'s chatbot.')

    url = ["https://maktaba.super.site", "https://maktaba.super.site/docs", "https://super.so/",
           "https://tailwindui.com/?ref=top", "https://getbootstrap.com/", "https://www.storj.io/"]

    favicon_path = "favicon.png"

    # Read the favicon image file and encode it in base64
    with open(favicon_path, "rb") as f:
        favicon_base64 = base64.b64encode(f.read()).decode()

    # Include the favicon in the HTML
    st.markdown(f"""
        <link rel="shortcut icon" href="data:image/png;base64,{favicon_base64}" type="image/png">
    """, unsafe_allow_html=True)

    prompt = st.text_input("Ask a question (query/prompt)")

    if st.button("Submit Query", type="primary"):
        response = process_query(url, prompt)
        st.write(response)

if __name__ == '__main__':
    main()
    