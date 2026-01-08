# =========================================
# ENGLISH REPORT COMMENT GENERATOR - Streamlit Version
# =========================================

import random
import streamlit as st
from docx import Document
import io

from statements import (
    opening_phrases,
    attitude_banks,
    reading_banks,
    writing_banks,
    reading_target_banks,
    writing_target_banks,
    closer_banks
)

TARGET_CHARS = 499
MAX_VARIANTS = 3  # number of variants per statement

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

def pick_phrase(bank, band, variant):
    """Selects the phrase for the given band and variant index"""
    phrases = bank[band]
    if isinstance(phrases, list):
        return phrases[(variant - 1) % len(phrases)]
    return phrases

def generate_comment(name, att, read, write, read_t, write_t, pronouns, attitude_target=None, variant=1):
    p, p_poss = pronouns
    opening = opening_phrases[(variant - 1) % len(opening_phrases)]

    att_phrase = pick_phrase(attitude_banks, att, variant)
    read_phrase = pick_phrase(reading_banks, read, variant)
    write_phrase = pick_phrase(writing_banks, write, variant)
    read_target_phrase = pick_phrase(reading_target_banks, read_t, variant)
    write_target_phrase = pick_phrase(writing_target_banks, write_t, variant)
    closer_phrase = closer_banks[(variant - 1) % len(closer_banks)]

    attitude_sentence = f"{opening} {name} {att_phrase}."
    reading_sentence = f"In reading, {p} {read_phrase}."
    writing_sentence = f"In writing, {p} {write_phrase}."
    reading_target_sentence = f"For the next term, {p} should {lowercase_first(read_target_phrase)}."
    writing_target_sentence = f"In addition, {p} should {lowercase_first(write_target_phrase)}."
    attitude_target_sentence = f" {lowercase_first(attitude_target)}" if attitude_target else ""

    comment_parts = [
        attitude_sentence + attitude_target_sentence,
        reading_sentence,
        writing_sentence,
        reading_target_sentence,
        writing_target_sentence,
        closer_phrase
    ]

    comment = " ".join(comment_parts)
    comment = truncate_comment(comment, TARGET_CHARS)
    return f"{name} (Variant {variant}): {comment}"

# ---------- STREAMLIT APP ----------
st.title("English Report Comment Generator (~499 chars)")
st.markdown(
    "Fill in the student details and click **Generate Comment**. You can add multiple students before downloading the full report."
)

if 'all_comments' not in st.session_state:
    st.session_state['all_comments'] = []
if 'current_variant' not in st.session_state:
    st.session_state['current_variant'] = 1

# Form for student details
with st.form("report_form"):
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    att = st.selectbox("Attitude band", list(attitude_banks.keys()))
    read = st.selectbox("Reading achievement band", list(reading_banks.keys()))
    write = st.selectbox("Writing achievement band", list(writing_banks.keys()))
    read_t = st.selectbox("Reading target band", list(reading_target_banks.keys()))
    write_t = st.selectbox("Writing target band", list(writing_target_banks.keys()))
    attitude_target = st.text_input("Optional Attitude Next Steps")

    submitted = st.form_submit_button("Generate Comment")
    vary_clicked = st.form_submit_button("Vary Comment")

# ---------- GENERATE OR VARY COMMENT ----------
if submitted and name:
    st.session_state['current_variant'] = 1
    pronouns = get_pronouns(gender)
    st.session_state['current_comment'] = generate_comment(
        name, att, read, write, read_t, write_t,
        pronouns, attitude_target, variant=st.session_state['current_variant']
    )

if vary_clicked and 'current_comment' in st.session_state:
    st.session_state['current_variant'] += 1
    if st.session_state['current_variant'] > MAX_VARIANTS:
        st.session_state['current_variant'] = 1
    pronouns = get_pronouns(gender)
    st.session_state['current_comment'] = generate_comment(
        name, att, read, write, read_t, write_t,
        pronouns, attitude_target, variant=st.session_state['current_variant']
    )

# ---------- SHOW GENERATED COMMENT ----------
if 'current_comment' in st.session_state:
    st.text_area("Generated Comment", value=st.session_state['current_comment'], height=200)
    st.write(f"Character count (including spaces): {len(st.session_state['current_comment'])} / {TARGET_CHARS}")

    if st.button("Add to All Comments"):
        st.session_state['all_comments'].append(st.session_state['current_comment'])

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
