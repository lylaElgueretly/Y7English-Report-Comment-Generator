# =========================================
# ENGLISH REPORT COMMENT GENERATOR
# =========================================

import random
import streamlit as st
from docx import Document

MAX_CHARS = 490

# ---------- OPENING PHRASES ----------
opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,",
    "In this term,"
]

# ---------- ACHIEVEMENT BANKS ----------
attitude_bank = {
    90: "approached learning with enthusiasm and confidence, showing independence and curiosity",
    85: "demonstrated a highly positive and motivated attitude towards learning",
    80: "showed a positive and motivated attitude towards learning and participated confidently",
    75: "showed consistent effort and engaged well in class activities",
    70: "was generally focused and responded well to guidance",
    65: "showed a steady approach to learning but benefited from encouragement",
    60: "required support to remain focused and engaged in lessons",
    55: "needed regular guidance to remain engaged and confident",
    40: "found it challenging to stay focused and required consistent encouragement",
    0:  "required significant support to engage confidently in learning"
}

reading_bank = {
    90: "understood texts and made insightful interpretations",
    85: "understood texts confidently and made strong interpretations",
    80: "understood texts confidently and interpreted key points",
    75: "understood texts securely and identified key ideas",
    70: "understood main ideas in texts with some support",
    65: "identified key points in texts with guidance",
    60: "showed basic understanding of texts with support",
    55: "understood simple information in texts",
    40: "understood texts with support",
    0:  "recognised familiar words but needed significant support to understand texts"
}

writing_bank = {
    90: "expressed ideas clearly using varied vocabulary and sentence structures",
    85: "wrote confidently using varied sentences and well-chosen vocabulary",
    80: "wrote structured pieces with appropriate vocabulary",
    75: "wrote organised paragraphs with suitable vocabulary",
    70: "wrote clear sentences and simple paragraphs",
    65: "wrote simple sentences with some organisation",
    60: "wrote short sentences with support",
    55: "structured simple written responses",
    40: "expressed ideas with support",
    0:  "required significant support to form sentences in writing"
}

# ---------- HELPERS ----------
def get_pronouns(gender):
    gender = gender.lower()
    if gender == "male":
        return "he", "his"
    elif gender == "female":
        return "she", "her"
    else:
        return "they", "their"

def lowercase_first(text):
    return text[0].lower() + text[1:] if text else ""

def strip_trailing_punct(text):
    return text.rstrip(". ,;")

def truncate_comment(comment, max_chars=MAX_CHARS):
    if len(comment) <= max_chars:
        return comment
    truncated = comment[:max_chars].rstrip(" ,;.")
    if "." in truncated:
        truncated = truncated[:truncated.rfind(".")+1]
    return truncated

def generate_comment(name, att, read, write, read_next, write_next, pronouns):
    p, _ = pronouns
    opening = random.choice(opening_phrases)

    attitude_sentence = f"{opening} {name} {attitude_bank[att]}."
    reading_sentence = f"In reading, {p} {reading_bank[read]}."
    writing_sentence = f"In writing, {p} {writing_bank[write]}."
    reading_target_sentence = f"For the next term, {p} should {lowercase_first(strip_trailing_punct(reading_bank[read_next]))}."
    writing_target_sentence = f"Additionally, {p} should {lowercase_first(strip_trailing_punct(writing_bank[write_next]))}."

    comment = " ".join([
        attitude_sentence,
        reading_sentence,
        writing_sentence,
        reading_target_sentence,
        writing_target_sentence
    ])

    comment = truncate_comment(comment)
    return comment, len(comment)

# =========================================
# STREAMLIT APP
# =========================================
st.title("English Report Comment Generator")
st.markdown("Fill in the student details and click **Generate Comment**. You can generate multiple entries and download the report as a Word file.")

# Store entries
if "entries" not in st.session_state:
    st.session_state.entries = []

# ---------- FORM ----------
with st.form("report_form"):
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    att = st.selectbox("Attitude to Learning", [90,85,80,75,70,65,60,55,40])
    read = st.selectbox("Reading Achieved", [90,85,80,75,70,65,60,55,40])
    write = st.selectbox("Writing Achieved", [90,85,80,75,70,65,60,55,40])
    read_next = st.selectbox("Next Steps - Reading", [90,85,80,75,70,65,60,55,40])
    write_next = st.selectbox("Next Steps - Writing", [90,85,80,75,70,65,60,55,40])

    submitted = st.form_submit_button("Generate Comment")

# ---------- PROCESS ----------
if submitted and name:
    pronouns = get_pronouns(gender)
    comment, char_count = generate_comment(name, att, read, write, read_next, write_next, pronouns)
    
    st.text_area("Generated Comment", value=comment, height=200)
    st.write(f"Character count (including spaces): {char_count} / {MAX_CHARS}")

    # Add to entries
    st.session_state.entries.append({
        "Name": name,
        "Comment": comment,
        "Characters": char_count
    })

# ---------- SHOW ENTRIES ----------
if st.session_state.entries:
    st.subheader(f"Entries so far: {len(st.session_state.entries)}")
    for i, entry in enumerate(st.session_state.entries, 1):
        st.write(f"{i}. {entry['Name']} ({entry['Characters']} chars)")

# ---------- DOWNLOAD WORD FILE ----------
if st.session_state.entries:
    doc = Document()
    for entry in st.session_state.entries:
        doc.add_paragraph(f"{entry['Name']}:\n{entry['Comment']}\n")
    word_name = "English_Report.docx"
    doc.save(word_name)
    with open(word_name, "rb") as f:
        st.download_button("Download Word Report", data=f, file_name=word_name, mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
