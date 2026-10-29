from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
projects = []
tasks = []

PAGE = """
<h1>Project Tool v3 - View Tasks</h1>
<a href="/tasks">View all tasks</a>

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
"""

TASKS_PAGE = """
<h1>All Tasks</h1>
<table border="1" cellpadding="6">
  <tr><th>Project</th><th>Task</th><th>Assigned to</th></tr>
  {% for t in tasks %}
  <tr><td>{{ t.project }}</td><td>{{ t.task }}</td><td>{{ t.assignee }}</td></tr>
  {% endfor %}
</table>
<br><a href="/">Back</a>
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

@app.route("/tasks")
def view_tasks():
    return render_template_string(TASKS_PAGE, tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)