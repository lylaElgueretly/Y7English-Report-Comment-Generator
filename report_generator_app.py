# =========================================
# Streamlit English Report Comment Generator
# Only: Attitude Achieved, Reading/Writing Achieved, Next Steps Reading/Writing
# Editable comments, multiple entries, download as Word
# Max characters 499
# =========================================

import streamlit as st
from docx import Document

MAX_CHARS = 499

# ---------------- BANKS ----------------
attitude_bank = {
    90: "Demonstrates an excellent attitude to learning; highly motivated, consistently engaged, and takes initiative in lessons.",
    85: "Shows a strong attitude to learning; usually focused, motivated, and participates actively.",
    80: "Has a positive attitude to learning; generally attentive and willing to contribute.",
    75: "Shows a good attitude to learning; usually completes tasks on time and engages in class activities.",
    70: "Displays a satisfactory attitude; completes tasks with support and engages occasionally.",
    65: "Demonstrates a developing attitude; sometimes attentive and completes tasks with prompting.",
    60: "Shows a limited attitude; needs regular prompting and reminders to stay on task.",
    55: "Attitude to learning is inconsistent; frequently distracted or passive in class.",
    40: "Shows minimal engagement in learning activities.",
    35: "Rarely demonstrates focus or motivation in learning."
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

reading_next_steps_bank = {
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

writing_next_steps_bank = {
    90: "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
    85: "refine vocabulary and explore more varied sentence structures for impact",
    80: "focus on precise sensory words and showing character emotions",
    75: "add more sensory details and actions that reveal character traits",
    70: "replace telling statements with descriptive or action-based sentences",
    65: "include adjectives, vivid verbs, and sensory details to enhance imagery",
    60: "focus on including at least one sensory detail per paragraph",
    55: "use sentence starters and story maps to add detail",
    40: "begin with simple sentences describing events and character feelings",
    35: "start by sequencing events and describing one action per sentence"
}

# ---------------- HELPERS ----------------
def truncate_comment(comment):
    if len(comment) <= MAX_CHARS:
        return comment
    return comment[:MAX_CHARS].rsplit(' ',1)[0]

def generate_comment(name, att, read, write, read_next, write_next):
    opening = "In this term,"
    comment = (
        f"{opening} {name} {attitude_bank[att]}. "
        f"In reading, {name.lower()} {reading_bank[read]}. "
        f"In writing, {name.lower()} {writing_bank[write]}. "
        f"For the next term, {name.lower()} should {reading_next_steps_bank[read_next]}. "
        f"In addition, {name.lower()} should {writing_next_steps_bank[write_next]}."
    )
    return truncate_comment(comment)

# ---------------- STREAMLIT APP ----------------
st.title("English Report Comment Generator")

if 'comments' not in st.session_state:
    st.session_state.comments = []  # store tuples of (name, comment)

with st.form("student_form"):
    name = st.text_input("Student Name")
    att = st.selectbox("Attitude to Learning Achieved", list(attitude_bank.keys()), index=0)
    read = st.selectbox("Reading Achieved", list(reading_bank.keys()), index=0)
    write = st.selectbox("Writing Achieved", list(writing_bank.keys()), index=0)
    read_next = st.selectbox("Next Steps - Reading", list(reading_next_steps_bank.keys()), index=0)
    write_next = st.selectbox("Next Steps - Writing", list(writing_next_steps_bank.keys()), index=0)
    
    submitted = st.form_submit_button("Generate Comment")
    
    if submitted:
        comment = generate_comment(name, att, read, write, read_next, write_next)
        st.session_state.comments.append([name, comment])

# Display all generated comments with edit option
for i, (name, comment) in enumerate(st.session_state.comments, start=1):
    edited_comment = st.text_area(f"**{i}. {name}**", value=comment, key=f"comment_{i}")
    st.session_state.comments[i-1][1] = edited_comment  # update with edits
    st.write(f"Character count (including spaces): {len(edited_comment)} / {MAX_CHARS}")

st.write("---")

# Generate another comment button (clears form but keeps previous)
if st.button("Generate Another Comment"):
    st.experimental_rerun()

# Download Word button
if st.session_state.comments:
    doc = Document()
    doc.add_heading("English Report Comments", 0)
    for i, (name, comment) in enumerate(st.session_state.comments, start=1):
        doc.add_heading(f"{i}. {name}", level=1)
        doc.add_paragraph(comment)
    doc_name = "English_Report_Comments.docx"
    doc.save(doc_name)
    st.success(f"Word document saved as {doc_name}. Check your folder or Streamlit downloads.")
