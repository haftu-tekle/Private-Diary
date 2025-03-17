from flask import Blueprint, jsonify, request
from app.database import get_db_connection

main=Blueprint('main', __name__)


@main.route('/entries', methods=['GET'])
def get_entries():
    connection=get_db_connection()
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM TABLE entries')
    row=cursor.fetchall()
    entries=[{'id':row[0],'date':row[1],'content':row[2]}]
    connection.commit()
    connection.close()

    return jsonify(entries)
