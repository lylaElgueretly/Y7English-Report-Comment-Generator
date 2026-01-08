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

def generate_comment(name, att, read, write, read_t, write_t, pronouns, variation_index=0, attitude_target=None):
    p, p_poss = pronouns
    opening = random.choice(opening_phrases)

    # pick phrase according to variation index
    att_phrase = attitude_bank[att][variation_index % len(attitude_bank[att])]
    read_phrase = reading_bank[read][variation_index % len(reading_bank[read])]
    write_phrase = writing_bank[write][variation_index % len(writing_bank[write])]
    read_target_phrase = reading_target_bank[read_t][variation_index % len(reading_target_bank[read_t])]
    write_target_phrase = writing_target_bank[write_t][variation_index % len(writing_target_bank[write_t])]

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
    "Fill in the student details and click **Generate Comment**. Click **Vary Comment** to cycle through variants."
)

if 'all_comments' not in st.session_state:
    st.session_state['all_comments'] = []

if 'variation_index' not in st.session_state:
    st.session_state['variation_index'] = {}

# Form for student details
with st.form("report_form"):
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    att = st.selectbox("Attitude band", [90,85,80,75,70,65,60,55,40])
    read = st.selectbox("Reading achievement band", [90,85,80,75,70,65,60,55,40])
    write = st.selectbox("Writing achievement band", [90,85,80,75,70,65,60,55,40])
    read_t = st.selectbox("Reading target band", [90,85,80,75,70,65,60,55,40])
    write_t = st.selectbox("Writing target band", [90,85,80,75,70,65,60,55,40])
    
    # Optional attitude next steps
    attitude_target = st.text_input("Optional Attitude Next Steps")

    submitted = st.form_submit_button("Generate Comment")

# Generate default comment
if submitted and name:
    pronouns = get_pronouns(gender)
    st.session_state['variation_index'][name] = 0
    comment = generate_comment(
        name, att, read, write, read_t, write_t, pronouns,
        variation_index=st.session_state['variation_index'][name],
        attitude_target=attitude_target
    )
    edited_comment = st.text_area(f"{name} (Variant 1)", value=comment, height=200)

    # Save to session
    st.session_state['all_comments'].append({
        "name": name,
        "att": att,
        "read": read,
        "write": write,
        "read_t": read_t,
        "write_t": write_t,
        "gender": gender,
        "attitude_target": attitude_target,
        "comment": edited_comment,
        "variant": 1
    })

# ---------- VARY COMMENT ----------
if st.session_state['all_comments']:
    for i, entry in enumerate(st.session_state['all_comments']):
        if st.button(f"Vary Comment for {entry['name']}"):
            # Increment variation index
            name = entry['name']
            pronouns = get_pronouns(entry['gender'])
            st.session_state['variation_index'][name] += 1
            var_index = st.session_state['variation_index'][name]

            # Re-generate comment
            new_comment = generate_comment(
                name,
                entry['att'],
                entry['read'],
                entry['write'],
                entry['read_t'],
                entry['write_t'],
                pronouns,
                variation_index=var_index,
                attitude_target=entry['attitude_target']
            )

            # Update entry
            entry['comment'] = new_comment
            entry['variant'] = (var_index % 3) + 1  # show 1-3
            st.experimental_rerun()

# ---------- DOWNLOAD FULL REPORT ----------
if st.session_state['all_comments']:
    if st.button("Download Full Report (Word)"):
        doc = Document()
        for c in st.session_state['all_comments']:
            doc.add_paragraph(f"{c['name']} (Variant {c['variant']}): {c['comment']}")
        
        # Use in-memory BytesIO
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
        st.write(f"{c['name']} (Variant {c['variant']}): {c['comment']}")
