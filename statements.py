# =========================================
# STATEMENTS BANK FOR ENGLISH REPORT GENERATOR
# =========================================

# Each statement now has 3 variations (lists) for controlled cycling

opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,",
    "In this term,",
    "Over the past term,"
]

attitude_bank = {
    90: [
        "approached learning with enthusiasm and confidence, showing independence and curiosity",
        "demonstrated exceptional engagement and curiosity in class activities",
        "showed remarkable enthusiasm and initiative throughout the term"
    ],
    85: [
        "demonstrated a highly positive and motivated attitude towards learning",
        "was consistently motivated and engaged in class activities",
        "showed strong commitment and eagerness to learn"
    ],
    80: [
        "showed a positive and motivated attitude towards learning and participated confidently",
        "engaged well in learning tasks with confidence",
        "demonstrated good motivation and involvement in class"
    ],
    75: [
        "showed consistent effort and engaged well in class activities",
        "participated steadily and followed instructions effectively",
        "worked consistently and maintained focus in lessons"
    ],
    70: [
        "was generally focused and responded well to guidance",
        "needed occasional support to stay focused but participated",
        "followed instructions and engaged with teacher guidance"
    ],
    65: [
        "showed a steady approach to learning but benefited from encouragement",
        "required some prompting to remain engaged in activities",
        "approached tasks with care, needing guidance at times"
    ],
    60: [
        "required support to remain focused and engaged in lessons",
        "needed regular encouragement to participate in tasks",
        "struggled to maintain focus without support"
    ],
    55: [
        "needed regular guidance to remain engaged and confident",
        "relied on teacher guidance to stay on task",
        "required frequent support to maintain confidence and engagement"
    ],
    40: [
        "found it challenging to stay focused and required consistent encouragement",
        "struggled to remain engaged and needed regular prompting",
        "found activities difficult without sustained support"
    ],
    0: [
        "required significant support to engage confidently in learning",
        "needed constant assistance to participate in lessons",
        "was unable to engage independently without help"
    ]
}

reading_bank = {
    90: [
        "understood texts and made insightful interpretations",
        "demonstrated deep comprehension and interpretation skills",
        "analysed texts confidently and drew nuanced conclusions"
    ],
    85: [
        "understood texts confidently and made strong interpretations",
        "read with confidence and drew meaningful conclusions",
        "interpreted texts accurately and with understanding"
    ],
    80: [
        "understood texts confidently and interpreted key points",
        "identified main ideas and explained them clearly",
        "showed understanding of texts and key messages"
    ],
    75: [
        "understood texts securely and identified key ideas",
        "recognised main points and details in texts",
        "demonstrated solid comprehension of reading passages"
    ],
    70: [
        "understood main ideas in texts with some support",
        "followed texts and identified central ideas with guidance",
        "showed understanding of key ideas with occasional help"
    ],
    65: [
        "identified key points in texts with guidance",
        "needed prompts to recognise important information",
        "showed partial understanding when supported"
    ],
    60: [
        "showed basic understanding of texts with support",
        "required assistance to comprehend reading material",
        "understood simple passages with help"
    ],
    55: [
        "understood simple information in texts",
        "could follow basic text information with guidance",
        "needed support to grasp content in readings"
    ],
    40: [
        "understood texts with support",
        "relied on teacher prompts to make sense of texts",
        "showed limited comprehension and required guidance"
    ],
    0: [
        "recognised familiar words but needed significant support to understand texts",
        "needed constant help to make sense of reading",
        "was unable to understand texts without support"
    ]
}

