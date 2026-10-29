from flask import Flask, request, render_template_string
app = Flask(__name__)
projects = []

PAGE = """
<h1>Project Tool v1 - Add Project</h1>
<form method="post">
  <input name="name" placeholder="Project name" required>
  <button>Create Project</button>
</form>
<ul>{% for p in projects %}<li>{{ p }}</li>{% endfor %}</ul>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        projects.append(request.form["name"])
    return render_template_string(PAGE, projects=projects)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)