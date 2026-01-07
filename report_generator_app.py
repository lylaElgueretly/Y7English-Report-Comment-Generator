# =========================================
# STAGE 7 ENGLISH REPORT COMMENT GENERATOR
# Streamlit Version | Multi-student | Next Steps Included
# =========================================

import streamlit as st
from docx import Document
import random

# ---------- MAX CHARS ----------
MAX_CHARS = 490

# ---------- OPENING PHRASES ----------
opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,",
    "In this term,"
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

# ---------- NEXT STEPS - ATTITUDE ----------
attitude_next_bank = {
    90: "Continue challenging themselves and leading by example in group tasks",
    85: "Maintain engagement and seek opportunities to extend learning independently",
    80: "Increase participation in discussions and take more initiative in independent tasks",
    75: "Focus on asking questions to deepen understanding and improve consistency",
    70: "Work on increasing focus and taking a more active role in lessons",
    65: "Aim to engage more consistently and take responsibility for independent learning",
    60: "Develop personal organisation and focus; try to contribute more during lessons",
    55: "Focus on staying engaged and completing tasks on time with support",
    40: "Begin by setting small targets to complete tasks and participate in lessons",
    35: "Work on basic engagement skills, starting with short, achievable tasks and participation"
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

reading_next_bank = {
    90: "Explore subtler inferences and interpret multiple perspectives to deepen analysis",
    85: "Extend inference skills and examine alternative interpretations",
    80: "Focus on recognising subtler implications and supporting ideas with evidence",
    75: "Practice identifying hidden meanings and making connections within the text",
    70: "Work on identifying implied ideas and summarising main points",
    65: "Focus on reading for meaning and noting key details",
    60: "Strengthen comprehension by paraphrasing and asking questions about the text",
    55: "Build vocabulary and re-read to clarify meaning",
    40: "Identify key events and main points with guided support",
    35: "Begin with guided reading and discussion to identify basic ideas"
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

writing_next_bank = {
    90: "Experiment with subtle suspense, varied perspectives, and advanced sensory effects",
    85: "Refine vocabulary and explore more varied sentence structures for impact",
    80: "Focus on precise sensory words and “showing” character emotions",
    75: "Add more sensory details and actions that reveal character traits",
    70: "Replace “telling” statements with descriptive or action-based sentences",
    65: "Include adjectives, vivid verbs, and sensory details to enhance imagery",
    60: "Focus on including at least one sensory detail per paragraph",
    55: "Use sentence starters and story maps to add detail",
    40: "Begin with simple sentences describing events and character feelings",
    35: "Start by sequencing events and describing one action per sentence"
}

# ---------- HELPERS ----------
def get_band(value, bank):
    try:
        band = int(value)
        return band if band in bank else 0
    except:
        return 0

def truncate_comment(comment, max_chars=MAX_CHARS):
    if len(comment) <= max_chars:
        return comment
    else:
        return comment[:max_chars].rsplit(' ', 1)[0]

# ---------- GENERATE COMMENT ----------
def generate_comment(student):
    opening = random.choice(opening_phrases)
    name = student["name"]
    att = student["attitude"]
    read = student["reading"]
    write = student["writing"]
    read_next = student["reading_next"]
    write_next = student["writing_next"]

    comment = (
        f"{opening} {name} {attitude_bank[att]}. "
        f"In reading, {name.lower()} {reading_bank[read]}. "
        f"In writing, {name.lower()} {writing_bank[write]}. "
        f"In the future, {name.lower()} should {reading_next_bank[read_next]}. "
        f"In addition, {name.lower()} should {writing_next_bank[write_next]}."
    )

    char_count = len(comment)
    if char_count > MAX_CHARS:
        # truncate only achievements, preserve next steps
        achievement_part = (
            f"{opening} {name} {attitude_bank[att]}. "
            f"In reading, {name.lower()} {reading_bank[read]}. "
            f"In writing, {name.lower()} {writing_bank[write]}."
        )
        achievement_part = truncate_comment(achievement_part, MAX_CHARS - 80)  # reserve space for next steps
        comment = (
            f"{achievement_part} "
            f"In the future, {name.lower()} should {reading_next_bank[read_next]}. "
            f"In addition, {name.lower()} should {writing_next_bank[write_next]}."
        )
        char_count = len(comment)

    return comment, char_count

# ---------- STREAMLIT APP ----------
st.set_page_config(page_title="English Report Comment Generator")

st.title("English Report Comment Generator")

if "students" not in st.session_state:
    st.session_state.students = []

with st.form("student_form"):
    name = st.text_input("Student Name")
    attitude = st.selectbox("Attitude to Learning", options=list(attitude_bank.keys()), index=0)
    reading = st.selectbox("Reading Achieved", options=list(reading_bank.keys()), index=0)
    writing = st.selectbox("Writing Achieved", options=list(writing_bank.keys()), index=0)
    reading_next = st.selectbox("Next Steps - Reading", options=list(reading_next_bank.keys()), index=0)
    writing_next = st.selectbox("Next Steps - Writing", options=list(writing_next_bank.keys()), index=0)
    submitted = st.form_submit_button("Generate Comment")

if submitted:
    student_data = {
        "name": name,
        "attitude": attitude,
        "reading": reading,
        "writing": writing,
        "reading_next": reading_next,
        "writing_next": writing_next
    }
    comment, char_count = generate_comment(student_data)
    student_data["comment"] = comment
    student_data["char_count"] = char_count

    st.session_state.students.append(student_data)

# ---------- DISPLAY GENERATED COMMENTS ----------
if st.session_state.students:
    st.subheader("Generated Comments")
    for idx, s in enumerate(st.session_state.students, 1):
        st.markdown(f"**{idx}. {s['name']}**")
        st.write(s['comment'])
        st.write(f"Character count (including spaces): {s['char_count']} / {MAX_CHARS}")

    # ---------- DOWNLOAD AS WORD ----------
    def download_word(students):
        doc = Document()
        doc.add_heading("English Report Comments", 0)
        for idx, s in enumerate(students, 1):
            doc.add_heading(f"{idx}. {s['name']}", level=1)
            doc.add_paragraph(s["comment"])
            doc.add_paragraph(f"Character count: {s['char_count']} / {MAX_CHARS}")
        file_path = "report_comments.docx"
        doc.save(file_path)
        return file_path

    st.download_button(
        label="Download All Comments as Word",
        data=open(download_word(st.session_state.students), "rb").read(),
        file_name="report_comments.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

st.write("---")
st.write("Add another student by filling the form above.")
