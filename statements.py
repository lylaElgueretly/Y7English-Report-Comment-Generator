import random
import streamlit as st
from docx import Document
import io

from statements import *

TARGET_CHARS = 499
MAX_VARIANTS = 3

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

def pick_phrase(bank_variant, band):
    return bank_variant.get(band, "")

def get_current_banks(variant):
    if variant == 1:
        return attitude_bank1, reading_bank1, writing_bank1, reading_target_bank1, writing_target_bank1
    elif variant == 2:
        return attitude_bank2, reading_bank2, writing_bank2, reading_target_bank2, writing_target_bank2
    else:
        return attitude_bank3, reading_bank3, writing_bank3, reading_target_bank3, writing_target_bank3

def generate_comment(name, att, read, write, read_t, write_t, pronouns, attitude_target=None, variant=1):
    p, p_poss = pronouns
    opening = random.choice(opening_phrases)
    
    attitude_bank, reading_bank, writing_bank, reading_target_bank, writing_target_bank = get_current_banks(variant)
    
    attitude_sentence = f"{opening} {name} {pick_phrase(attitude_bank, att)}."
    reading_sentence = f"In reading, {p} {pick_phrase(reading_bank, read)}."
    writing_sentence = f"In writing, {p} {pick_phrase(writing_bank, write)}."
    reading_target_sentence = f"For the next term, {p} should {lowercase_first(pick_phrase(reading_target_bank, read_t))}."
    writing_target_sentence = f"In addition, {p} should {lowercase_first(pick_phrase(writing_target_bank, write_t))}."
    
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
    return f"{name} (Variant {variant}): {comment}"

# ---------- SESSION STATE ----------
if 'all_comments' not in st.session_state:
    st.session_state['all_comments'] = []

if 'current_variant' not in st.session_state:
    st.session_state['current_variant'] = 1

if 'current_comment' not in st.session_state:
    st.session_state['current_comment'] = ""

if 'current_pronouns' not in st.session_state:
    st.session_state['current_pronouns'] = ("they", "their")

# ---------- STREAMLIT UI ----------
st.title("English Report Comment Generator (~499 chars)")
st.markdown("Fill in the student details and click **Generate Comment**. You can vary the comment or add multiple students before downloading the full report.")

# ---------- FORM ----------
with st.form("report_form"):
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    att = st.selectbox("Attitude band", [90,85,80])
    read = st.selectbox("Reading achievement band", [90,85,80])
    write = st.selectbox("Writing achievement band", [90,85,80])
    read_t = st.selectbox("Reading target band", [90,85,80])
    write_t = st.selectbox("Writing target band", [90,85,80])
    attitude_target = st.text_input("Optional Attitude Next Steps")
    
    submitted = st.form_submit_button("Generate Comment")

if submitted and name:
    st.session_state['current_pronouns'] = get_pronouns(gender)
    st.session_state['current_comment'] = generate_comment(
        name, att, read, write, read_t, write_t, 
        st.session_state['current_pronouns'], 
        attitude_target,
        variant=st.session_state['current_variant']
    )

# ---------- SHOW GENERATED COMMENT ----------
if st.session_state['current_comment']:
    st.text_area("Generated Comment", value=st.session_state['current_comment'], height=200)
    st.write(f"Character count (including spaces): {len(st.session_state['current_comment'])} / {TARGET_CHARS}")

    # ---------- VARIANT BUTTON ----------
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Vary Comment"):
            st.session_state['current_variant'] += 1
            if st.session_state['current_variant'] > MAX_VARIANTS:
                st.session_state['current_variant'] = 1
            st.session_state['current_comment'] = generate_comment(
                name, att, read, write, read_t, write_t,
                st.session_state['current_pronouns'],
                attitude_target,
                variant=st.session_state['current_variant']
            )
            st.experimental_rerun()
    with col2:
        if st.button("Add Another Comment"):
            st.session_state['all_comments'].append(st.session_state['current_comment'])
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

# ---------- SHOW ALL ADDED COMMENTS ----------
if st.session_state['all_comments']:
    st.markdown("### All Added Comments:")
    for c in st.session_state['all_comments']:
        st.write(c)
