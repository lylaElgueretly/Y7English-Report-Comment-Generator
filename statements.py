# =========================================
# STATEMENTS.PY
# This file contains ONLY text banks (no logic)
# All phrases now have 2-3 variations per band for randomization
# =========================================

# ---------- OPENING PHRASES ----------
opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,",
    "In this term,",
    "Over the past term,"
]

# ---------- ATTITUDE BANK ----------
attitude_bank = {
    90: [
        "demonstrated exceptional engagement and curiosity in class activities",
        "approached learning with enthusiasm and confidence, showing independence and curiosity",
        "consistently engaged in learning with a positive and motivated attitude"
    ],
    85: [
        "demonstrated a highly positive and motivated attitude towards learning",
        "showed strong motivation and eagerness in class activities",
        "participated confidently and maintained a positive learning approach"
    ],
    80: [
        "showed a positive and motivated attitude towards learning and participated confidently",
        "engaged in learning with enthusiasm and contributed actively",
        "maintained good focus and motivation in lessons"
    ],
    75: [
        "showed consistent effort and engaged well in class activities",
        "completed tasks reliably and participated in lessons",
        "applied effort and contributed to class discussions"
    ],
    70: [
        "was generally focused and responded well to guidance",
        "maintained focus with occasional support from the teacher",
        "followed instructions well and showed steady engagement"
    ],
    65: [
        "showed a steady approach to learning but benefited from encouragement",
        "engaged in tasks with support and guidance",
        "needed occasional prompting to stay on task"
    ],
    60: [
        "required support to remain focused and engaged in lessons",
        "needed help to maintain attention and participation",
        "benefited from guidance to complete tasks"
    ],
    55: [
        "needed regular guidance to remain engaged and confident",
        "showed limited independence and required frequent support",
        "relied on teacher support to complete activities"
    ],
    40: [
        "found it challenging to stay focused and required consistent encouragement",
        "struggled to engage and needed regular reminders",
        "required ongoing guidance to participate effectively"
    ],
    0: [
        "required significant support to engage confidently in learning",
        "needed constant assistance to participate in lessons",
        "was unable to complete tasks without teacher help"
    ]
}

# ---------- READING BANK ----------
reading_bank = {
    90: [
        "demonstrated deep comprehension and interpretation skills",
        "understood texts and made insightful interpretations",
        "analysed texts thoroughly and drew sophisticated conclusions"
    ],
    85: [
        "understood texts confidently and made strong interpretations",
        "showed secure comprehension and reasoning",
        "interpreted texts well and supported ideas with evidence"
    ],
    80: [
        "understood texts confidently and interpreted key points",
        "identified main ideas and supported interpretations",
        "read texts carefully and drew appropriate conclusions"
    ],
    75: [
        "understood texts securely and identified key ideas",
        "grasped main points and basic details in texts",
        "demonstrated comprehension of essential ideas"
    ],
    70: [
        "understood main ideas in texts with some support",
        "identified basic content with teacher guidance",
        "followed text meaning with occasional prompting"
    ],
    65: [
        "identified key points in texts with guidance",
        "needed support to extract main ideas",
        "relied on teacher help to understand texts"
    ],
    60: [
        "showed basic understanding of texts with support",
        "recognised simple ideas but required help",
        "needed guidance to comprehend main points"
    ],
    55: [
        "understood simple information in texts",
        "followed basic content with teacher assistance",
        "needed prompting to grasp text meaning"
    ],
    40: [
        "understood texts with support",
        "required teacher guidance to comprehend simple texts",
        "needed help to identify basic ideas"
    ],
    0: [
        "recognised familiar words but needed significant support to understand texts",
        "struggled to comprehend texts even with guidance",
        "was unable to interpret text meaning without help"
    ]
}

