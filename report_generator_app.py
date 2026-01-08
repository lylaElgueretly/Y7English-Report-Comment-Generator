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
MAX_VARIANTS = 3  # maximum number of variants per band

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
    options = bank.get(key, [""])
    return options[variant % len(options)]

def generate_comment(name, att, read, write, read_t, write_t, pronouns, attitude_target=None, variant=0):
    p, p_poss = pronouns
    opening = random.choice(opening_phrases)

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
    return f"{name} (Variant {variant+1}): {comment}"

# ---------- STREAMLIT APP ----------
st.title("English Report Comment Generator (~499 chars)")
st.markdown(
    "Fill in the student details and click **Generate Comment**. Use **Vary Comment** to cycle through variants."
)

# Initialize session state
if 'all_comments' not in st.session_state:
    st.session_state['all_comments'] = []
if 'current_comment' not in st.session_state:
    st.session_state['current_comment'] = ""
if 'current_variant' not in st.session_state:
    st.session_state['current_variant'] = 0
if 'current_pronouns' not in st.session_state:
    st.session_state['current_pronouns'] = ("they", "their")
if 'current_student' not in st.session_state:
    st.session_state['current_student'] = {}

# ---------- FORM ----------
with st.form("report_form"):
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    att = st.selectbox("Attitude band", [90,85,80,75,70,65,60,55,40,0])
    read = st.selectbox("Reading achievement band", [90,85,80,75,70,65,60,55,40,0])
    write = st.selectbox("Writing achievement band", [90,85,80,75,70,65,60,55,40,0])
    read_t = st.selectbox("Reading target band", [90,85,80,75,70,65,60,55,40,0])
    write_t = st.selectbox("Writing target band", [90,85,80,75,70,65,60,55,40,0])
    
    attitude_target = st.text_input("Optional Attitude Next Steps")

    submitted = st.form_submit_button("Generate Comment")

if submitted and name:
    st.session_state['current_pronouns'] = get_pronouns(gender)
    st.session_state['current_variant'] = 0
    st.session_state['current_student'] = {
        "name": name,
        "att": att,
        "read": read,
        "write": write,
        "read_t": read_t,
        "write_t": write_t,
        "attitude_target": attitude_target
    }
    st.session_state['current_comment'] = generate_comment(
        name, att, read, write, read_t, write_t,
        st.session_state['current_pronouns'],
        attitude_target,
        variant=st.session_state['current_variant']
    )

# ---------- VARY COMMENT ----------
if st.session_state['current_student']:
    if st.button("Vary Comment"):
        st.session_state['current_variant'] += 1
        cs = st.session_state['current_student']
        st.session_state['current_comment'] = generate_comment(
            cs['name'], cs['att'], cs['read'], cs['write'],
            cs['read_t'], cs['write_t'],
            st.session_state['current_pronouns'],
            attitude_target=cs['attitude_target'],
            variant=st.session_state['current_variant']
        )

# ---------- DISPLAY CURRENT COMMENT ----------
if st.session_state['current_comment']:
    st.markdown("### Generated Comment")
    st.write(st.session_state['current_comment'])
    st.write(f"Character count (including spaces): {len(st.session_state['current_comment'])} / {TARGET_CHARS}")

    if st.button("Add Comment to Report"):
        st.session_state['all_comments'].append(st.session_state['current_comment'])
        st.session_state['current_comment'] = ""
        st.session_state['current_variant'] = 0
        st.session_state['current_student'] = {}

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
