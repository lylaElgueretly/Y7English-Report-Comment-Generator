# =========================================
# ENGLISH REPORT COMMENT GENERATOR - Streamlit Version
# =========================================

import random
import streamlit as st
from docx import Document
import io
from statements import *  # <-- import your text banks

TARGET_CHARS = 499  # target character count including spaces

# ---------- HELPERS ----------
def get_pronouns(gender):
    gender = gender.lower()
    if gender == "male":
        return "he", "his"
    elif gender == "female":
        return "she", "her"
    return "they", "their"

def lowercase_first(text):
    return text[0].lower() + text[1:] if text else ""

def truncate_comment(comment, target=TARGET_CHARS):
    if len(comment) <= target:
        return comment
    truncated = comment[:target].rstrip(" ,;.")  # remove dangling punctuation
    if "." in truncated:
        truncated = truncated[:truncated.rfind(".")+1]  # truncate at last full stop
    return truncated

def generate_comment(name, att, read, write, read_t, write_t, pronouns, attitude_target=None):
    p, p_poss = pronouns
    opening = random.choice(opening_phrases)

    attitude_sentence = f"{opening} {name} {attitude_bank[att]}."
    reading_sentence = f"In reading, {p} {reading_bank[read]}."
    writing_sentence = f"In writing, {p} {writing_bank[write]}."
    reading_target_sentence = f"For the next term, {p} should {lowercase_first(reading_target_bank[read_t])}."
    writing_target_sentence = f"In addition, {p} should {lowercase_first(writing_target_bank[write_t])}."
    
    attitude_target_sentence = f" {lowercase_first(attitude_target)}" if attitude_target else ""
    closer_sentence = random.choice(closer_bank)

    comment_parts = [
        attitude_sentence + attitude_target_sentence,
        reading_sentence,
        writing_sentence,
        reading_target_sentence,
        writing_target_sentence,
        closer_sentence
    ]

    comment = " ".join(comment_parts)
    comment = truncate_comment(comment, TARGET_CHARS)
    return comment

# ---------- STREAMLIT APP ----------
st.title("English Report Comment Generator (~499 chars)")
st.markdown(
    "Fill in the student details and click **Generate Comment**. You can add multiple students before downloading the full report."
)

# Initialize session state
if 'all_comments' not in st.session_state:
    st.session_state['all_comments'] = []

# ---------- STUDENT FORM ----------
with st.form("report_form"):
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    att = st.selectbox("Attitude band", [90,85,80,75,70,65,60,55,40])
    read = st.selectbox("Reading achievement band", [90,85,80,75,70,65,60,55,40])
    write = st.selectbox("Writing achievement band", [90,85,80,75,70,65,60,55,40])
    read_t = st.selectbox("Reading target band", [90,85,80,75,70,65,60,55,40])
    write_t = st.selectbox("Writing target band", [90,85,80,75,70,65,60,55,40])
    
    attitude_target = st.text_input("Optional Attitude Next Steps")
    submitted = st.form_submit_button("Generate Comment")

if submitted and name:
    pronouns = get_pronouns(gender)
    comment = generate_comment(name, att, read, write, read_t, write_t, pronouns, attitude_target)
    edited_comment = st.text_area("Generated Comment (editable)", value=comment, height=200)
    st.write(f"Character count (including spaces): {len(edited_comment)} / {TARGET_CHARS}")

    if st.button("Add Comment to Report"):
        st.session_state['all_comments'].append(f"{name}: {edited_comment}")
        st.success(f"Comment for {name} added.")
        st.experimental_rerun()  # restart form to add next student

# ---------- DOWNLOAD FULL REPORT ----------
if st.session_state['all_comments']:
    st.markdown("### All Generated Comments:")
    for c in st.session_state['all_comments']:
        st.write(c)

    file_stream = io.BytesIO()
    doc = Document()
    for c in st.session_state['all_comments']:
        doc.add_paragraph(c)
    doc.save(file_stream)
    file_stream.seek(0)

    st.download_button(
        label="Download Full Report (Word)",
        data=file_stream,
        file_name="English_Report_Comments.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
