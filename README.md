# AI Career Guidance Agent

An AI-powered Career Guidance Agent built using **Python**, **LangChain**, **Ollama**, and **Qwen2.5-7B**. It analyzes a student's existing skills, identifies skill gaps, recommends the most suitable career path, suggests portfolio projects, generates a personalized learning roadmap, and provides interview preparation tips.

---

## Features

- Skill Gap Analysis
- Career Role Recommendation
- Personalized Learning Roadmap
- Interview Preparation Tips
- Real-world Project Recommendations
- Conversation Memory
- Local LLM using Ollama
- Powered by Qwen2.5-7B

---

## Tech Stack

- Python
- LangChain
- Ollama
- Qwen2.5-7B
- VS Code

---

## Project Structure

```text
AI-Career-Guidance-Agent/
│
├── Agent.py
├── README.md
├── pyproject.toml
├── main.py
└── .gitignore
```

---

## How It Works

1. Student enters their skills or career goal.
2. AI analyzes the current skill set.
3. Missing skills are identified.
4. The best career role is recommended.
5. Three real-world portfolio projects are suggested.
6. A personalized learning roadmap is generated.
7. Interview preparation tips are provided.

---

## Example Input

```text
Student:
My skills are Python, SQL, Power BI, Pandas, and NumPy.
Which career suits me?
```

---

## Example Output

```text
Recommended Role
Data Analyst

Current Skills
• Python
• SQL
• Power BI
• Pandas
• NumPy

Missing Skills
• Statistics
• Scikit-Learn
• Machine Learning

Suggested Projects
1. Sales Forecasting Model
2. Fraud Detection System
3. Customer Churn Analysis

Learning Roadmap
1. Learn Statistics
2. Study Scikit-Learn
3. Build Machine Learning Models
4. Create Portfolio Projects
5. Deploy and Showcase Projects

Interview Preparation Tips
• Practice SQL and Python coding.
• Explain your projects clearly.
• Revise statistics and machine learning concepts.
```

---

# Screenshots

## 1. Career Recommendation

> Insert Screenshot 1 here

![Career Recommendation](images/career_recommendation.png)

---

## 2. AI Engineer Skill Gap Analysis

> Insert Screenshot 2 here

![Skill Gap Analysis](images/skill_gap_analysis.png)

---

## 3. Project Recommendations

> Insert Screenshot 3 here

![Project Suggestions](images/project_recommendations.png)

---

## Future Improvements

- Streamlit Web Interface
- Resume Upload Support
- PDF Career Report Generation
- Course Recommendations
- Multi-domain Career Guidance
- User Authentication
- Chat History Export

---

## Run the Project

```bash
ollama serve
```

```bash
ollama pull qwen2.5:7b
```

```bash
python Agent.py
```

---

## Author

**Pramodha Reddy**

GitHub: https://github.com/Pramodhaprogrammer

---

## License

This project is developed for learning, portfolio, and educational purposes.