writing_bank = {
    90: [
        "expressed ideas clearly using varied vocabulary and sentence structures",
        "wrote with excellent clarity and creativity",
        "demonstrated sophisticated writing skills with strong expression"
    ],
    85: [
        "wrote confidently using varied sentences and well-chosen vocabulary",
        "produced structured and fluent written work",
        "used a range of sentences and vocabulary effectively"
    ],
    80: [
        "wrote structured pieces with appropriate vocabulary",
        "organised writing with clear sentences",
        "demonstrated competent writing skills with suitable vocabulary"
    ],
    75: [
        "wrote organised paragraphs with suitable vocabulary",
        "structured paragraphs clearly and coherently",
        "showed ability to organise ideas in writing"
    ],
    70: [
        "wrote clear sentences and simple paragraphs",
        "expressed ideas in simple, understandable sentences",
        "produced straightforward written work with clarity"
    ],
    65: [
        "wrote simple sentences with some organisation",
        "structured basic sentences but needed improvement",
        "showed emerging organisation in writing"
    ],
    60: [
        "wrote short sentences with support",
        "needed guidance to form coherent sentences",
        "produced brief written responses with help"
    ],
    55: [
        "structured simple written responses",
        "required prompts to write basic sentences",
        "relied on assistance to produce understandable writing"
    ],
    40: [
        "expressed ideas with support",
        "needed help to convey ideas in writing",
        "showed very basic writing ability with teacher help"
    ],
    0: [
        "required significant support to form sentences in writing",
        "was unable to write independently without help",
        "needed constant support to communicate ideas in writing"
    ]
}

reading_target_bank = {
    90: [
        "explore subtler inferences and interpret multiple perspectives to deepen analysis",
        "focus on analysing texts more critically and insightfully",
        "extend comprehension to include nuanced interpretation of texts"
    ],
    85: [
        "extend inference skills and examine alternative interpretations",
        "develop ability to consider multiple perspectives",
        "practice deeper analysis of reading material"
    ],
    80: [
        "focus on recognising subtler implications and supporting ideas with evidence",
        "work on identifying implied ideas and supporting them",
        "improve skills in noticing hidden meanings in texts"
    ],
    75: [
        "practice identifying hidden meanings and making connections within the text",
        "strengthen ability to find underlying ideas in passages",
        "connect textual ideas to broader meaning"
    ],
    70: [
        "work on identifying implied ideas and summarising main points",
        "develop skill in summarising key points accurately",
        "focus on understanding implied ideas in texts"
    ],
    65: [
        "focus on reading for meaning and noting key details",
        "improve comprehension and note important information",
        "practice understanding key points with support"
    ],
    60: [
        "strengthen comprehension by paraphrasing and asking questions about the text",
        "re-read texts and clarify meaning",
        "practice summarising and questioning for understanding"
    ],
    55: [
        "build vocabulary and re-read to clarify meaning",
        "focus on understanding words and phrases",
        "use re-reading to improve comprehension"
    ],
    40: [
        "identify key events and main points with guided support",
        "follow simple events and details with guidance",
        "practice basic comprehension with help"
    ],
    35: [
        "begin with guided reading and discussion to identify basic ideas",
        "start with teacher-led reading tasks",
        "identify main points with teacher support"
    ]
}

writing_target_bank = {
    90: [
        "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
        "enhance writing with creative techniques and sophisticated style",
        "develop more complex and expressive writing skills"
    ],
    85: [
        "refine vocabulary and explore more varied sentence structures for impact",
        "practice richer vocabulary and sentence variation",
        "improve sentence variety and word choice for effect"
    ],
    80: [
        "focus on precise sensory words and 'showing' character emotions",
        "develop descriptive skills in writing",
        "practice using sensory details to enhance writing"
    ],
    75: [
        "add more sensory details and actions that reveal character traits",
        "practice showing rather than telling in writing",
        "use descriptive actions to convey character traits"
    ],
    70: [
        "replace 'telling' statements with descriptive or action-based sentences",
        "focus on adding detail to sentences",
        "improve clarity by describing actions and events"
    ],
    65: [
        "include adjectives, vivid verbs, and sensory details to enhance imagery",
        "practice using descriptive language effectively",
        "enhance imagery through adjectives and action verbs"
    ],
    60: [
        "focus on including at least one sensory detail per paragraph",
        "practice adding descriptive details consistently",
        "develop ability to enrich sentences with sensory words"
    ],
    55: [
        "use sentence starters and story maps to add detail",
        "plan sentences with guidance to improve structure",
        "practice organising writing with prompts"
    ],
    40: [
        "begin with simple sentences describing events and character feelings",
        "write short descriptive sentences",
        "practice basic narrative writing"
    ],
    35: [
        "start by sequencing events and describing one action per sentence",
        "focus on ordering sentences logically",
        "practice simple story sequencing"
    ]
}

closer_bank = [
    "Overall, progress was evident over the course of the term",
    "With continued support, further progress is expected next term",
    "Confidence improved gradually as the term progressed"
]
