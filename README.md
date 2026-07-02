# AI Career Guidance Agent

An AI-powered Career Guidance Agent built using **Python**, **LangChain**, **Ollama**, and **Qwen2.5**. The agent analyzes a student's skills, identifies missing skills, recommends the most suitable career path, suggests projects, generates a learning roadmap, and provides interview preparation tips.

---

## Features

- Skill Gap Analysis
- Career Role Recommendation
- Learning Roadmap Generation
- Interview Preparation Tips
- Project Recommendations
- Conversation Memory
- Runs Locally using Ollama
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

```
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

1. Student enters their skills.
2. AI analyzes existing skills.
3. Identifies missing skills.
4. Recommends the best career role.
5. Suggests exactly 3 projects.
6. Generates a learning roadmap.
7. Provides interview preparation tips.

---

## Example Input

```
Student:
My skills are Python, SQL and Power BI.
I want to become a Data Scientist.
```

---

## Example Output

```
Recommended Role:
Data Scientist

Current Skills:
- Python
- SQL
- Power BI

Missing Skills:
- Statistics
- Machine Learning
- Scikit-Learn
- Deep Learning
- Model Deployment

Suggested Projects:
1. Loan Risk Prediction
2. Customer Churn Prediction
3. Recommendation System

Learning Roadmap:
- Learn Statistics
- Learn Machine Learning
- Practice Pandas & NumPy
- Build ML Projects
- Deploy Models

Interview Tips:
- Practice SQL
- Revise Machine Learning Concepts
- Build Real-world Projects
```

---

## Screenshots

### Career Recommendation

(Add Screenshot 1 here)

### Data Scientist Roadmap

(Add Screenshot 2 here)

### Project Suggestions

(Add Screenshot 3 here)

---

## Run the Project

Install Ollama and pull the model:

```bash
ollama pull qwen2.5:7b
```

Run the project:

```bash
python Agent.py
```

---

## Future Improvements

- Streamlit Web Interface
- Resume Analyzer
- Job Recommendation
- Course Recommendation
- PDF Report Generation
- Vector Database Integration
- RAG-based Career Guidance

---

## Author

**Pramodha Reddy**

GitHub:
https://github.com/Pramodhaprogrammer
