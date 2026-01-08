# =========================================
# ENGLISH REPORT COMMENT GENERATOR - Streamlit Version
# =========================================

import random
import streamlit as st
from docx import Document
import io

from statements import (
    opening_phrases,
    attitude_bank,
    reading_bank,
    writing_bank,
    reading_target_bank,
    writing_target_bank,
    closer_bank
)

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
    truncated = comment[:target].rstrip(" ,;.")
    if "." in truncated:
        truncated = truncated[:truncated.rfind(".")+1]
    return truncated

# ---------- STATE ----------
if 'all_comments' not in st.session_state:
    st.session_state['all_comments'] = []

if 'variant_counter' not in st.session_state:
    st.session_state['variant_counter'] = 0

# ---------- COMMENT GENERATOR ----------
def generate_comment(name, att, read, write, read_t, write_t, pronouns, attitude_target=None):
    p, p_poss = pronouns
    variant = st.session_state['variant_counter'] % 3  # cycle 0,1,2

    opening = opening_phrases[variant % len(opening_phrases)]

    # Pick variant phrase
    att_phrase = attitude_bank[att][variant] if isinstance(attitude_bank[att], list) else attitude_bank[att]
    read_phrase = reading_bank[read][variant] if isinstance(reading_bank[read], list) else reading_bank[read]
    write_phrase = writing_bank[write][variant] if isinstance(writing_bank[write], list) else writing_bank[write]
    read_target_phrase = reading_target_bank[read_t][variant] if isinstance(reading_target_bank[read_t], list) else reading_target_bank[read_t]
    write_target_phrase = writing_target_bank[write_t][variant] if isinstance(writing_target_bank[write_t], list) else writing_target_bank[write_t]

    attitude_sentence = f"{opening} {name} {att_phrase}."
    reading_sentence = f"In reading, {p} {read_phrase}."
    writing_sentence = f"In writing, {p} {write_phrase}."
    reading_target_sentence = f"For the next term, {p} should {lowercase_first(read_target_phrase)}."
    writing_target_sentence = f"In addition, {p} should {lowercase_first(write_target_phrase)}."

    attitude_target_sentence = f" {lowercase_first(attitude_target)}" if attitude_target else ""
    closer_sentence = closer_bank[variant % len(closer_bank)]

    comment_parts = [
        f"{name} (Variant {variant+1}): " + attitude_sentence + attitude_target_sentence,
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
    "Fill in the student details and click **Generate Comment**. Use **Vary** to cycle through variant statements."
)

# Form for student details
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

# ---------- HANDLE COMMENT GENERATION ----------
if submitted and name:
    pronouns = get_pronouns(gender)
    st.session_state['current_comment'] = generate_comment(
        name, att, read, write, read_t, write_t, pronouns, attitude_target
    )

# Display current comment (read-only)
if 'current_comment' in st.session_state:
    st.markdown("### Generated Comment")
    st.write(st.session_state['current_comment'])

# ---------- VARY BUTTON ----------
if st.button("Vary"):
    st.session_state['variant_counter'] += 1
    if 'current_comment' in st.session_state:
        st.session_state['current_comment'] = generate_comment(
            name, att, read, write, read_t, write_t, pronouns, attitude_target
        )

# ---------- ADD ANOTHER COMMENT BUTTON ----------
if st.button("Add Another Comment"):
    if 'current_comment' in st.session_state:
        st.session_state['all_comments'].append(st.session_state['current_comment'])
    st.session_state['variant_counter'] = 0
    if 'current_comment' in st.session_state:
        del st.session_state['current_comment']

# ---------- DOWNLOAD FULL REPORT ----------
if st.session_state['all_comments']:
    if st.button("Download Full Report (Word)"):
        doc = Document()
        for c in st.session_state['all_comments']:
            doc.add_paragraph(c)

        file_stream = io.BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)

        st.download_button(
            label="Download Word File",
            data=file_stream,
            file_name="English_Report_Comments.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

# ---------- SHOW ALL COMMENTS SO FAR ----------
if st.session_state['all_comments']:
    st.markdown("### All Saved Comments:")
    for c in st.session_state['all_comments']:
        st.write(c)
