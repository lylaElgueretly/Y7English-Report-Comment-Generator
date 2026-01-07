# =========================================
# ENGLISH REPORT COMMENT GENERATOR
# Multiple students | ~450-490 chars | Word download
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

# ---------- WRITING ACHIEVEMENT ----------
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

# ---------- READING TARGET ----------
reading_target_bank = {
    90: "explore subtler inferences and interpret multiple perspectives to deepen analysis",
    85: "extend inference skills and examine alternative interpretations",
    80: "focus on recognising subtler implications and supporting ideas with evidence",
    75: "practice identifying hidden meanings and making connections within the text",
    70: "work on identifying implied ideas and summarising main points",
    65: "focus on reading for meaning and noting key details",
    60: "strengthen comprehension by paraphrasing and asking questions about the text",
    55: "build vocabulary and re-read to clarify meaning",
    40: "identify key events and main points with guided support",
    35: "begin with guided reading and discussion to identify basic ideas"
}

# ---------- WRITING TARGET ----------
writing_target_bank = {
    90: "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
    85: "refine vocabulary and explore more varied sentence structures for impact",
    80: "focus on precise sensory words and 'showing' character emotions",
    75: "add more sensory details and actions that reveal character traits",
    70: "replace 'telling' statements with descriptive or action-based sentences",
    65: "include adjectives, vivid verbs, and sensory details to enhance imagery",
    60: "focus on including at least one sensory detail per paragraph",
    55: "use sentence starters and story maps to add detail",
    40: "begin with simple sentences describing events and character feelings",
    35: "start by sequencing events and describing one action per sentence"
}

# ---------- CLOSER ----------
closer_bank = [
    "Overall, progress was evident over the course of the term.",
    "With continued support, further progress is expected next term.",
    "Confidence improved gradually as the term progressed."
]

# ---------- HELPERS ----------
def truncate_comment(comment, max_chars=490):
    if len(comment) <= max_chars:
        return comment
    truncated = comment[:max_chars].rstrip(" ,;.") 
    if "." in truncated:
        truncated = truncated[:truncated.rfind(".")+1]
    return truncated

def generate_comment(name, att, read, write, read_t, write_t):
    opening = random.choice(opening_phrases)
    comment = (
        f"{opening} {name} {attitude_bank[att]}. "
        f"In reading, {name.lower()} {reading_bank[read]}. "
        f"In writing, {name.lower()} {writing_bank[write]}. "
        f"For the next term, {name.lower()} should {reading_target_bank[read_t]}. "
        f"Additionally, {name.lower()} should {writing_target_bank[write_t]}. "
        f"{closer_bank[0]}"
    )
    comment = truncate_comment(comment, MAX_CHARS)
    return comment, len(comment)

# ---------- STREAMLIT APP ----------
st.title("English Report Comment Generator")

if "entries" not in st.session_state:
    st.session_state.entries = []

with st.form("student_form"):
    name = st.text_input("Student Name")
    att = st.selectbox("Attitude to Learning", sorted(attitude_bank.keys(), reverse=True))
    read = st.selectbox("Reading Achieved", sorted(reading_bank.keys(), reverse=True))
    write = st.selectbox("Writing Achieved", sorted(writing_bank.keys(), reverse=True))
    read_t = st.selectbox("Next Steps - Reading", sorted(reading_target_bank.keys(), reverse=True))
    write_t = st.selectbox("Next Steps - Writing", sorted(writing_target_bank.keys(), reverse=True))

    submitted = st.form_submit_button("Generate Comment")

if submitted and name:
    comment, char_count = generate_comment(name, att, read, write, read_t, write_t)
    st.session_state.entries.append((name, comment, char_count))

# ---------- DISPLAY ALL GENERATED COMMENTS ----------
if st.session_state.entries:
    st.subheader("Generated Comments")
    for i, (student_name, comment, char_count) in enumerate(st.session_state.entries, 1):
        st.markdown(f"**{i}. {student_name}**")
        st.write(comment)
        st.write(f"Character count (including spaces): {char_count} / {MAX_CHARS}")

# ---------- ADD ANOTHER STUDENT BUTTON ----------
if st.session_state.entries:
    if st.button("Add Another Student"):
        st.experimental_rerun()

# ---------- DOWNLOAD WORD FILE ----------
if st.session_state.entries:
    doc = Document()
    for i, (student_name, comment, _) in enumerate(st.session_state.entries, 1):
        doc.add_paragraph(f"{i}. {student_name}")
        doc.add_paragraph(comment)
        doc.add_paragraph("")  # space between comments
    file_name = "English_Report_Comments.docx"
    doc.save(file_name)
    with open(file_name, "rb") as f:
        st.download_button("Download Word Report", f, file_name=file_name,
                           mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
