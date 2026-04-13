from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Your Name</h1>
    <p>Data-driven optimization & modeling</p>

    <h2>Projects</h2>
    <ul>
        <li>AI Learning System</li>
        <li>Scheduling Optimization</li>
    </ul>

    <h2>Research</h2>
    <p>Neural Networks & Risk Modeling</p>
    """

if __name__ == "__main__":
    app.run(debug=True)