# ---------- WRITING BANK ----------
writing_bank = {
    90: [
        "expressed ideas clearly using varied vocabulary and sentence structures",
        "wrote with excellent clarity and creativity",
        "produced sophisticated writing with precision and style"
    ],
    85: [
        "wrote confidently using varied sentences and well-chosen vocabulary",
        "demonstrated clear organisation and vocabulary choice",
        "produced structured and coherent writing pieces"
    ],
    80: [
        "wrote structured pieces with appropriate vocabulary",
        "organised writing logically and used suitable words",
        "expressed ideas clearly with sound sentence structure"
    ],
    75: [
        "wrote organised paragraphs with suitable vocabulary",
        "demonstrated clear paragraphing and language use",
        "expressed ideas in well-structured sentences"
    ],
    70: [
        "wrote clear sentences and simple paragraphs",
        "produced basic writing with understandable sentences",
        "conveyed ideas using simple structured paragraphs"
    ],
    65: [
        "wrote simple sentences with some organisation",
        "expressed ideas in basic sentences with limited structure",
        "needed guidance to organise sentences effectively"
    ],
    60: [
        "wrote short sentences with support",
        "produced brief writing with teacher assistance",
        "needed help to structure basic sentences"
    ],
    55: [
        "structured simple written responses",
        "wrote very simple sentences with minimal organisation",
        "required guidance to produce coherent writing"
    ],
    40: [
        "expressed ideas with support",
        "needed help to form understandable sentences",
        "relied on teacher support for basic writing"
    ],
    0: [
        "required significant support to form sentences in writing",
        "was unable to produce written ideas independently",
        "needed constant assistance to write simple sentences"
    ]
}

# ---------- READING TARGET BANK ----------
reading_target_bank = {
    90: [
        "explore subtler inferences and interpret multiple perspectives to deepen analysis",
        "analyse texts for nuanced meanings and multiple viewpoints",
        "develop further critical thinking through text interpretation"
    ],
    85: [
        "extend inference skills and examine alternative interpretations",
        "focus on deeper understanding and perspectives",
        "practice supporting interpretations with evidence"
    ],
    80: [
        "focus on recognising subtler implications and supporting ideas with evidence",
        "develop inference and reasoning skills",
        "work on identifying key implications in texts"
    ],
    75: [
        "practice identifying hidden meanings and making connections within the text",
        "focus on comprehension and linking ideas",
        "work on understanding implied meanings in texts"
    ],
    70: [
        "work on identifying implied ideas and summarising main points",
        "develop summarising and recognition skills",
        "focus on main ideas and supporting details"
    ],
    65: [
        "focus on reading for meaning and noting key details",
        "practice extracting important information",
        "work on understanding basic text ideas"
    ],
    60: [
        "strengthen comprehension by paraphrasing and asking questions about the text",
        "work on clarifying meaning through questioning",
        "practice restating ideas in your own words"
    ],
    55: [
        "build vocabulary and re-read to clarify meaning",
        "develop basic comprehension skills",
        "focus on recognising simple ideas in texts"
    ],
    40: [
        "identify key events and main points with guided support",
        "practice finding main ideas with help",
        "work on recognising events and basic points"
    ],
    35: [
        "begin with guided reading and discussion to identify basic ideas",
        "start reading with teacher support to understand content",
        "work on identifying simple concepts with guidance"
    ]
}

# ---------- WRITING TARGET BANK ----------
writing_target_bank = {
    90: [
        "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
        "develop nuanced narrative techniques and complex sentence structures",
        "explore advanced writing effects for clarity and impact"
    ],
    85: [
        "refine vocabulary and explore more varied sentence structures for impact",
        "practice using precise vocabulary and varied sentences",
        "improve expression through sentence variety and word choice"
    ],
    80: [
        "focus on precise sensory words and 'showing' character emotions",
        "practice describing characters with sensory detail",
        "develop writing that conveys feelings through actions and words"
    ],
    75: [
        "add more sensory details and actions that reveal character traits",
        "include descriptive actions to develop characters",
        "focus on showing rather than telling in writing"
    ],
    70: [
        "replace 'telling' statements with descriptive or action-based sentences",
        "practice converting statements into descriptive writing",
        "develop clarity through action-based sentences"
    ],
    65: [
        "include adjectives, vivid verbs, and sensory details to enhance imagery",
        "focus on enriching sentences with descriptive words",
        "develop detailed and vivid writing techniques"
    ],
    60: [
        "focus on including at least one sensory detail per paragraph",
        "practice adding description to basic writing",
        "work on enhancing writing clarity with sensory words"
    ],
    55: [
        "use sentence starters and story maps to add detail",
        "practice structuring writing with planning tools",
        "develop organised paragraphs using prompts"
    ],
    40: [
        "begin with simple sentences describing events and character feelings",
        "practice basic descriptive writing",
        "work on writing sentences with clarity"
    ],
    35: [
        "start by sequencing events and describing one action per sentence",
        "practice ordering events and simple description",
        "work on writing clear step-by-step narratives"
    ]
}

# ---------- CLOSER BANK ----------
closer_bank = [
    "Overall, progress was evident over the course of the term",
    "With continued support, further progress is expected next term",
    "Confidence improved gradually as the term progressed"
]
