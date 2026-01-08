# =========================================
# ENGLISH REPORT COMMENT GENERATOR - STATEMENTS BANKS
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

# ---------- ACHIEVEMENT BANKS ----------
attitude_bank = {
    90: [
        "approached learning with enthusiasm and confidence, showing independence and curiosity",
        "demonstrated exceptional engagement and curiosity in class activities",
        "showed outstanding motivation and independence in learning tasks"
    ],
    85: [
        "demonstrated a highly positive and motivated attitude towards learning",
        "was consistently enthusiastic and focused in class activities",
        "showed great initiative and interest in learning"
    ],
    80: [
        "showed a positive and motivated attitude towards learning and participated confidently",
        "engaged well with activities and demonstrated steady motivation",
        "was attentive and showed consistent effort in learning"
    ],
    75: [
        "showed consistent effort and engaged well in class activities",
        "participated reliably and focused on learning tasks",
        "worked steadily and responded positively to guidance"
    ],
    70: [
        "was generally focused and responded well to guidance",
        "showed attention in class and followed instructions",
        "needed some prompting but generally engaged"
    ],
    65: [
        "showed a steady approach to learning but benefited from encouragement",
        "engaged with support and responded to guidance",
        "participated in class with some encouragement"
    ],
    60: [
        "required support to remain focused and engaged in lessons",
        "needed guidance to stay on task and participate",
        "benefited from encouragement and reminders to focus"
    ],
    55: [
        "needed regular guidance to remain engaged and confident",
        "struggled to maintain focus without support",
        "required frequent encouragement to participate"
    ],
    40: [
        "found it challenging to stay focused and required consistent encouragement",
        "required significant prompting to engage in activities",
        "found it difficult to maintain concentration without support"
    ],
    0: [
        "required significant support to engage confidently in learning",
        "struggled to participate without continuous assistance",
        "was unable to engage effectively without guidance"
    ]
}

reading_bank = {
    90: [
        "understood texts and made insightful interpretations",
        "demonstrated deep comprehension and interpretation skills",
        "interpreted texts confidently with clear understanding"
    ],
    85: [
        "understood texts confidently and made strong interpretations",
        "showed good comprehension and understanding of main ideas",
        "interpreted texts with confidence and clarity"
    ],
    80: [
        "understood texts confidently and interpreted key points",
        "demonstrated secure comprehension of texts",
        "grasped key ideas and meaning from texts"
    ],
    75: [
        "understood texts securely and identified key ideas",
        "showed understanding of main points with some guidance",
        "identified main ideas in reading passages"
    ],
    70: [
        "understood main ideas in texts with some support",
        "required occasional help to grasp key points",
        "showed basic understanding of texts"
    ],
    65: [
        "identified key points in texts with guidance",
        "needed support to extract main ideas",
        "understood some information with help"
    ],
    60: [
        "showed basic understanding of texts with support",
        "needed help to comprehend texts",
        "required guidance to understand passages"
    ],
    55: [
        "understood simple information in texts",
        "showed limited comprehension",
        "needed support to grasp basic points"
    ],
    40: [
        "understood texts with support",
        "required guidance to follow reading materials",
        "needed assistance to extract information"
    ],
    0: [
        "recognised familiar words but needed significant support to understand texts",
        "could identify some words but comprehension was limited",
        "required continuous support to understand texts"
    ]
}

writing_bank = {
    90: [
        "expressed ideas clearly using varied vocabulary and sentence structures",
        "wrote with excellent clarity and creativity",
        "produced structured and sophisticated writing"
    ],
    85: [
        "wrote confidently using varied sentences and well-chosen vocabulary",
        "demonstrated strong clarity and vocabulary in writing",
        "expressed ideas effectively with some creativity"
    ],
    80: [
        "wrote structured pieces with appropriate vocabulary",
        "organized ideas clearly in writing",
        "used suitable sentences and vocabulary in tasks"
    ],
    75: [
        "wrote organised paragraphs with suitable vocabulary",
        "structured writing appropriately",
        "showed clarity in writing paragraphs"
    ],
    70: [
        "wrote clear sentences and simple paragraphs",
        "constructed understandable sentences and short paragraphs",
        "showed basic organisation in writing"
    ],
    65: [
        "wrote simple sentences with some organisation",
        "produced basic sentences with guidance",
        "used simple sentences in writing"
    ],
    60: [
        "wrote short sentences with support",
        "needed help to write complete sentences",
        "produced simple sentence-level writing"
    ],
    55: [
        "structured simple written responses",
        "needed support to organise writing",
        "showed limited sentence structure"
    ],
    40: [
        "expressed ideas with support",
        "required help to form sentences",
        "struggled to write independently"
    ],
    0: [
        "required significant support to form sentences in writing",
        "needed continuous guidance to write",
        "was unable to produce independent writing"
    ]
}

