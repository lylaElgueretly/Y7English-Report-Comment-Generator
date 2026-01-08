# statements.py
# Text banks with 3 variants each for English report comments

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
        "approached learning with enthusiasm and confidence, showing independence and curiosity",
        "demonstrated exceptional engagement and curiosity in class activities",
        "showed outstanding motivation and consistently participated with confidence"
    ],
    85: [
        "demonstrated a highly positive and motivated attitude towards learning",
        "showed consistent enthusiasm and engagement in lessons",
        "actively contributed and participated with interest and energy"
    ],
    80: [
        "showed a positive and motivated attitude towards learning and participated confidently",
        "approached lessons with interest and contributed ideas regularly",
        "demonstrated confidence and engagement in classroom activities"
    ],
    75: [
        "showed consistent effort and engaged well in class activities",
        "maintained a good attitude and worked steadily throughout the term",
        "participated regularly and approached tasks with focus"
    ],
    70: [
        "was generally focused and responded well to guidance",
        "showed a steady approach to learning with some support",
        "followed instructions and remained engaged in most activities"
    ],
    65: [
        "showed a steady approach to learning but benefited from encouragement",
        "needed occasional prompts to stay on task and engaged",
        "participated with support and maintained effort throughout lessons"
    ],
    60: [
        "required support to remain focused and engaged in lessons",
        "needed guidance to complete tasks and remain attentive",
        "showed basic engagement with teacher support"
    ],
    55: [
        "needed regular guidance to remain engaged and confident",
        "struggled to stay on task without support",
        "participated minimally and required reminders to focus"
    ],
    40: [
        "found it challenging to stay focused and required consistent encouragement",
        "needed significant prompting to engage in class activities",
        "required continual support to participate meaningfully"
    ]
}

# ---------- READING BANK ----------
reading_bank = {
    90: [
        "understood texts and made insightful interpretations",
        "demonstrated deep comprehension and interpretation skills",
        "interpreted texts critically and made sophisticated observations"
    ],
    85: [
        "understood texts confidently and made strong interpretations",
        "read fluently and interpreted key ideas accurately",
        "demonstrated sound comprehension and reasoning skills"
    ],
    80: [
        "understood texts confidently and interpreted key points",
        "read with understanding and identified main ideas",
        "made clear interpretations of texts with some detail"
    ],
    75: [
        "understood texts securely and identified key ideas",
        "read texts and extracted important information accurately",
        "showed solid comprehension and noted main points"
    ],
    70: [
        "understood main ideas in texts with some support",
        "could identify basic points in texts with guidance",
        "read for meaning and summarised key ideas with support"
    ],
    65: [
        "identified key points in texts with guidance",
        "needed prompts to understand the main ideas",
        "required teacher support to extract information"
    ],
    60: [
        "showed basic understanding of texts with support",
        "struggled to comprehend texts without guidance",
        "needed help to interpret text meaning"
    ],
    55: [
        "understood simple information in texts",
        "needed assistance to identify points in text",
        "required support to understand basic details"
    ],
    40: [
        "understood texts with support",
        "struggled to comprehend texts even with help",
        "required constant guidance to follow text meaning"
    ]
}

# ---------- WRITING BANK ----------
writing_bank = {
    90: [
        "expressed ideas clearly using varied vocabulary and sentence structures",
        "wrote with excellent clarity and creativity",
        "produced sophisticated, well-structured writing"
    ],
    85: [
        "wrote confidently using varied sentences and well-chosen vocabulary",
        "expressed ideas effectively with appropriate vocabulary",
        "produced clear and organised written work"
    ],
    80: [
        "wrote structured pieces with appropriate vocabulary",
        "used clear sentences to express ideas",
        "structured writing with some variety in sentences"
    ],
    75: [
        "wrote organised paragraphs with suitable vocabulary",
        "showed logical organisation in written work",
        "produced coherent writing with some details"
    ],
    70: [
        "wrote clear sentences and simple paragraphs",
        "used simple language to communicate ideas",
        "produced basic paragraphs with understandable sentences"
    ],
    65: [
        "wrote simple sentences with some organisation",
        "expressed ideas in basic sentences with guidance",
        "required support to organise writing"
    ],
    60: [
        "wrote short sentences with support",
        "needed help to complete written tasks",
        "produced very simple sentences with teacher guidance"
    ],
    55: [
        "structured simple written responses",
        "needed prompts to write coherently",
        "required guidance to complete writing tasks"
    ],
    40: [
        "expressed ideas with support",
        "struggled to form sentences independently",
        "required significant support to write basic ideas"
    ]
}

