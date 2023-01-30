from flask import Flask
import utils

app = Flask(__name__)

candidates = utils.load_candidates()


@app.route('/')
def page_index():

    str_candidates = '<pre>'
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']} <br>{candidate['position']} <br>{candidate['skills']}<br><br>"
    str_candidates += '</pre>'
    return str_candidates


@app.route('/candidates/<int:id>')
def profile(id):
    candidate = candidates[id]
    str_candidates = '<pre>'
    str_candidates += f"<img src={candidate['pictures']}></img> <br><br>{candidate['name']} <br>{candidate['position']} <br>{candidate['skills']}"
    str_candidates += '</pre>'
    return str_candidates


@app.route('/skills/<skill>')
def skills(skill):
    str_candidates = '<pre>'
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill in candidate_skills:
            str_candidates += f"{candidate['name']} <br>{candidate['position']} <br>{candidate['skills']}<br><br>"
    str_candidates += '</pre>'
    return str_candidates


app.run()
