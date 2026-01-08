# statements.py
# This file contains ONLY text banks (no logic)

import random

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
    90: [
        "approached learning with enthusiasm and confidence, showing independence and curiosity",
        "demonstrated exceptional curiosity and independence in learning"
    ],
    85: [
        "demonstrated a highly positive and motivated attitude towards learning",
        "showed strong motivation and a positive approach to class tasks"
    ],
    80: [
        "showed a positive and motivated attitude towards learning and participated confidently",
        "participated confidently and maintained a positive attitude in class"
    ],
    75: [
        "showed consistent effort and engaged well in class activities",
        "worked steadily and contributed positively to lessons"
    ],
    70: [
        "was generally focused and responded well to guidance",
        "followed instructions and maintained focus with some support"
    ],
    65: [
        "showed a steady approach to learning but benefited from encouragement",
        "needed occasional guidance to stay on track"
    ],
    60: [
        "required support to remain focused and engaged in lessons",
        "needed help to stay engaged and attentive during activities"
    ],
    55: [
        "needed regular guidance to remain engaged and confident",
        "benefited from reminders to stay on task"
    ],
    40: [
        "found it challenging to stay focused and required consistent encouragement",
        "needed frequent support to maintain engagement"
    ],
    0: [
        "required significant support to engage confidently in learning",
        "struggled to participate without constant guidance"
    ]
}

reading_bank = {
    90: [
        "understood texts and made insightful interpretations",
        "demonstrated excellent understanding of texts with insightful analysis"
    ],
    85: [
        "understood texts confidently and made strong interpretations",
        "showed clear comprehension and strong interpretation skills"
    ],
    80: [
        "understood texts confidently and interpreted key points",
        "identified main ideas and supported interpretations effectively"
    ],
    75: [
        "understood texts securely and identified key ideas",
        "recognised key points in texts accurately"
    ],
    70: [
        "understood main ideas in texts with some support",
        "followed the main ideas and needed occasional guidance"
    ],
    65: [
        "identified key points in texts with guidance",
        "required support to pick out important information"
    ],
    60: [
        "showed basic understanding of texts with support",
        "understood simple ideas when prompted"
    ],
    55: [
        "understood simple information in texts",
        "needed help to understand short passages"
    ],
    40: [
        "understood texts with support",
        "required guidance to comprehend texts"
    ],
    0: [
        "recognised familiar words but needed significant support to understand texts",
        "needed one-on-one help to read and understand texts"
    ]
}

writing_bank = {
    90: [
        "expressed ideas clearly using varied vocabulary and sentence structures",
        "wrote with clarity and creativity, using rich vocabulary"
    ],
    85: [
        "wrote confidently using varied sentences and well-chosen vocabulary",
        "produced structured writing with good sentence variety"
    ],
    80: [
        "wrote structured pieces with appropriate vocabulary",
        "used clear sentences to express ideas effectively"
    ],
    75: [
        "wrote organised paragraphs with suitable vocabulary",
        "showed logical structure in writing with adequate vocabulary"
    ],
    70: [
        "wrote clear sentences and simple paragraphs",
        "expressed ideas in straightforward sentences"
    ],
    65: [
        "wrote simple sentences with some organisation",
        "needed support to structure basic sentences"
    ],
    60: [
        "wrote short sentences with support",
        "required guidance to form complete sentences"
    ],
    55: [
        "structured simple written responses",
        "needed help to organise ideas in writing"
    ],
    40: [
        "expressed ideas with support",
        "relied on teacher support to write clearly"
    ],
    0: [
        "required significant support to form sentences in writing",
        "struggled to write without constant assistance"
    ]
}

reading_target_bank = {
    90: [
        "explore subtler inferences and interpret multiple perspectives to deepen analysis",
        "analyse texts more deeply and explore alternative interpretations"
    ],
    85: [
        "extend inference skills and examine alternative interpretations",
        "practice considering different perspectives in reading"
    ],
    80: [
        "focus on recognising subtler implications and supporting ideas with evidence",
        "refine skills in identifying hidden meanings and backing up ideas"
    ],
    75: [
        "practice identifying hidden meanings and making connections within the text",
        "work on connecting key ideas across texts"
    ],
    70: [
        "work on identifying implied ideas and summarising main points",
        "develop summarising skills and spotting implied meaning"
    ],
    65: [
        "focus on reading for meaning and noting key details",
        "practice picking out essential information"
    ],
    60: [
        "strengthen comprehension by paraphrasing and asking questions about the text",
        "re-read and paraphrase to enhance understanding"
    ],
    55: [
        "build vocabulary and re-read to clarify meaning",
        "focus on key vocabulary and rereading strategies"
    ],
    40: [
        "identify key events and main points with guided support",
        "use prompts to locate main points in texts"
    ],
    35: [
        "begin with guided reading and discussion to identify basic ideas",
        "work on understanding simple texts with help"
    ]
}

writing_target_bank = {
    90: [
        "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
        "explore different narrative perspectives and creative language use"
    ],
    85: [
        "refine vocabulary and explore more varied sentence structures for impact",
        "practice richer vocabulary and sentence variety for effect"
    ],
    80: [
        "focus on precise sensory words and 'showing' character emotions",
        "develop descriptive writing and show character feelings"
    ],
    75: [
        "add more sensory details and actions that reveal character traits",
        "practice including actions and descriptions to develop characters"
    ],
    70: [
        "replace 'telling' statements with descriptive or action-based sentences",
        "work on showing rather than telling in writing"
    ],
    65: [
        "include adjectives, vivid verbs, and sensory details to enhance imagery",
        "focus on enriching sentences with descriptive words and actions"
    ],
    60: [
        "focus on including at least one sensory detail per paragraph",
        "practice adding details to support clarity in writing"
    ],
    55: [
        "use sentence starters and story maps to add detail",
        "organise ideas using structured writing aids"
    ],
    40: [
        "begin with simple sentences describing events and character feelings",
        "write short sentences with basic description"
    ],
    35: [
        "start by sequencing events and describing one action per sentence",
        "practice ordering events
