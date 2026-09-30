from flask import Flask, jsonify
import database as db

app = Flask(__name__)

@app.route('/plant/<plant_id>')
def get_plant_data(plant_id):
    match plant_id:
        case "plant_1":
            return return_json(db.readings_001, 1)
        case "plant_2":
            return return_json(db.readings_002, 2)
        case _:
            return jsonify({"error": "Invalid plant ID"}), 404
        
def return_json(database_table, plant_id):
    with db.engine.connect() as conn:
        query_moisture = database_table.select().order_by(database_table.c.date.desc()).limit(1)
        moisture = conn.execute(query_moisture).fetchone()

        query_plant = db.plants.select().where(db.plants.c.id == plant_id)
        plant = conn.execute(query_plant).fetchone()

        if moisture is None:
            return jsonify({"error": "No data found"}), 404
        elif plant is None:
            return jsonify({"error": "Plant not found"}), 404
        
        result_dict = {
            "moisture": dict(moisture._mapping),
            "plant": dict(plant._mapping),
        }
        return jsonify(result_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)