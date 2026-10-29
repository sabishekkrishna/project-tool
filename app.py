from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
projects = {}

# v1 Endpoint: Create Project
@app.route('/api/project', methods=['POST'])
def add_project():
    data = request.json
    project_name = data.get('name')
    if not project_name:
        return jsonify({"error": "Project name required"}), 400
    
    projects[project_name] = []
    return jsonify({"message": f"Project '{project_name}' created successfully", "version": "v1"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)