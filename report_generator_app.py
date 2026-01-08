# =========================================
# ENGLISH REPORT COMMENT GENERATOR - Streamlit Version
# =========================================

import random
import streamlit as st
from docx import Document
import io

TARGET_CHARS = 499  # target character count including spaces
MAX_VARIANTS = 3  # number of variants per band

# ---------- IMPORT STATEMENTS ----------
from statements import (
    opening_phrases,
    attitude_bank,
    reading_bank,
    writing_bank,
    reading_target_bank,
    writing_target_bank,
    closer_bank
)

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

# ---------- COMMENT GENERATOR ----------
def generate_comment(name, att, read, write, read_t, write_t, pronouns, variant=0, attitude_target=None):
    p, p_poss = pronouns
    opening = random.choice(opening_phrases)

    # Helper to pick variant safely
    def pick_variant(bank, key):
        val = bank[key]
        if isinstance(val, list):
            return val[variant % len(val)]
        return val

    att_phrase = pick_variant(attitude_bank, att)
    read_phrase = pick_variant(reading_bank, read)
    write_phrase = pick_variant(writing_bank, write)
    read_target_phrase = pick_variant(reading_target_bank, read_t)
    write_target_phrase = pick_variant(writing_target_bank, write_t)

    attitude_sentence = f"{opening} {name} {att_phrase}."
    reading_sentence = f"In reading, {p} {read_phrase}."
    writing_sentence = f"In writing, {p} {write_phrase}."
    reading_target_sentence = f"For the next term, {p} should {lowercase_first(read_target_phrase)}."
    writing_target_sentence = f"In addition, {p} should {lowercase_first(write_target_phrase)}."
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
    return truncate_comment(comment, TARGET_CHARS)

# ---------- STREAMLIT APP ----------
st.title("English Report Comment Generator (~499 chars)")
st.markdown(
    "Fill in the student details and click **Generate Comment**. You can add multiple students before downloading the full report."
)

if 'all_comments' not in st.session_state:
    st.session_state['all_comments'] = []
if 'variant' not in st.session_state:
    st.session_state['variant'] = 0
if 'current_pronouns' not in st.session_state:
    st.session_state['current_pronouns'] = ("they","their")

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

# Generate comment
if submitted and name:
    st.session_state['current_pronouns'] = get_pronouns(gender)
    st.session_state['current_comment'] = generate_comment(
        name, att, read, write, read_t, write_t,
        st.session_state['current_pronouns'],
        variant=st.session_state['variant'],
        attitude_target=attitude_target
    )
    st.session_state['current_name'] = name

# Show current comment
if 'current_comment' in st.session_state:
    st.markdown(f"### Generated Comment")
    st.write(f"{st.session_state['current_name']} (Variant {st.session_state['variant']+1}): {st.session_state['current_comment']}")
    st.write(f"Character count (including spaces): {len(st.session_state['current_comment'])} / {TARGET_CHARS}")

# Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Vary Comment"):
        st.session_state['variant'] += 1
        if 'current_name' in st.session_state:
            st.session_state['current_comment'] = generate_comment(
                st.session_state['current_name'],
                att, read, write, read_t, write_t,
                st.session_state['current_pronouns'],
                variant=st.session_state['variant'],
                attitude_target=attitude_target
            )
with col2:
    if st.button("Add Comment to Report"):
        st.session_state['all_comments'].append(
            f"{st.session_state['current_name']} (Variant {st.session_state['variant']+1}): {st.session_state['current_comment']}"
        )
        st.session_state['variant'] = 0  # reset for next student
with col3:
    if st.button("Clear Current Comment"):
        st.session_state['current_comment'] = ""
        st.session_state['variant'] = 0

# Download full report
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

# Show all comments
if st.session_state['all_comments']:
    st.markdown("### All Generated Comments:")
    for c in st.session_state['all_comments']:
        st.write(c)
