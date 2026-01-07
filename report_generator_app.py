# =========================================
# STAGE 7 ENGLISH REPORT COMMENT GENERATOR
# Streamlit version
# Multiple students | Pedagogically sound | Custom next steps
# =========================================

import streamlit as st
import random
from docx import Document
from io import BytesIO

MAX_CHARS = 490

# ---------- OPENING PHRASES ----------
opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,",
    "In this term,"
]

# ---------- ATTITUDE TO LEARNING ----------
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

attitude_next_bank = {
    90: "continue challenging themselves and leading by example in group tasks",
    85: "maintain engagement and seek opportunities to extend learning independently",
    80: "increase participation in discussions and take more initiative in independent tasks",
    75: "focus on asking questions to deepen understanding and improve consistency",
    70: "work on increasing focus and taking a more active role in lessons",
    65: "aim to engage more consistently and take responsibility for independent learning",
    60: "develop personal organisation and focus; try to contribute more during lessons",
    55: "focus on staying engaged and completing tasks on time with support",
    40: "begin by setting small targets to complete tasks and participate in lessons",
    35: "work on basic engagement skills, starting with short, achievable tasks and participation"
}

# ---------- READING BANKS ----------
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

# ---------- WRITING BANKS ----------
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

writing_target_bank = {
    90: "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
    85: "refine vocabulary and explore more varied sentence structures for impact",
    80: "focus on precise sensory words and showing character emotions",
    75: "add more sensory details and actions that reveal character traits",
    70: "replace 'telling' statements with descriptive or action-based sentences",
    65: "include adjectives, vivid verbs, and sensory details to enhance imagery",
    60: "focus on including at least one sensory detail per paragraph",
    55: "use sentence starters and story maps to add detail",
    40: "begin with simple sentences describing events and character feelings",
    35: "start by sequencing events and describing one action per sentence"
}

# ---------- HELPER FUNCTIONS ----------
def truncate_comment(comment, max_chars=MAX_CHARS):
    if len(comment) <= max_chars:
        return comment
    else:
        return comment[:max_chars].rsplit(' ', 1)[0]

def generate_comment(student):
    opening = random.choice(opening_phrases)
    comment = (
        f"{opening} {student['name']} {attitude_bank[student['attitude']]}."
        f" In reading, {student['name'].lower()} {reading_bank[student['reading_ach']]}."
        f" In writing, {student['name'].lower()} {writing_bank[student['writing_ach']]}."
        f" In the future, {student['name'].lower()} should {reading_target_bank[student['reading_next']]}."
        f" In addition, {student['name'].lower()} should {writing_target_bank[student['writing_next']]}."
    )
    truncated = truncate_comment(comment)
    return truncated, len(truncated)

# ---------- STREAMLIT UI ----------
st.title("English Report Comment Generator")

if 'students' not in st.session_state:
    st.session_state.students = []

with st.form("student_form", clear_on_submit=True):
    name = st.text_input("Student Name")
    attitude = st.selectbox("Attitude to Learning", sorted(attitude_bank.keys(), reverse=True))
    reading_ach = st.selectbox("Reading Achieved", sorted(reading_bank.keys(), reverse=True))
    writing_ach = st.selectbox("Writing Achieved", sorted(writing_bank.keys(), reverse=True))
    reading_next = st.selectbox("Next Steps - Reading", sorted(reading_target_bank.keys(), reverse=True))
    writing_next = st.selectbox("Next Steps - Writing", sorted(writing_target_bank.keys(), reverse=True))
    
    submitted = st.form_submit_button("Generate Comment")
    
    if submitted:
        student = {
            "name": name,
            "attitude": attitude,
            "reading_ach": reading_ach,
            "writing_ach": writing_ach,
            "reading_next": reading_next,
            "writing_next": writing_next
        }
        st.session_state.students.append(student)

# ---------- DISPLAY GENERATED COMMENTS ----------
if st.session_state.students:
    st.header("Generated Comments")
    for i, student in enumerate(st.session_state.students, start=1):
        comment_text, char_count = generate_comment(student)
        st.markdown(f"**{i}. {student['name']}**")
        st.write(comment_text)
        st.write(f"Character count (including spaces): {char_count} / {MAX_CHARS}")

    # ---------- DOWNLOAD AS WORD ----------
    def download_word():
        doc = Document()
        for student in st.session_state.students:
            comment_text, _ = generate_comment(student)
            doc.add_paragraph(f"{student['name']}")
            doc.add_paragraph(comment_text)
            doc.add_paragraph("")
        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)
        return buffer

    st.download_button(
        label="Download Comments as Word",
        data=download_word(),
        file_name="student_comments.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

