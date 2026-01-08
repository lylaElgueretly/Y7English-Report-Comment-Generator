# report_generator_app.py
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
MAX_VARIANTS = 3  # we have 3 variants per bank

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
    """Pick variant from bank safely"""
    variants = bank[band]
    index = (variant - 1) % len(variants)
    return variants[index]

def generate_comment(name, att, read, write, read_t, write_t, pronouns, variant=1, attitude_target=None):
    p, p_poss = pronouns
    opening = random.choice(opening_phrases)

    att_phrase = pick_phrase(attitude_bank, att, variant)
    read_phrase = pick_phrase(reading_bank, read, variant)
    write_phrase = pick_phrase(writing_bank, write, variant)
    read_target_phrase = pick_phrase(reading_target_bank, read_t, variant)
    write_target_phrase = pick_phrase(writing_target_bank, write_t, variant)

    attitude_target_sentence = f" {lowercase_first(attitude_target)}" if attitude_target else ""

    comment_parts = [
        f"{opening} {name} {att_phrase}.{attitude_target_sentence}",
        f"In reading, {p} {read_phrase}.",
        f"In writing, {p} {write_phrase}.",
        f"For the next term, {p} should {lowercase_first(read_target_phrase)}.",
        f"In addition, {p} should {lowercase_first(write_target_phrase)}.",
        random.choice(closer_bank)
    ]

    comment = " ".join(comment_parts)
    comment = truncate_comment(comment, TARGET_CHARS)
    return comment

# ---------- STREAMLIT APP ----------
st.title("English Report Comment Generator (~499 chars)")
st.markdown(
    "Fill in the student details and click **Generate Comment**. "
    "Use **Vary Comment** to cycle variants. You can add multiple students before downloading the full report."
)

# ---------- SESSION STATE ----------
if 'all_comments' not in st.session_state:
    st.session_state['all_comments'] = []

if 'current_variant' not in st.session_state:
    st.session_state['current_variant'] = 1

if 'current_pronouns' not in st.session_state:
    st.session_state['current_pronouns'] = ("they", "their")

# ---------- FORM ----------
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

# ---------- GENERATE COMMENT ----------
if submitted and name:
    st.session_state['current_pronouns'] = get_pronouns(gender)
    st.session_state['current_variant'] = 1
    comment = generate_comment(
        name, att, read, write, read_t, write_t,
        st.session_state['current_pronouns'],
        variant=st.session_state['current_variant'],
        attitude_target=attitude_target
    )
    st.session_state['current_comment'] = comment

# ---------- SHOW GENERATED COMMENT ----------
if 'current_comment' in st.session_state and st.session_state['current_comment']:
    st.markdown("### Generated Comment")
    st.write(f"{name} (Variant {st.session_state['current_variant']}): {st.session_state['current_comment']}")
    st.write(f"Character count (including spaces): {len(st.session_state['current_comment'])} / {TARGET_CHARS}")

    # ---------- VARY COMMENT ----------
    if st.button("Vary Comment"):
        st.session_state['current_variant'] += 1
        if st.session_state['current_variant'] > MAX_VARIANTS:
            st.session_state['current_variant'] = MAX_VARIANTS  # do not exceed max
        st.session_state['current_comment'] = generate_comment(
            name, att, read, write, read_t, write_t,
            st.session_state['current_pronouns'],
            variant=st.session_state['current_variant'],
            attitude_target=attitude_target
        )
        st.experimental_rerun()

    # ---------- ADD COMMENT ----------
    if st.button("Add Another Comment"):
        st.session_state['all_comments'].append(
            f"{name} (Variant {st.session_state['current_variant']}): {st.session_state['current_comment']}"
        )
        # Reset for next student
        st.session_state['current_comment'] = ""
        st.session_state['current_variant'] = 1
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

# ---------- SHOW ALL COMMENTS SO FAR ----------
if st.session_state['all_comments']:
    st.markdown("### All Added Comments:")
    for c in st.session_state['all_comments']:
        st.write(c)
