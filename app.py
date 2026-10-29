from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
projects = []
tasks = []

PAGE = """
<h1>Project Tool v2 - Add Task</h1>

<h2>Create Project</h2>
<form method="post" action="/project">
  <input name="name" placeholder="Project name" required>
  <button>Create Project</button>
</form>

<h2>Assign Task</h2>
<form method="post" action="/task">
  <select name="project">{% for p in projects %}<option>{{ p }}</option>{% endfor %}</select>
  <input name="task" placeholder="Task" required>
  <input name="assignee" placeholder="Assigned to" required>
  <button>Add Task</button>
</form>

<h3>Projects</h3>
<ul>{% for p in projects %}<li>{{ p }}</li>{% endfor %}</ul>
"""

@app.route("/")
def home():
    return render_template_string(PAGE, projects=projects)

@app.route("/project", methods=["POST"])
def add_project():
    projects.append(request.form["name"])
    return redirect("/")

@app.route("/task", methods=["POST"])
def add_task():
    tasks.append({
        "project": request.form["project"],
        "task": request.form["task"],
        "assignee": request.form["assignee"],
    })
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)