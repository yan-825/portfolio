from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>LEE PO YAN | Portfolio</title>
        <style>
            body {
                font-family: Arial;
                max-width: 900px;
                margin: auto;
                padding: 20px;
                line-height: 1.6;
            }
            img {
                width: 150px;
                border-radius: 10px;
            }
            h1 {
                margin-bottom: 5px;
            }
            h2 {
                border-bottom: 2px solid #ccc;
                padding-bottom: 5px;
            }
            .section {
                margin-top: 30px;
            }
            .card {
                margin-bottom: 20px;
            }
            a {
                display: inline-block;
                margin-top: 5px;
                padding: 5px 10px;
                background-color: #007BFF;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            a:hover {
                background-color: #0056b3;
            }
        </style>
    </head>

    <body>

        <!-- Profile -->
        <img src="https://drive.google.com/uc?export=view&id=1g1Ix06xvKmotzBHVZuB5r7ZW9pccz7GT">
        <h1>LEE PO YAN</h1>
        <p>Data-driven optimization & modeling</p>

        <!-- About -->
        <div class="section">
            <h2>About</h2>
            <p>
            Background in mathematical modeling and data analysis, with Python development experience. 
            Skilled in problem-solving, system optimization, and applying quantitative methods to real-world engineering challenges.
            A reliable and collaborative team player, adaptable to fast-paced environments, and willing to learn and support team objectives.
            </p>
        </div>

        <!-- Projects -->
        <div class="section">
            <h2>Projects</h2>

            <div class="card">
                <b>AI Learning System</b><br>
                Python-based system integrating generative AI, LINE Bot, database, speech recognition, and image processing.<br>
            </div>

        </div>

        <!-- Research -->
        <div class="section">
            <h2>Research</h2>

            <div class="card">
                <b>Conference Paper (APERA 2025)</b><br>
                Designed a Python-based AI system integrating generative AI and LINE Bot, with database integration, speech recognition, and image processing.<br>
                <a href="https://drive.google.com/file/d/1TUnp0noxOzjRhIFoQFJSdbaeMCS5T9Rt/preview" target="_blank">View Paper</a>
            </div>

            <div class="card">
                <b>SRM-Based Research (Neural Networks)</b><br>
                Research on neural network-based risk modeling and spectral risk measures.<br>
                <a href="https://drive.google.com/file/d/1Ne_iSsYGQYeXM2a0LQsWU4JB_n6M1dGG/preview" target="_blank">View Research</a>
            </div>

        </div>

        <!-- Competitions -->
        <div class="section">
            <h2>Competitions</h2>

            <div class="card">
                <b>CFA Institute Research Challenge</b><br>
                Equity research on Delta Electronics using DCF and SOTP valuation models.<br>
                <a href="https://drive.google.com/file/d/1tpNhQWzsJRKVwMkbbQ-cFeO36NxS-YGN/preview" target="_blank">View Report</a>
            </div>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()