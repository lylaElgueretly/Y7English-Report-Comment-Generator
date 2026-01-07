# =========================================
# STAGE 7 ENGLISH REPORT COMMENT GENERATOR
# Multi-student | Pedagogically sound | ≤490 chars
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

# ---------- READING ACHIEVEMENT ----------
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

# ---------- WRITING ACHIEVEMENT ----------
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
def truncate_comment(comment, max_chars=MAX_CHARS):
    if len(comment) <= max_chars:
        return comment
    else:
        # Truncate at last full stop before max_chars
        truncated = comment[:max_chars]
        if '.' in truncated:
            return truncated.rsplit('.', 1)[0] + '.'
        return truncated

def generate_comment(name, att, read, write, read_t, write_t):
    opening = random.choice(opening_phrases)
    
    comment = (
        f"{opening} {name} {attitude_bank[att]}. "
        f"In reading, {name.lower()} {reading_bank[read]}. "
        f"In writing, {name.lower()} {writing_bank[write]}. "
        f"In the future, {name.lower()} should {reading_target_bank[read_t]}. "
        f"In addition, {name.lower()} should {writing_target_bank[write_t]}."
    )
    
    comment = truncate_comment(comment)
    return comment, len(comment)

# ---------- STREAMLIT APP ----------
st.title("English Report Comment Generator")

if "comments" not in st.session_state:
    st.session_state.comments = []

with st.form(key="comment_form"):
    name = st.text_input("Student Name")
    
    col1, col2 = st.columns(2)
    with col1:
        att = st.selectbox("Attitude to Learning", options=list(attitude_bank.keys()), index=0)
        read = st.selectbox("Reading Achieved", options=list(reading_bank.keys()), index=0)
        write = st.selectbox("Writing Achieved", options=list(writing_bank.keys()), index=0)
    with col2:
        read_t = st.selectbox("Next Steps - Reading", options=list(reading_target_bank.keys()), index=0)
        write_t = st.selectbox("Next Steps - Writing", options=list(writing_target_bank.keys()), index=0)
    
    submitted = st.form_submit_button("Generate Comment")
    
    if submitted and name:
        comment, count = generate_comment(name, att, read, write, read_t, write_t)
        st.session_state.comments.append({"name": name, "comment": comment, "count": count})

# Display all generated comments
if st.session_state.comments:
    st.subheader("Generated Comments")
    for idx, entry in enumerate(st.session_state.comments, 1):
        st.markdown(f"**{idx}. {entry['name']}**")
        st.write(entry['comment'])
        st.write(f"Character count (including spaces): {entry['count']} / {MAX_CHARS}")
        st.write("---")

    # Word download
    def download_word():
        doc = Document()
        for idx, entry in enumerate(st.session_state.comments, 1):
            doc.add_heading(f"{idx}. {entry['name']}", level=2)
            doc.add_paragraph(entry['comment'])
            doc.add_paragraph(f"Character count (including spaces): {entry['count']} / {MAX_CHARS}")
        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)
        return buffer

    st.download_button(
        label="Download All Comments as Word",
        data=download_word(),
        file_name="student_comments.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
