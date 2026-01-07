# =========================================
# STAGE 7 ENGLISH REPORT COMMENT GENERATOR - Streamlit Version
# Multiple Student Entries & Combined Download
# =========================================

import random
import streamlit as st
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

attitude_target_bank = {
    90: "Continue challenging themselves and lead by example in group tasks, extending learning independently.",
    85: "Maintain engagement and actively seek opportunities to deepen understanding and skills.",
    80: "Increase participation in discussions and take more initiative in independent tasks.",
    75: "Focus on asking questions to deepen understanding and improve consistency in class activities.",
    70: "Work on increasing focus and taking a more active role in lessons and learning tasks.",
    65: "Aim to engage more consistently and take responsibility for independent learning.",
    60: "Develop personal organisation and focus; contribute more actively during lessons.",
    55: "Focus on staying engaged and completing tasks on time with support and guidance.",
    40: "Begin by setting small targets to complete tasks and participate more fully in lessons.",
    35: "Work on basic engagement skills, starting with short, achievable tasks and participation."
}

reading_target_bank = {
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

writing_target_bank = {
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

homework_bank = {
    90: "Maintain excellent homework habits consistently.",
    80: "Complete homework thoughtfully most of the time.",
    70: "Complete homework sometimes without full effort.",
    60: "Complete homework but without consistent effort.",
    50: "Homework not consistently completed."
}

classwork_bank = {
    90: "Engage consistently and follow instructions effectively in classwork.",
    80: "Complete classwork thoughtfully most of the time.",
    70: "Complete classwork sometimes without full effort.",
    60: "Complete classwork but without consistent effort.",
    50: "Classwork not consistently completed."
}

closer_bank = [
    "Overall, progress was evident over the course of the term.",
    "With continued support, further progress is expected next term.",
    "Confidence improved gradually as the term progressed."
]

# ---------- HELPERS ----------
def get_band(value):
    try:
        band = int(value)
        return band if band in attitude_bank else 0
    except:
        return 0

def truncate_comment(comment, max_chars=490):
    if len(comment) <= max_chars:
        return comment
    truncated = comment[:max_chars].rstrip(" ,;.")
    if "." in truncated:
        truncated = truncated[:truncated.rfind(".")+1]
    return truncated

def get_pronouns(gender):
    gender = gender.lower()
    if gender == "male":
        return "he", "his"
    elif gender == "female":
        return "she", "her"
    else:
        return "he", "his"

def lowercase_first(text):
    return text[0].lower() + text[1:] if text else ""

def strip_trailing_punct(text):
    return text.rstrip(". ,;")

def generate_comment(name, att, read, write, read_t, write_t, hw, cw, pronouns, max_chars=490):
    p, p_poss = pronouns
    opening = random.choice(opening_phrases)

    attitude_sentence = f"{opening} {name} {attitude_bank[att]}."
    reading_sentence = f"In reading, {p} {reading_bank[read]}."
    writing_sentence = f"In writing, {p} {writing_bank[write]}."
    reading_target_sentence = f"For the next term, {p} should {lowercase_first(strip_trailing_punct(reading_target_bank[read_t]))}."
    writing_target_sentence = f"Additionally, {p} should {lowercase_first(strip_trailing_punct(writing_target_bank[write_t]))}."

    homework_sentence = f"{p} should {lowercase_first(hw)}." if hw else ""
    classwork_sentence = f"{p} should {lowercase_first(cw)}." if cw else ""

    closer_sentence = closer_bank[0]

    comment = " ".join([
        attitude_sentence,
        reading_sentence,
        writing_sentence,
        reading_target_sentence,
        writing_target_sentence,
        homework_sentence,
        classwork_sentence,
        closer_sentence
    ])

    comment = truncate_comment(comment, max_chars)
    return comment, len(comment)

# =========================================
# STREAMLIT APP
# =========================================

st.title("English Report Comment Generator")

st.markdown("Fill in the student details. You can add multiple entries before downloading a combined report.")

# ---------- SESSION STATE FOR MULTIPLE STUDENTS ----------
if 'entries' not in st.session_state:
    st.session_state.entries = []

# ---------- FORM ----------
with st.form("report_form"):
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    att = st.selectbox("Attitude band", [90,85,80,75,70,65,60,55,40])
    read = st.selectbox("Reading achievement band", [90,85,80,75,70,65,60,55,40])
    write = st.selectbox("Writing achievement band", [90,85,80,75,70,65,60,55,40])
    read_t = st.selectbox("Reading target band", [90,85,80,75,70,65,60,55,40])
    write_t = st.selectbox("Writing target band", [90,85,80,75,70,65,60,55,40])
    hw_level = st.selectbox("Homework effort level", list(homework_bank.keys()))
    cw_level = st.selectbox("Classwork effort level", list(classwork_bank.keys()))

    submitted = st.form_submit_button("Add Student Entry")

# ---------- ADD STUDENT ----------
if submitted and name:
    pronouns = get_pronouns(gender)
    comment, count = generate_comment(
        name, att, read, write, read_t, write_t,
        homework_bank[hw_level],
        classwork_bank[cw_level],
        pronouns
    )
    st.session_state.entries.append((name, comment))
    st.success(f"Entry added for {name} (total entries: {len(st.session_state.entries)})")

# ---------- DISPLAY ALL ENTRIES ----------
if st.session_state.entries:
    st.subheader("Current Entries")
    for i, (student, comment) in enumerate(st.session_state.entries, 1):
        st.markdown(f"**{i}. {student}**")
        st.text_area(f"Comment {i}", comment, height=150)

# ---------- DOWNLOAD COMBINED REPORT ----------
if st.session_state.entries:
    doc = Document()
    for student, comment in st.session_state.entries:
        doc.add_paragraph(f"{student}:\n{comment}\n")
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    st.download_button(
        label="Download Combined Word Report",
        data=buffer,
        file_name="combined_report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
