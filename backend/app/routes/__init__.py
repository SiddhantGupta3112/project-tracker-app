from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Project Management API is running'
    })