import streamlit as st
import requests

st.title("📝 Text Processing App")

text = st.text_area("Enter text to process:")

if "history" not in st.session_state:
    st.session_state.history = []

BASE_URL = "http://127.0.0.1:8000"

if st.button("🔍 Process Text"):
    if text.strip():
        response = requests.post(f"{BASE_URL}/process", json={"text": text}, cookies={"session_id": st.session_state.get("session_id", "")})
        if response.status_code == 200:
            result = response.json()
            
            # Store session ID from response cookies
            session_id = response.cookies.get("session_id")
            if session_id:
                st.session_state["session_id"] = session_id
            
            # Display results
            st.subheader("🔹 Processed Results")
            st.write(f"**Summary:** {result['summary']}")
            st.write(f"**Keywords:** {', '.join(result['keywords'])}")
            st.write(f"**Sentiment:** {result['sentiment'].capitalize()}")
        else:
            st.error("❌ Error processing text. Please try again.")
    else:
        st.warning("⚠️ Please enter some text before processing.")

if st.button("📜 Get History"):
    if "session_id" in st.session_state:
        history_response = requests.get(f"{BASE_URL}/history", cookies={"session_id": st.session_state["session_id"]})
        if history_response.status_code == 200:
            history = history_response.json()
            if history:
                st.subheader("📌 Chat History")
                for idx, entry in enumerate(history):
                    st.markdown(f"**📝 Entry {idx + 1}:**")
                    st.write(f"**Text:** {entry['text']}")
                    st.write(f"**Summary:** {entry['summary']}")
                    st.write(f"**Keywords:** {', '.join(entry['keywords'])}")
                    st.write(f"**Sentiment:** {entry['sentiment'].capitalize()}")
                    st.write("---")
            else:
                st.info("ℹ️ No history found.")
        else:
            st.error("❌ Failed to fetch history.")
    else:
        st.warning("⚠️ No session found. Process text first!")

