from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2.5:1.5b")

print("AI Career Agent Ready (type exit to stop)")

history = []

while True:
    user = input("Student: ")

    if user.lower() == "exit":
        break

    # memory add manually
    history.append(f"Student: {user}")

    prompt = """
You are an expert AI Career Guidance and Skill Gap Analysis Agent.
Carefully read the student's skills and do not repeat them as missing skills.

Conversation so far:
""" + "\n".join(history) + """

For every student query:

1. Analyze current skills.
2. Identify missing skills.
3. Suggest 3 relevant projects.
4. Create a step-by-step learning roadmap.
5. Provide interview preparation tips.
6. If the student asks which career suits them, recommend the most suitable role and explain why.

Rules:
- Give concise answers.
- Do not repeat points.
- Focus on Data Science, AI, Data Analyst, Software Engineer, and Full Stack roles.
- Mention SQL, Python, Machine Learning, Statistics, Power BI, and Data Structures when relevant.
- Use bullet points.
- Do not make assumptions about skill level.
- If a skill is mentioned by the student, treat it as known.
- Prioritize Statistics, Machine Learning, Pandas, NumPy, Scikit-Learn for Data Science roles.
- Do not recommend R or MATLAB unless specifically requested.
- Never list a student's known skills as missing skills.
- If the student already knows Python, SQL, or Power BI, do not suggest learning their basics again.
- Generate only skills that are genuinely missing for the target role.
- Tailor the roadmap based on the student's existing skills.
- For Data Scientist role, focus on Statistics, Machine Learning, Pandas, NumPy, Scikit-Learn, Deep Learning, and Model Deployment.
- Suggest exactly 3 projects.
- Keep answers under 300 words.
- For Data Scientist roles, prioritize Statistics, Machine Learning, Pandas, NumPy, Scikit-Learn, Data Visualization, and Model Deployment over Data Structures and Algorithms.
- When asked about career suitability, first provide Recommended Role and Reason.
- Choose from Data Analyst, Data Scientist, AI Engineer, Software Engineer, or Full Stack Developer.
- Ignore incomplete or invalid student inputs.
- If the input is not a career-related question, ask the student to provide more details.
"""
    response = llm.invoke(prompt)

    history.append(f"AI: {response}")

    print("\nAI:\n", response)