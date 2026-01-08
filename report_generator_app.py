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
MAX_VARIANTS = 3    # Number of statement variants per bank

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

def pick_phrase(bank, key, variant):
    """Pick the correct variant from bank"""
    if key not in bank:
        return "No statement available"
    variant_index = variant % MAX_VARIANTS
    return bank[key][variant_index]

def generate_comment(name, att, read, write, read_t, write_t, pronouns, variant=0, attitude_target=None):
    p, p_poss = pronouns
    opening = random.choice(opening_phrases)

    # Pick phrases based on variant
    att_phrase = pick_phrase(attitude_bank, att, variant)
    read_phrase = pick_phrase(reading_bank, read, variant)
    write_phrase = pick_phrase(writing_bank, write, variant)
    read_target_phrase = pick_phrase(reading_target_bank, read_t, variant)
    write_target_phrase = pick_phrase(writing_target_bank, write_t, variant)

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
    comment = truncate_comment(comment, TARGET_CHARS)
    return f"{name} (Variant {variant + 1}): {comment}"

# ---------- STREAMLIT APP ----------
st.title("English Report Comment Generator (~499 chars)")
st.markdown(
    "Fill in the student details and click **Generate Comment**. You can vary the comment, add multiple students, and download the full report."
)

# Initialize session state safely
st.session_state.setdefault('all_comments', [])
st.session_state.setdefault('current_variant', 0)
st.session_state.setdefault('current_pronouns', ("they", "their"))
st.session_state.setdefault('current_comment', "")

# ---------- FORM ----------
with st.form("report_form"):
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    att = st.selectbox("Attitude band", [90,85,80,75,70,65,60,55,40,35])
    read = st.selectbox("Reading achievement band", [90,85,80,75,70,65,60,55,40,35])
    write = st.selectbox("Writing achievement band", [90,85,80,75,70,65,60,55,40,35])
    read_t = st.selectbox("Reading target band", [90,85,80,75,70,65,60,55,40,35])
    write_t = st.selectbox("Writing target band", [90,85,80,75,70,65,60,55,40,35])
    attitude_target = st.text_input("Optional Attitude Next Steps")

    submitted = st.form_submit_button("Generate Comment")

# ---------- GENERATE COMMENT ----------
if submitted and name:
    st.session_state['current_pronouns'] = get_pronouns(gender)
    st.session_state['current_comment'] = generate_comment(
        name, att, read, write, read_t, write_t,
        st.session_state['current_pronouns'],
        variant=st.session_state['current_variant'],
        attitude_target=attitude_target
    )

# ---------- SHOW GENERATED COMMENT ----------
if st.session_state['current_comment']:
    st.text_area("Generated Comment", value=st.session_state['current_comment'], height=200)
    st.write(f"Character count (including spaces): {len(st.session_state['current_comment'])} / {TARGET_CHARS}")

# ---------- BUTTONS ----------
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Vary Comment", key="vary_btn"):
        st.session_state['current_variant'] = (st.session_state['current_variant'] + 1) % MAX_VARIANTS
        st.session_state['current_comment'] = generate_comment(
            name, att, read, write, read_t, write_t,
            st.session_state['current_pronouns'],
            variant=st.session_state['current_variant'],
            attitude_target=attitude_target
        )
        st.experimental_rerun()

with col2:
    if st.button("Add Comment", key="add_btn"):
        st.session_state['all_comments'].append(st.session_state['current_comment'])
        st.session_state['current_comment'] = ""
        st.session_state['current_variant'] = 0
        st.experimental_rerun()

with col3:
    if st.button("Clear All", key="clear_btn"):
        st.session_state['all_comments'] = []
        st.session_state['current_comment'] = ""
        st.session_state['current_variant'] = 0
        st.experimental_rerun()

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

# ---------- SHOW ALL COMMENTS ----------
if st.session_state['all_comments']:
    st.markdown("### All Added Comments:")
    for c in st.session_state['all_comments']:
        st.write(c)