# ---------- READING TARGET BANK ----------
reading_target_bank = {
    90: [
        "explore subtler inferences and interpret multiple perspectives to deepen analysis",
        "develop advanced comprehension skills and analyse underlying themes",
        "engage with complex texts and make nuanced interpretations"
    ],
    85: [
        "extend inference skills and examine alternative interpretations",
        "work on analysing text meaning and recognising subtler points",
        "practice interpreting multiple angles in a text"
    ],
    80: [
        "focus on recognising subtler implications and supporting ideas with evidence",
        "analyse texts for deeper understanding and support ideas",
        "practice making connections and drawing conclusions from texts"
    ],
    75: [
        "practice identifying hidden meanings and making connections within the text",
        "develop comprehension skills by exploring implied ideas",
        "work on summarising main points with more detail"
    ],
    70: [
        "work on identifying implied ideas and summarising main points",
        "strengthen understanding by noticing patterns in texts",
        "focus on clarifying meaning and key details"
    ],
    65: [
        "focus on reading for meaning and noting key details",
        "develop comprehension by highlighting important ideas",
        "work on understanding main points with support"
    ],
    60: [
        "strengthen comprehension by paraphrasing and asking questions about the text",
        "practice summarising texts with teacher guidance",
        "work on understanding texts with prompts"
    ],
    55: [
        "build vocabulary and re-read to clarify meaning",
        "focus on extracting basic information",
        "develop reading skills with guided support"
    ],
    40: [
        "identify key events and main points with guided support",
        "work on basic understanding of events and ideas",
        "practice reading comprehension with assistance"
    ]
}

# ---------- WRITING TARGET BANK ----------
writing_target_bank = {
    90: [
        "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
        "enhance creative writing by exploring sophisticated techniques",
        "develop narrative style with advanced vocabulary and detail"
    ],
    85: [
        "refine vocabulary and explore more varied sentence structures for impact",
        "practice enhancing clarity and creative expression",
        "work on expanding sentence structures and stylistic choices"
    ],
    80: [
        "focus on precise sensory words and 'showing' character emotions",
        "add descriptive details and vary sentence types",
        "enhance clarity and expression through detail and style"
    ],
    75: [
        "add more sensory details and actions that reveal character traits",
        "practice showing character emotions through action",
        "work on enhancing imagery and expression in writing"
    ],
    70: [
        "replace 'telling' statements with descriptive or action-based sentences",
        "focus on using actions to reveal character traits",
        "practice adding descriptive elements to writing"
    ],
    65: [
        "include adjectives, vivid verbs, and sensory details to enhance imagery",
        "practice using descriptive language to develop ideas",
        "work on adding sensory details and rich vocabulary"
    ],
    60: [
        "focus on including at least one sensory detail per paragraph",
        "practice writing with added descriptive elements",
        "develop detail in sentences to enhance clarity"
    ],
    55: [
        "use sentence starters and story maps to add detail",
        "work on structuring writing with prompts",
        "practice adding clarity and detail to simple sentences"
    ],
    40: [
        "begin with simple sentences describing events and character feelings",
        "practice sequencing events and basic description",
        "focus on simple sentences and clear ideas"
    ]
}

# ---------- CLOSER BANK ----------
closer_bank = [
    "Overall, progress was evident over the course of the term",
    "With continued support, further progress is expected next term",
    "Confidence improved gradually as the term progressed"
]
