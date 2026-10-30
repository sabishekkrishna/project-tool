from datetime import datetime
from flask import Flask, request, redirect, flash, render_template_string

app = Flask(__name__)
app.secret_key = "project-tool-secret"

VERSION = "v1"
projects = []

HEAD = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Project Tool {{ version }}</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',Roboto,Arial,sans-serif;background:#f1f5f9;color:#1e293b;min-height:100vh}
.navbar{background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;padding:18px 32px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 10px rgba(0,0,0,.15)}
.navbar h1{font-size:22px;font-weight:600}
.navbar .right{display:flex;align-items:center;gap:18px}
.navbar a{color:#fff;text-decoration:none;font-size:15px;opacity:.9}
.navbar a:hover{opacity:1;text-decoration:underline}
.badge{background:rgba(255,255,255,.22);padding:4px 14px;border-radius:20px;font-size:13px;font-weight:600}
.container{max-width:900px;margin:30px auto;padding:0 20px}
.card{background:#fff;border-radius:12px;padding:24px;margin-bottom:24px;box-shadow:0 1px 4px rgba(0,0,0,.08)}
.card h2{font-size:18px;margin-bottom:16px;color:#4f46e5}
form{display:flex;gap:10px;flex-wrap:wrap}
input,select{flex:1;min-width:160px;padding:11px 14px;border:1px solid #cbd5e1;border-radius:8px;font-size:15px;background:#fff}
input:focus,select:focus{outline:none;border-color:#4f46e5;box-shadow:0 0 0 3px rgba(79,70,229,.15)}
button{background:#4f46e5;color:#fff;border:0;padding:11px 22px;border-radius:8px;font-size:15px;font-weight:600;cursor:pointer}
button:hover{background:#4338ca}
.list{list-style:none}
.list li{padding:13px 4px;border-bottom:1px solid #e2e8f0;display:flex;justify-content:space-between;align-items:center;gap:10px}
.list li:last-child{border-bottom:0}
.muted{color:#94a3b8;font-size:13px}
.empty{color:#94a3b8;text-align:center;padding:24px 0}
.flash{background:#dcfce7;color:#166534;padding:12px 16px;border-radius:8px;margin-bottom:20px;border:1px solid #bbf7d0}
.tag{background:#e0e7ff;color:#4338ca;padding:3px 12px;border-radius:12px;font-size:13px;font-weight:600}
.stats{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-bottom:24px}
.stat{background:#fff;border-radius:12px;padding:20px;text-align:center;box-shadow:0 1px 4px rgba(0,0,0,.08)}
.stat .num{font-size:32px;font-weight:700;color:#4f46e5}
.stat .lbl{color:#64748b;font-size:14px;margin-top:4px}
table{width:100%;border-collapse:collapse}
th{background:#eef2ff;color:#4f46e5;text-align:left;padding:12px;font-size:14px}
td{padding:12px;border-bottom:1px solid #e2e8f0;font-size:15px}
tr:hover td{background:#f8fafc}
</style>
</head>
<body>
<div class="navbar">
  <h1>📋 Project Tool</h1>
  <div class="right"><span class="badge">{{ version }}</span></div>
</div>
<div class="container">
{% with msgs = get_flashed_messages() %}{% for m in msgs %}<div class="flash">✔ {{ m }}</div>{% endfor %}{% endwith %}
"""

PAGE = """
<div class="card">
  <h2>➕ Create New Project</h2>
  <form method="post" action="/project">
    <input name="name" placeholder="Enter project name" required maxlength="60">
    <button type="submit">Create Project</button>
  </form>
</div>

<div class="card">
  <h2>📁 Projects ({{ projects|length }})</h2>
  {% if projects %}
  <ul class="list">
    {% for p in projects %}
    <li><span><strong>{{ loop.index }}.</strong> {{ p.name }}</span><span class="muted">{{ p.created }}</span></li>
    {% endfor %}
  </ul>
  {% else %}
  <div class="empty">No projects yet. Create your first project above.</div>
  {% endif %}
</div>
</div>
</body>
</html>
"""

def page(template, **ctx):
    return render_template_string(HEAD + template, version=VERSION, **ctx)

@app.route("/")
def home():
    return page(PAGE, projects=projects)

@app.route("/project", methods=["POST"])
def add_project():
    name = request.form["name"].strip()
    if name:
        projects.append({"name": name, "created": datetime.now().strftime("%d %b %Y, %I:%M %p")})
        flash(f'Project "{name}" created successfully')
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)