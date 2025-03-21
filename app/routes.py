from flask import Blueprint, request, jsonify
from app.database import get_db_connection
from datetime import datetime
main=Blueprint('main', __name__)


#Making the paths

@main.route('/entries', methods=['POST'])
def add_entry():
    DATA=request.get_json()
    date=DATA.get('date')
    content=DATA.get('content')
    
    if not content:
        return jsonify({'error':'This must be field'})
    if not date:
        date=datetime.now().strftime('%Y-%m-%d')
    connection=get_db_connection()
    cursor=connection.cursor()
    

    cursor.execute('INSERT INTO entries (date, content) VALUES (?, ?)', (date, content))
    connection.commit()
    connection.close()
    return jsonify('The journal has been added successfully')
    

@main.route('/entries', methods=['GET'])
def get_entry():
    connection=get_db_connection()
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM entries')
    entries=[{'id':row[0], 'date':row[1], 'content':row[2]}for row in cursor.fetchall()]
    connection.close()
    return jsonify(entries)

@main.route('/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):  
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM entries WHERE id = ?', (entry_id,)) 
    connection.commit()  
    connection.close()
    return jsonify({'message': f'Entry with ID {entry_id} has been deleted'}), 200

    

if __name__=='__main__':
    main.run()


