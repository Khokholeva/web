import flask
from data import db_session, __all_models
from flask import jsonify, request

User = __all_models.users.User
Jobs = __all_models.jobs.Jobs

blueprint = flask.Blueprint('news_api', __name__,
                            template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'job', 'work_size',
                                    'start_date', 'end_date',
                                    'collaborators',  'is_finished',
                                    'team_leader', 'leader.name', 'leader.surname'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'news': job.to_dict(only=('id', 'job', 'work_size', 'is_finished', 'leader.name'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['job', 'work_size', 'team_leader', 'is_finished', 'collaborators']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    job = Jobs(
        job=request.json['job'],
        work_size=request.json['work_size'],
        team_leader=request.json['team_leader'],
        is_finished=request.json['is_finished'],
        collaborators=request.json['collaborators']
    )
    session.add(job)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_news(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    session.delete(job)
    session.commit()
    return jsonify({'success': 'OK'})
