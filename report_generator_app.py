# =========================================
# STAGE 7 ENGLISH REPORT COMMENT GENERATOR
# Pedagogically sound, full sentences, multi-student
# =========================================

import streamlit as st
from docx import Document
import random

st.set_page_config(page_title="Y7 English Report Comment Generator", layout="wide")

# ----------------------
# BANKS OF STATEMENTS
# ----------------------

# Attitude to Learning
attitude_bank = {
    90: "approached learning with enthusiasm and confidence, showing independence and curiosity",
    85: "showed consistent effort and engaged well in class activities",
    80: "had a positive attitude to learning; generally attentive and willing to contribute",
    75: "showed good effort; usually completes tasks on time and participates in class",
    70: "displayed satisfactory engagement; completes tasks with support",
    65: "demonstrated a developing attitude; sometimes attentive with prompting",
    60: "showed limited focus; requires regular reminders",
    55: "was inconsistent in attention; frequently distracted or passive",
    40: "showed minimal engagement in learning activities",
    35: "rarely demonstrated focus or motivation"
}

attitude_next_bank = {
    90: "Continue challenging themselves and leading by example in group tasks.",
    85: "Maintain engagement and seek opportunities to extend learning independently.",
    80: "Increase participation in discussions and take more initiative in independent tasks.",
    75: "Focus on asking questions to deepen understanding and improve consistency.",
    70: "Work on increasing focus and taking a more active role in lessons.",
    65: "Aim to engage more consistently and take responsibility for independent learning.",
    60: "Develop personal organisation and focus; try to contribute more during lessons.",
    55: "Focus on staying engaged and completing tasks on time with support.",
    40: "Begin by setting small targets to complete tasks and participate in lessons.",
    35: "Work on basic engagement skills, starting with short, achievable tasks and participation."
}

# Reading
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
    90: "Explore subtler inferences and interpret multiple perspectives to deepen analysis.",
    85: "Extend inference skills and examine alternative interpretations.",
    80: "Focus on recognising subtler implications and supporting ideas with evidence.",
    75: "Practice identifying hidden meanings and making connections within the text.",
    70: "Work on identifying implied ideas and summarising main points.",
    65: "Focus on reading for meaning and noting key details.",
    60: "Strengthen comprehension by paraphrasing and asking questions about the text.",
    55: "Build vocabulary and re-read to clarify meaning.",
    40: "Identify key events and main points with guided support.",
    35: "Begin with guided reading and discussion to identify basic ideas."
}

# Writing
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
    90: "Experiment with subtle suspense, varied perspectives, and advanced sensory effects.",
    85: "Refine vocabulary and explore more varied sentence structures for impact.",
    80: "Focus on precise sensory words and 'showing' character emotions.",
    75: "Add more sensory details and actions that reveal character traits.",
    70: "Replace 'telling' statements with descriptive or action-based sentences.",
    65: "Include adjectives, vivid verbs, and sensory details to enhance imagery.",
    60: "Focus on including at least one sensory detail per paragraph.",
    55: "Use sentence starters and story maps to add detail.",
    40: "Begin with simple sentences describing events and character feelings.",
    35: "Start by sequencing events and describing one action per sentence."
}

# ----------------------
# HELPER FUNCTIONS
# ----------------------
def get_pronouns(gender):
    gender = gender.lower()
    if gender in ['male', 'm']:
        return "he", "his"
    elif gender in ['female', 'f']:
        return "she", "her"
    else:
        return "they", "their"

def truncate_comment(comment, max_chars=490):
    if len(comment) <= max_chars:
        return comment
    else:
        # Truncate safely at word boundary
        return comment[:max_chars].rsplit(' ', 1)[0]

def generate_comment(name, gender, att, read, write, att_next, read_next, write_next):
    p, poss = get_pronouns(gender)
    # Build comment in sections
    comment = (
        f"In this term, {name} {attitude_bank[att]}. "
        f"In reading, {p} {reading_bank[read]}. "
        f"In writing, {p} {writing_bank[write]}. "
        f"For the next term, {p} should {reading_next_bank[read_next]} "
        f"In addition, {p} should {writing_next_bank[write_next]}"
    )
    return truncate_comment(comment), len(comment)

# ----------------------
# STREAMLIT INTERFACE
# ----------------------
st.title("English Report Comment Generator")

students = []

with st.form("student_form"):
    st.subheader("Enter Student Details")
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    att = st.selectbox("Attitude to Learning", list(attitude_bank.keys()), index=0)
    att_next = st.selectbox("Next Steps - Attitude to Learning", list(attitude_next_bank.keys()), index=0)
    read = st.selectbox("Reading Achieved", list(reading_bank.keys()), index=0)
    read_next = st.selectbox("Next Steps - Reading", list(reading_next_bank.keys()), index=0)
    write = st.selectbox("Writing Achieved", list(writing_bank.keys()), index=0)
    write_next = st.selectbox("Next Steps - Writing", list(writing_next_bank.keys()), index=0)
    
    submitted = st.form_submit_button("Generate Comment")
    
    if submitted:
        comment, char_count = generate_comment(
            name, gender, att, read, write, att_next, read_next, write_next
        )
        students.append({"name": name, "comment": comment, "chars": char_count})
        st.success(f"Comment generated for {name} ({char_count} chars)")
        
# ----------------------
# DISPLAY GENERATED COMMENTS
# ----------------------
if students:
    st.subheader("Generated Comments")
    for idx, s in enumerate(students, 1):
        st.markdown(f"**{idx}. {s['name']}**")
        st.write(s['comment'])
        st.write(f"Character count (including spaces): {s['chars']} / 490")

# ----------------------
# DOWNLOAD COMMENTS AS WORD FILE
# ----------------------
if students:
    if st.button("Download Comments as Word"):
        doc = Document()
        doc.add_heading("Generated Report Comments", 0)
        for idx, s in enumerate(students, 1):
            doc.add_paragraph(f"{idx}. {s['name']}")
            doc.add_paragraph(s['comment'])
            doc.add_paragraph(f"Character count: {s['chars']} / 490\n")
        doc.save("report_comments.docx")
        with open("report_comments.docx", "rb") as file:
            st.download_button("Download Word file", file, file_name="report_comments.docx")
