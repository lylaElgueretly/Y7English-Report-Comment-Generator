# report_generator_app.py
import streamlit as st
import random
from docx import Document
from io import BytesIO

# ===============================
# CONFIG
# ===============================
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
    90: "demonstrates an excellent attitude to learning; highly motivated, consistently engaged, and takes initiative in lessons",
    85: "shows a strong attitude to learning; usually focused, motivated, and participates actively",
    80: "has a positive attitude to learning; generally attentive and willing to contribute",
    75: "shows a good attitude to learning; usually completes tasks on time and engages in class activities",
    70: "displays a satisfactory attitude; completes tasks with support and engages occasionally",
    65: "demonstrates a developing attitude; sometimes attentive and completes tasks with prompting",
    60: "shows a limited attitude; needs regular prompting and reminders to stay on task",
    55: "attitude to learning is inconsistent; frequently distracted or passive in class",
    40: "shows minimal engagement in learning activities",
    35: "rarely demonstrates focus or motivation in learning"
}

reading_bank = {
    90: "demonstrates excellent understanding of explicit and implicit ideas in texts",
    85: "shows strong understanding of explicit and some implicit ideas",
    80: "understands main ideas and some supporting details",
    75: "shows good understanding of main ideas with occasional inference",
    70: "understands basic ideas; limited inference",
    65: "identifies a few ideas with minimal inference",
    60: "recognises simple ideas",
    55: "understands very basic ideas",
    40: "struggles to identify ideas",
    35: "minimal comprehension of texts"
}

writing_bank = {
    90: "writes highly engaging narratives, showing not telling, with vivid verbs and sensory language",
    85: "writes engaging narratives with effective descriptive and sensory detail",
    80: "produces clear narratives using some descriptive and sensory language",
    75: "writes coherent narratives with occasional description",
    70: "uses basic description; narrative is simple",
    65: "narrative is straightforward; limited descriptive detail",
    60: "very basic narrative with minimal description",
    55: "narrative is underdeveloped",
    40: "struggles to write narratives",
    35: "writing lacks narrative sense"
}

reading_next_bank = {
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

writing_next_bank = {
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

# ---------- HELPERS ----------
def safe_truncate(text, max_len):
    if len(text) <= max_len:
        return text
    return text[:max_len].rsplit(' ',1)[0]

def generate_comment(student, max_chars=MAX_CHARS):
    # Split max_chars into sections
    budgets = [120, 90, 90, 90, 90]  # opening/attitude, reading, writing, reading next, writing next
    
    sections = [
        f"{random.choice(opening_phrases)} {student['name']} {attitude_bank[student['attitude']]}",
        f"In reading, {student['name'].lower()} {reading_bank[student['reading']]}",
        f"In writing, {student['name'].lower()} {writing_bank[student['writing']]}",
        f"In the future, {student['name'].lower()} should {reading_next_bank[student['reading_next']]}",
        f"In addition, {student['name'].lower()} should {writing_next_bank[student['writing_next']]}"
    ]
    
    truncated_sections = [safe_truncate(s,b) for s,b in zip(sections, budgets)]
    comment = ". ".join(truncated_sections) + "."
    return comment, len(comment)

def create_word_download(comments):
    doc = Document()
    for i, c in enumerate(comments, start=1):
        doc.add_paragraph(f"{i}. {c['name']}\n")
        doc.add_paragraph(c['comment'])
        doc.add_paragraph(f"Character count (including spaces): {c['count']} / {MAX_CHARS}\n")
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

# ===============================
# STREAMLIT APP
# ===============================
st.title("English Report Comment Generator")

if 'students' not in st.session_state:
    st.session_state.students = []

with st.form(key='student_form'):
    name = st.text_input("Student Name")
    attitude = st.selectbox("Attitude to Learning", sorted(attitude_bank.keys(), reverse=True))
    reading = st.selectbox("Reading Achievement", sorted(reading_bank.keys(), reverse=True))
    writing = st.selectbox("Writing Achievement", sorted(writing_bank.keys(), reverse=True))
    reading_next = st.selectbox("Next Step - Reading", sorted(reading_next_bank.keys(), reverse=True))
    writing_next = st.selectbox("Next Step - Writing", sorted(writing_next_bank.keys(), reverse=True))
    
    submit = st.form_submit_button("Generate Comment")
    
    if submit and name:
        student = {
            'name': name.strip(),
            'attitude': attitude,
            'reading': reading,
            'writing': writing,
            'reading_next': reading_next,
            'writing_next': writing_next
        }
        comment, count = generate_comment(student)
        student['comment'] = comment
        student['count'] = count
        st.session_state.students.append(student)

# Display generated comments
if st.session_state.students:
    st.subheader("Generated Comments")
    for i, s in enumerate(st.session_state.students, s_