reading_target_bank = {
    90: [
        "explore subtler inferences and interpret multiple perspectives to deepen analysis",
        "extend critical reading skills by examining alternative interpretations",
        "focus on nuanced analysis and identifying underlying meanings"
    ],
    85: [
        "extend inference skills and examine alternative interpretations",
        "practice deeper analysis of text and multiple viewpoints",
        "work on interpreting texts in more detail"
    ],
    80: [
        "focus on recognising subtler implications and supporting ideas with evidence",
        "analyse texts with attention to subtle meaning",
        "work on understanding nuances and implications"
    ],
    75: [
        "practice identifying hidden meanings and making connections within the text",
        "focus on interpreting underlying ideas",
        "analyse text to understand key themes"
    ],
    70: [
        "work on identifying implied ideas and summarising main points",
        "practice finding main ideas with some guidance",
        "focus on extracting meaning and summarising text"
    ],
    65: [
        "focus on reading for meaning and noting key details",
        "work on comprehension with guidance",
        "practice identifying key points"
    ],
    60: [
        "strengthen comprehension by paraphrasing and asking questions about the text",
        "focus on understanding meaning with support",
        "re-read texts and clarify understanding"
    ],
    55: [
        "build vocabulary and re-read to clarify meaning",
        "practice comprehension strategies",
        "work on reading fluency with support"
    ],
    40: [
        "identify key events and main points with guided support",
        "practice basic understanding of events",
        "work with support to follow the story"
    ],
    35: [
        "begin with guided reading and discussion to identify basic ideas",
        "focus on basic comprehension skills",
        "work on initial understanding of texts"
    ]
}

writing_target_bank = {
    90: [
        "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
        "refine descriptive writing with multiple perspectives",
        "develop sophisticated narrative techniques"
    ],
    85: [
        "refine vocabulary and explore more varied sentence structures for impact",
        "improve sentence variety and descriptive clarity",
        "focus on stylistic improvement and impact"
    ],
    80: [
        "focus on precise sensory words and 'showing' character emotions",
        "work on using vivid vocabulary and sensory detail",
        "enhance writing by showing rather than telling"
    ],
    75: [
        "add more sensory details and actions that reveal character traits",
        "practice descriptive writing with clear character portrayal",
        "use actions and details to enhance stories"
    ],
    70: [
        "replace 'telling' statements with descriptive or action-based sentences",
        "focus on describing rather than explaining",
        "use actions to show character traits"
    ],
    65: [
        "include adjectives, vivid verbs, and sensory details to enhance imagery",
        "add descriptive words and actions to improve writing",
        "practice imagery in sentences"
    ],
    60: [
        "focus on including at least one sensory detail per paragraph",
        "practice adding descriptive details in writing",
        "use sensory detail to enrich sentences"
    ],
    55: [
        "use sentence starters and story maps to add detail",
        "work on structuring sentences for clarity",
        "practice using guidance to improve writing"
    ],
    40: [
        "begin with simple sentences describing events and character feelings",
        "practice basic sentence writing",
        "start with describing actions simply"
    ],
    35: [
        "start by sequencing events and describing one action per sentence",
        "work on ordering sentences and simple description",
        "practice writing simple event sequences"
    ]
}

closer_bank = [
    "Overall, progress was evident over the course of the term",
    "With continued support, further progress is expected next term",
    "Confidence improved gradually as the term progressed"
]
