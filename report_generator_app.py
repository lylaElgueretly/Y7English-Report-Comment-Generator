# report_generator_app.py
import streamlit as st
from docx import Document
import random

MAX_CHARS = 499

st.set_page_config(page_title="English Report Comment Generator", layout="centered")

# ------------------ BANKS ------------------
attitude_bank = {
    90: "approached learning with enthusiasm and confidence, showing independence and curiosity",
    85: "showed a strong attitude to learning; usually focused, motivated, and participates actively",
    80: "had a positive attitude to learning; generally attentive and willing to contribute",
    75: "showed a good attitude to learning; usually completes tasks on time and engages in class activities",
    70: "displays a satisfactory attitude; completes tasks with support and engages occasionally",
    65: "demonstrated a developing attitude; sometimes attentive and completes tasks with prompting",
    60: "shows a limited attitude; needs regular prompting and reminders to stay on task",
    55: "attitude to learning is inconsistent; frequently distracted or passive in class",
    40: "shows minimal engagement in learning activities",
    35: "rarely demonstrates focus or motivation in learning"
}

reading_bank = {
    90: "understood texts and made insightful interpretations",
    85: "understood texts confidently and made strong interpretations",
    80: "understood main ideas and some supporting details",
    75: "understood main ideas with occasional inference",
    70: "understood basic ideas; limited inference",
    65: "identified a few ideas with minimal inference",
    60: "recognised simple ideas",
    55: "understood very basic ideas",
    40: "struggled to identify ideas",
    35: "had minimal comprehension of texts"
}

writing_bank = {
    90: "wrote highly engaging narratives, showing not telling, with vivid verbs and sensory language",
    85: "wrote engaging narratives with effective descriptive and sensory detail",
    80: "produced clear narratives using some descriptive and sensory language",
    75: "wrote coherent narratives with occasional description",
    70: "used basic description; narrative is simple",
    65: "narrative is straightforward; limited descriptive detail",
    60: "very basic narrative with minimal description",
    55: "narrative is underdeveloped",
    40: "struggled to write narratives",
    35: "writing lacks narrative sense"
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

opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,",
    "In this term,"
]

# ------------------ HELPERS ------------------
def generate_comment(name, att, read, write, read_t, write_t):
    opening = random.choice(opening_phrases)
    comment = (
        f"{opening} {name} {attitude_bank[att]}. "
        f"In reading, {name.lower()} {reading_bank[read]}. "
        f"In writing, {name.lower()} {writing_bank[write]}. "
        f"For the next term, {name.lower()} should {reading_target_bank[read_t]}. "
        f"In addition, {name.lower()} should {writing_target_bank[write_t]}."
    )
    if len(comment) > MAX_CHARS:
        comment = comment[:MAX_CHARS].rsplit(' ', 1)[0] + "."
    return comment, len(comment)

# ------------------ STREAMLIT APP ------------------
st.title("English Report Comment Generator")

# Session state to store multiple students
if "students" not in st.session_state:
    st.session_state.students = []

def add_student():
    comment, char_count = generate_comment(
        st.session_state.name,
        st.session_state.att,
        st.session_state.read,
        st.session_state.write,
        st.session_state.read_t,
        st.session_state.write_t
    )
    st.session_state.students.append({
        "name": st.session_state.name,
        "comment": comment,
        "char_count": char_count
    })

with st.form("student_form"):
    st.subheader("Enter Student Details")
    st.text_input("Student Name", key="name")
    st.selectbox("Attitude to Learning (achieved)", list(attitude_bank.keys()), index=0, key="att")
    st.selectbox("Reading Achieved", list(reading_bank.keys()), index=0, key="read")
    st.selectbox("Writing Achieved", list(writing_bank.keys()), index=0, key="write")
    st.selectbox("Next Steps - Reading", list(reading_target_bank.keys()), index=0, key="read_t")
    st.selectbox("Next Steps - Writing", list(writing_target_bank.keys()), index=0, key="write_t")

    submitted = st.form_submit_button("Generate Comment for Student", on_click=add_student)

# ------------------ DISPLAY COMMENTS ------------------
if st.session_state.students:
    st.subheader("Generated Comments")
    for i, s in enumerate(st.session_state.students, start=1):
        st.markdown(f"**{i}. {s['name']}**")
        st.write(s["comment"])
        st.write(f"Character count (including spaces): {s['char_count']} / {MAX_CHARS}")
        st.write("---")

# ------------------ DOWNLOAD AS WORD ------------------
if st.session_state.students:
    if st.button("Download All Comments as Word"):
        doc = Document()
        for i, s in enumerate(st.session_state.students, start=1):
            doc.add_paragraph(f"{i}. {s['name']}")
            doc.add_paragraph(s["comment"])
            doc.add_paragraph(f"Character count (including spaces): {s['char_count']} / {MAX_CHARS}")
            doc.add_paragraph("\n")
        doc_name = "English_Report_Comments.docx"
        doc.save(doc_name)
        st.success(f"Word document saved as {doc_name}. Check your folder or Streamlit downloads.")
