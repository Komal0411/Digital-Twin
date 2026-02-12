from flask import Flask, render_template, request
import pandas as pd
import pickle
import json
import plotly.express as px
from plotly.utils import PlotlyJSONEncoder
from config import get_connection

app = Flask(__name__)

# ---------------- UTILITIES ---------------- #

def load_model(name):
    return pickle.load(open(f"models/{name}", "rb"))

def align_features(df, features):
    for col in features:
        if col not in df.columns:
            df[col] = 0
    return df[features]

def bar_chart(title, value):
    fig = px.bar(
        x=[title],
        y=[value],
        text=[value]
    )
    fig.update_layout(
        template="plotly_dark",
        height=350,
        yaxis_range=[0, 100],
        title=title
    )
    return json.dumps(fig, cls=PlotlyJSONEncoder)

# ---------------- HOME ---------------- #

@app.route("/")
def index():
    return render_template("index.html")

# ---------------- ACADEMIC ---------------- #

@app.route("/academic", methods=["GET", "POST"])
def academic():
    conn = get_connection()

    if request.method == "POST":
     conn.cursor().execute(
        """INSERT INTO Academic
        (Subject, Hours_Studied, Attendance, Internal_Score, Exam_Score)
        VALUES (?,?,?,?,?)""",
        request.form["subject"],
        float(request.form["hours"]),
        float(request.form["attendance"]),
        float(request.form["internal"]),
        float(request.form["score"])
    )
    conn.commit()

    df = pd.read_sql("SELECT * FROM Academic", conn)

    if not df.empty:
     model = load_model("academic_model.pkl")
     features = ["Hours_Studied", "Attendance", "Internal_Score", "Exam_Score"]

     latest = df.tail(1)[features]
     predicted_score = round(model.predict(latest)[0], 2)
     graphJSON = bar_chart("Predicted Academic Score", predicted_score)


    recommendations = [
            "Increase study consistency",
            "Improve attendance",
            "Focus on internal assessments"
        ]

    return render_template(
        "academic.html",
        graphJSON=graphJSON,
        predicted_score=predicted_score,
        recommendations=recommendations
    )

# ---------------- WELLNESS ---------------- #

@app.route("/wellness", methods=["GET", "POST"])
def wellness():
    conn = get_connection()

    if request.method == "POST":
        conn.cursor().execute(
            "INSERT INTO Wellness (Sleep_Hours, Exercise_Hours, Mood, Stress_Level, Wellness_Index) VALUES (?,?,?,?,?)",
            float(request.form["sleep"]),
            float(request.form["exercise"]),
            int(request.form["mood"]),
            float(request.form["stress"]),
            float(request.form["wellness_index"])
        )
        conn.commit()

    df = pd.read_sql("SELECT * FROM Wellness", conn)

    predicted_score = graphJSON = None
    recommendations = []

    if not df.empty:
        model = load_model("wellness_model.pkl")
        features = ["Sleep_Hours", "Exercise_Hours", "Mood", "Stress_Level"]

        latest = df.tail(1)[features]
        predicted_score = round(model.predict(latest)[0], 2)
        graphJSON = bar_chart("Predicted Wellness Index", predicted_score)

        recommendations = [
            "Maintain 7–8 hours sleep",
            "Increase physical activity",
            "Manage stress effectively"
        ]

    return render_template(
        "wellness.html",
        graphJSON=graphJSON,
        predicted_score=predicted_score,
        recommendations=recommendations
    )

# ---------------- CAREER ---------------- #

@app.route("/career", methods=["GET", "POST"])
def career():
    conn = get_connection()

    if request.method == "POST":
        conn.cursor().execute(
            "INSERT INTO Career (Skill, Skills, Experience, Projects, Projects_Completed, Job_Applications, Performance_Score) VALUES (?,?,?,?,?,?,?)",
            request.form["skill"],
            int(request.form["skills"]),
            int(request.form["experience"]),
            int(request.form["projects"]),
            int(request.form["projects_completed"]),
            int(request.form["jobs"]),
            float(request.form["performance"])
        )
        conn.commit()

    df = pd.read_sql("SELECT * FROM Career", conn)

    predicted_score = graphJSON = None
    recommendations = []

    if not df.empty:
        model = load_model("career_model.pkl")
        features = ["Skills", "Experience", "Projects"]

        latest = df.tail(1)
        X = align_features(latest, features)

        predicted_score = round(model.predict(X)[0], 2)
        graphJSON = bar_chart("Predicted Career Performance", predicted_score)

        recommendations = [
            "Complete more real-world projects",
            "Improve practical experience",
            "Apply consistently for roles"
        ]

    return render_template(
        "career.html",
        graphJSON=graphJSON,
        predicted_score=predicted_score,
        recommendations=recommendations
    )

# ---------------- BEHAVIOR ---------------- #

@app.route("/behavior", methods=["GET", "POST"])
def behavior():
    conn = get_connection()

    if request.method == "POST":
        conn.cursor().execute(
            "INSERT INTO Behavior (Productivity_Score, Social_Interactions, Habits, Emotional_Score) VALUES (?,?,?,?)",
            float(request.form["productivity"]),
            int(request.form["social"]),
            int(request.form["habits"]),
            float(request.form["emotional"])
        )
        conn.commit()

    df = pd.read_sql("SELECT * FROM Behavior", conn)

    predicted_score = graphJSON = None
    recommendations = []

    if not df.empty:
        model = load_model("behavior_model.pkl")
        features = ["Focus", "Consistency", "Motivation"]

        latest = df.tail(1)
        X = align_features(latest, features)

        predicted_score = round(model.predict(X)[0], 2)
        graphJSON = bar_chart("Predicted Emotional Score", predicted_score)

        recommendations = [
            "Improve daily focus routines",
            "Maintain consistency",
            "Strengthen positive habits"
        ]

    return render_template(
        "behavior.html",
        graphJSON=graphJSON,
        predicted_score=predicted_score,
        recommendations=recommendations
    )

# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(debug=True)
