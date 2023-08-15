# /src/api/routes.py
from flask import Blueprint, request, jsonify
from ..services import weather_service

bp = Blueprint('api', __name__)

@bp.route('/weather', methods=['POST'])
def collect_weather_data():
    user_id = request.json.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    result = weather_service.fetch_weather_data(user_id)
    return jsonify(result), 201

@bp.route('/weather/<user_id>', methods=['GET'])
def get_progress(user_id):
    progress = weather_service.calculate_progress(user_id)
    return jsonify({'progress': progress})
