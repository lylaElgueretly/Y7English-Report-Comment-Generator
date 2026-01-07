# =========================================
# ENGLISH REPORT COMMENT GENERATOR - Streamlit Version
# Fixed: Preserve edits on "Add Another Comment"
# =========================================

import random
import streamlit as st
from docx import Document

TARGET_CHARS = 499  # target character count including spaces

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
attitude_bank = {90:"approached learning with enthusiasm and confidence, showing independence and curiosity",
85:"demonstrated a highly positive and motivated attitude towards learning",
80:"showed a positive and motivated attitude towards learning and participated confidently",
75:"showed consistent effort and engaged well in class activities",
70:"was generally focused and responded well to guidance",
65:"showed a steady approach to learning but benefited from encouragement",
60:"required support to remain focused and engaged in lessons",
55:"needed regular guidance to remain engaged and confident",
40:"found it challenging to stay focused and required consistent encouragement",
0:"required significant support to engage confidently in learning"}

reading_bank = {90:"understood texts and made insightful interpretations",
85:"understood texts confidently and made strong interpretations",
80:"understood texts confidently and interpreted key points",
75:"understood texts securely and identified key ideas",
70:"understood main ideas in texts with some support",
65:"identified key points in texts with guidance",
60:"showed basic understanding of texts with support",
55:"understood simple information in texts",
40:"understood texts with support",
0:"recognised familiar words but needed significant support to understand texts"}

writing_bank = {90:"expressed ideas clearly using varied vocabulary and sentence structures",
85:"wrote confidently using varied sentences and well-chosen vocabulary",
80:"wrote structured pieces with appropriate vocabulary",
75:"wrote organised paragraphs with suitable vocabulary",
70:"wrote clear sentences and simple paragraphs",
65:"wrote simple sentences with some organisation",
60:"wrote short sentences with support",
55:"structured simple written responses",
40:"expressed ideas with support",
0:"required significant support to form sentences in writing"}

reading_target_bank = {90:"explore subtler inferences and interpret multiple perspectives to deepen analysis",
85:"extend inference skills and examine alternative interpretations",
80:"focus on recognising subtler implications and supporting ideas with evidence",
75:"practice identifying hidden meanings and making connections within the text",
70:"work on identifying implied ideas and summarising main points",
65:"focus on reading for meaning and noting key details",
60:"strengthen comprehension by paraphrasing and asking questions about the text",
55:"build vocabulary and re-read to clarify meaning",
40:"identify key events and main points with guided support",
35:"begin with guided reading and discussion to identify basic ideas"}

writing_target_bank = {90:"experiment with subtle suspense, varied perspectives, and advanced sensory effects",
85:"refine vocabulary and explore more varied sentence structures for impact",
80:"focus on precise sensory words and 'showing' character emotions",
75:"add more sensory details and actions that reveal character traits",
70:"replace 'telling' statements with descriptive or action-based sentences",
65:"include adjectives, vivid verbs, and sensory details to enhance imagery",
60:"focus on including at least one sensory detail per paragraph",
55:"use sentence starters and story maps to add detail",
40:"begin with simple sentences describing events and character feelings",
35:"start by sequencing events and describing one action per sentence"}

closer_bank = [
    "Overall, progress was evident over the course of the term.",
    "With continued support, further progress is expected next term.",
    "Confidence improved gradually as the term progressed."
]

# ---------- HELPERS ----------
def get_pronouns(gender):
    gender = gender.lower()
    if gender == "male": return "he","his"
    if gender == "female": return "she","her"
    return "they","their"

def lowercase_first(text):
    return text[0].lower() + text[1:] if text else ""

def truncate_comment(comment, target=TARGET_CHARS):
    if len(comment)<=target:
        return comment
    truncated = comment[:target].rstrip(" ,;.")
    if "." in truncated:
        truncated = truncated[:truncated.rfind(".")+1]
    return truncated

def generate_comment(name, att, read, write, read_t, write_t, pronouns, attitude_target=None):
    p,p_poss = pronouns
    opening = random.choice(opening_phrases)
    attitude_sentence = f"{opening} {name} {attitude_bank[att]}."
    reading_sentence = f"In reading, {p} {reading_bank[read]}."
    writing_sentence = f"In writing, {p} {writing_bank[write]}."
    reading_target_sentence = f"For the next term, {p} should {lowercase_first(reading_target_bank[read_t])}."
    writing_target_sentence = f"In addition, {p} should {lowercase_first(writing_target_bank[write_t])}."
    attitude_target_sentence = f" {lowercase_first(attitude_target)}" if attitude_target else ""
    closer_sentence = random.choice(closer_bank)
    comment_parts = [attitude_sentence+attitude_target_sentence,reading_sentence,writing_sentence,reading_target_sentence,writing_target_sentence,closer_sentence]
    comment = " ".join(comment_parts)
    comment = truncate_comment(comment,TARGET_CHARS)
    return comment

# ---------- STREAMLIT APP ----------
st.title("English Report Comment Generator (~499 chars)")
st.markdown("Fill in student details, generate comments, edit, add multiple students, and download report.")

if 'all_comments' not in st.session_state: st.session_state['all_comments']=[]
if 'current_comment' not in st.session_state: st.session_state['current_comment']=''

with st.form("report_form"):
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male","Female"])
    att = st.selectbox("Attitude band",[90,85,80,75,70,65,60,55,40])
    read = st.selectbox("Reading achievement band",[90,85,80,75,70,65,60,55,40])
    write = st.selectbox("Writing achievement band",[90,85,80,75,70,65,60,55,40])
    read_t = st.selectbox("Reading target band",[90,85,80,75,70,65,60,55,40])
    write_t = st.selectbox("Writing target band",[90,85,80,75,70,65,60,55,40])
    attitude_target = st.text_input("Optional Attitude Next Steps")
    submitted = st.form_submit_button("Generate Comment")

if submitted and name:
    pronouns=get_pronouns(gender)
    st.session_state['current_comment']=generate_comment(name,att,read,write,read_t,write_t,pronouns,attitude_target)

edited_comment=st.text_area("Generated Comment (editable)",st.session_state['current_comment'],height=200)
st.write(f"Character count (including spaces): {len(edited_comment)} / {TARGET_CHARS}")

# Save edits back to session state
st.session_state['current_comment']=edited_comment

if st.button("Add Another Comment") and edited_comment:
    st.session_state['all_comments'].append(f"{name}: {st.session_state['current_comment']}")
    st.session_state['current_comment']=''
    st.experimental_rerun()

# ---------- DOWNLOAD FULL REPORT ----------
if st.session_state['all_comments']:
    if st.button("Download Full Report (Word)"):
        doc=Document()
        for c in st.session_state['all_comments']:
            doc.add_paragraph(c)
        file_name="English_Report_Comments.docx"
        doc.save(file_name)
        with open(file_name,"rb") as f:
            st.download_button(label="Download Word File",data=f,file_name=file_name,mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

# ---------- SHOW ALL COMMENTS SO FAR ----------
if st.session_state['all_comments']:
    st.markdown("### All Generated Comments:")
    for idx,c in enumerate(st.session_state['all_comments'],start=1):
        st.write(f"**{idx}.** {c}")
