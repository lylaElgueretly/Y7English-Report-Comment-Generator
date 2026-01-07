import streamlit as st
import random
from docx import Document
from io import BytesIO

# =========================================
# ENGLISH REPORT COMMENT GENERATOR
# Preserved sentence banks (verbatim)
# Multiple entries | ≤490 chars | Word export
# =========================================

MAX_CHARS = 490

# ---------- OPENING PHRASES ----------
opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,",
    "In this term,",
    "Over the past term,"
]

# ---------- ATTITUDE ----------
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

# ---------- READING ACHIEVEMENT ----------
reading_bank = {
    90: "understanding texts and making insightful interpretations",
    85: "understanding texts confidently and making strong interpretations",
    80: "understanding texts confidently and interpreting key points",
    75: "understanding texts securely and identifying key ideas",
    70: "understanding main ideas in texts with some support",
    65: "identifying key points in texts with guidance",
    60: "showing basic understanding of texts with support",
    55: "understanding simple information in texts",
    40: "understanding texts with support",
    0:  "recognising familiar words but needing significant support to understand texts"
}

# ---------- WRITING ACHIEVEMENT ----------
writing_bank = {
    90: "expressing ideas clearly using varied vocabulary and sentence structures",
    85: "writing confidently using varied sentences and well-chosen vocabulary",
    80: "writing structured pieces with appropriate vocabulary",
    75: "writing organised paragraphs with suitable vocabulary",
    70: "writing clear sentences and simple paragraphs",
    65: "writing simple sentences with some organisation",
    60: "writing short sentences with support",
    55: "structuring simple written responses",
    40: "expressing ideas with support",
    0:  "requiring significant support to form sentences in writing"
}

# ---------- READING TARGET ----------
reading_target_bank = {
    90: "continue analysing texts in greater depth",
    85: "develop more detailed responses to texts",
    80: "explain ideas in greater detail using evidence",
    75: "develop more detailed responses with closer reference to the text",
    70: "build confidence in explaining ideas when reading",
    65: "focus on identifying and explaining key ideas in texts",
    60: "practise understanding main ideas in short texts",
    55: "develop basic reading comprehension skills",
    40: "practise reading regularly to improve understanding",
    0:  "build confidence in recognising basic words and ideas"
}

# ---------- WRITING TARGET ----------
writing_target_bank = {
    90: "refine accuracy further and experiment with more complex structures",
    85: "develop more sophisticated vocabulary and sentence variety",
    80: "vary sentence structures and develop ideas more fully",
    75: "expand ideas further and check accuracy carefully",
    70: "develop ideas in more detail and use a wider range of vocabulary",
    65: "organise ideas more clearly and write in full sentences",
    60: "extend written responses beyond short sentences",
    55: "focus on basic sentence structure and spelling",
    40: "practise writing simple sentences",
    0:  "build confidence in writing through regular guided practice"
}

# ---------- HELPERS ----------
def get_band(value):
    try:
        value = int(value)
        return value if value in attitude_bank else 0
    except:
        return 0

def truncate_comment(text, max_chars):
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(" ", 1)[0]

def get_pronouns(gender):
    if gender == "Female":
        return "she", "her"
    return "he", "his"

def generate_comment(name, gender, att, read, write, read_t, write_t):
    p, poss = get_pronouns(gender)
    opening = random.choice(opening_phrases)

    reading_phrase = (
        f"demonstrated {reading_bank[read]}"
        if read >= 75 else f"experienced difficulty {reading_bank[read]}"
    )
    writing_phrase = (
        f"demonstrated {writing_bank[write]}"
        if write >= 75 else f"experienced difficulty {writing_bank[write]}"
    )

    comment = (
        f"{opening} {name} {attitude_bank[att]}. "
        f"{p.capitalize()} {reading_phrase} and {writing_phrase}, "
        f"which reflected {poss} current level of confidence. "
        f"Next term, {p} should {reading_target_bank[read_t]}, "
        f"{writing_target_bank[write_t]}."
    )

    comment = truncate_comment(comment, MAX_CHARS)
    return comment, len(comment)

# ---------- STREAMLIT UI ----------
st.title("English Report Comment Generator")

if "entries" not in st.session_state:
    st.session_state.entries = []

name = st.text_input("Student Name")
gender = st.selectbox("Gender", ["Male", "Female"])

att = st.selectbox("Attitude to Learning", sorted(attitude_bank.keys(), reverse=True))
read = st.selectbox("Reading Achieved", sorted(reading_bank.keys(), reverse=True))
write = st.selectbox("Writing Achieved", sorted(writing_bank.keys(), reverse=True))
read_t = st.selectbox("Next Steps – Reading", sorted(reading_target_bank.keys(), reverse=True))
write_t = st.selectbox("Next Steps – Writing", sorted(writing_target_bank.keys(), reverse=True))

if st.button("Generate Comment"):
    if name:
        comment, count = generate_comment(name, gender, att, read, write, read_t, write_t)
        st.session_state.entries.append((name, comment, count))

if st.session_state.entries:
    st.subheader("Generated Comments")
    for i, (n, c, cnt) in enumerate(st.session_state.entries, 1):
        st.markdown(f"**{i}. {n}**")
        st.write(c)
        st.caption(f"Character count (including spaces): {cnt} / {MAX_CHARS}")

    if st.button("Download as Word"):
        doc = Document()
        for n, c, _ in st.session_state.entries:
            doc.add_paragraph(f"{n}\n{c}\n")

        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        st.download_button(
            label="Download Word File",
            data=buffer,
            file_name="English_Report_Comments.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
