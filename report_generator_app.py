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
MAX_VARIANTS = 3    # we have 3 variants per band

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

def generate_comment(name, att, read, write, read_t, write_t, pronouns, variant=0, attitude_target=None):
    """
    variant: 0,1,2 corresponds to Variant 1,2,3
    """
    p, p_poss = pronouns
    opening = random.choice(opening_phrases)

    # pick variant for each bank
    att_phrase = attitude_bank[att][variant % MAX_VARIANTS]
    read_phrase = reading_bank[read][variant % MAX_VARIANTS]
    write_phrase = writing_bank[write][variant % MAX_VARIANTS]
    read_target_phrase = reading_target_bank[read_t][variant % MAX_VARIANTS]
    write_target_phrase = writing_target_bank[write_t][variant % MAX_VARIANTS]

    attitude_sentence = f"{opening} {name} {att_phrase}."
    reading_sentence = f"In reading, {p} {read_phrase}."
    writing_sentence = f"In writing, {p} {write_phrase}."
    reading_target_sentence = f"For the next term, {p} should {lowercase_first(read_target_phrase)}."
    writing_target_sentence = f"In addition, {p} should {lowercase_first(write_target_phrase)}."

    # optional attitude target
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
    "Fill in the student details and click **Generate Comment**. You can cycle through 3 variants using **Vary Comment**."
)

# Initialize session state
if 'all_comments' not in st.session_state:
    st.session_state['all_comments'] = []

if 'variant_index' not in st.session_state:
    st.session_state['variant_index'] = 0

if 'current_pronouns' not in st.session_state:
    st.session_state['current_pronouns'] = ("they", "their")

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

if submitted and name:
    st.session_state['current_pronouns'] = get_pronouns(gender)
    st.session_state['variant_index'] = 0  # Reset to Variant 1
    st.session_state['current_comment'] = generate_comment(
        name, att, read, write, read_t, write_t,
        st.session_state['current_pronouns'],
        variant=st.session_state['variant_index'],
        attitude_target=attitude_target
    )

# Display generated comment
if 'current_comment' in st.session_state and name:
    variant_num = st.session_state['variant_index'] + 1
    st.markdown(f"**Generated Comment**")
    st.write(f"{name} (Variant {variant_num}): {st.session_state['current_comment']}")
    st.write(f"Character count (including spaces): {len(st.session_state['current_comment'])} / {TARGET_CHARS}")

    if st.button("Vary Comment"):
        st.session_state['variant_index'] = (st.session_state['variant_index'] + 1) % MAX_VARIANTS
        # regenerate with new variant
        st.session_state['current_comment'] = generate_comment(
            name, att, read, write, read_t, write_t,
            st.session_state['current_pronouns'],
            variant=st.session_state['variant_index'],
            attitude_target=attitude_target
        )
        st.experimental_rerun()

    if st.button("Add to Report"):
        st.session_state['all_comments'].append(f"{name} (Variant {variant_num}): {st.session_state['current_comment']}")

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
    st.markdown("### All Generated Comments:")
    for c in st.session_state['all_comments']:
        st.write(c)
