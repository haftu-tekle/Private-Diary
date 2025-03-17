from flask import Blueprint, jsonify, request
from app.database import get_db_connection
from datetime import datetime

main=Blueprint('main', __name__)

@main.route('/entries', methods=['GET'])
def get_entry():
    connection=get_db_connection()
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM TABLE entries')
    entries=[{'id':row[0],'date':row[1],'content':row[2] } for row in cursor.fetchall() ]
    connection.close()
    return jsonify(entries)

@main.route('/entries', methods=['POST'])
def add_entry():
    connection=get_db_connection()
    cursor=connection.cursor()
    data=request.get_json()
    date=data.get('date')
    content=data.get('content')
    if not content:
        return jsonify({'error': 'This field should be filled'})


    if not date:
        date=datetime.now().strftime('%Y-%m-%d')
    cursor.execute('INSERT INTO (entries) VALUES (?,?)', (date, content))
    connection.commit()
    return jsonify('The Journal has been added succesfully')