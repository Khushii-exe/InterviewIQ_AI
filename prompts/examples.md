# EXAMPLE INTERVIEW EVALUATION

This section contains examples that demonstrate the expected reasoning process and output style.

The examples are only references.

Do NOT copy their content.

Follow the same evaluation style.

======================================================

## EXAMPLE 1

Transcript

Interviewer:
Tell me about yourself.

Candidate:
Good morning.
Thank you for giving me this opportunity.
I am Khushi Singh, currently pursuing B.Tech in Computer Science.
I enjoy Machine Learning because I love solving real-world problems.

------------------------------------------------------

Expected Evaluation

The interviewer asked a single introductory question.

The candidate gave a relevant answer.

The greeting should NOT be treated as a separate answer.

The introduction is complete.

The communication is clear.

The tone is professional.

------------------------------------------------------

Expected JSON

{
  "question_number":1,

  "question":"Tell me about yourself.",

  "answer_summary":"Candidate introduced academic background, interests and career goal.",

  "scores":{

      "technical_correctness":9,

      "clarity":9,

      "completeness":9,

      "confidence":8,

      "professionalism":10

  },

  "strengths":[

      "Well structured introduction",

      "Professional greeting",

      "Clear motivation"

  ],

  "improvements":[

      "Mention one measurable achievement."

  ],

  "feedback":"Strong self introduction with good communication."
}

======================================================

## EXAMPLE 2

Transcript

Interviewer:
Interesting.

Why Machine Learning?

Can you explain why you chose this field?

Candidate:

I enjoy solving practical problems.

I also enjoy mathematics.

Recently I started learning Deep Learning.

------------------------------------------------------

Expected Evaluation

The interviewer asked one logical question.

Although spoken in multiple sentences,
the interviewer intent is

Why Machine Learning?

Merge them into ONE question.

------------------------------------------------------

Expected JSON

{
    "question_number":2,

    "question":"Why did you choose Machine Learning?",

    "answer_summary":"Candidate explained motivation towards ML using practical problem solving and mathematics.",

    "scores":{

        "technical_correctness":8,

        "clarity":9,

        "completeness":8,

        "confidence":8,

        "professionalism":9

    },

    "strengths":[

        "Clear motivation",

        "Relevant explanation"

    ],

    "improvements":[

        "Mention long-term career vision."

    ],

    "feedback":"Good answer with genuine interest. More concrete examples would strengthen it."
}

======================================================

Important Observations

✓ Greetings are NOT interview questions.
✓ Follow-up questions may belong to one logical question.
✓ Ignore acknowledgements such as:

"Okay"
"Hmm"
"Right"
"I see"

unless they contain meaningful interviewer intent.

✓ Do NOT split candidate answers unnecessarily.
✓ Prefer semantic understanding over punctuation.