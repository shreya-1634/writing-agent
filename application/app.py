import streamlit as st
from agents.planner import generate_plan
from agents.writer import write_content
from agents.editor import refine_content

st.set_page_config(page_title="Writing Agent", page_icon="✍️")

st.title("✍️ Multi-Agent Writing System")

topic = st.text_input("Enter topic:")

if st.button("Generate Article"):
    if topic:
        with st.spinner("Planning..."):
            plan = generate_plan(topic)
        st.subheader("📌 Plan")
        st.write(plan)

        with st.spinner("Writing..."):
            draft = write_content(plan)
        st.subheader("✍️ Draft")
        st.write(draft)

        with st.spinner("Editing..."):
            final = refine_content(draft)
        st.subheader("✅ Final Output")
        st.write(final)
    else:
        st.warning("Please enter a topic")
