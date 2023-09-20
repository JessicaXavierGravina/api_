from flask import Flask, render_template, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parking.db'  # Configuração do SQLite em memória

db = SQLAlchemy(app)

class ParkingEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(10), nullable=False)
    entry_time = db.Column(db.TIMESTAMP(timezone=True), default=db.func.now())
    exit_time = db.Column(db.TIMESTAMP(timezone=True))
    paid = db.Column(db.Boolean, default=False)

@app.route('/')
def home():
    # plate = request.form.get('plate')
    #
    # new_entry = ParkingEntry(plate=plate)
    #
    # try:
    #     db.session.add(new_entry)
    #     db.session.commit()
    #     return jsonify({'id': new_entry.id}), 201
    # except Exception as e:
    #     db.session.rollback()
    #     return jsonify({'error': str(e)}), 500

    return render_template("registros_entrada.html") #, plate=plate)


app.config['PROPAGATE_EXCEPTIONS'] = True  # Propagar exceções para uma resposta HTTP detalhada
app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()
