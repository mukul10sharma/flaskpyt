from flask import Flask, jsonify

app = Flask(__name__)

books_db = [
    {
        'name':'Secret',
        'price':260 
    },
    {
        'name':'Deep work',
        'price':354
    }
]

# retrive all the books
@app.route('/')
def home():
    return jsonify({'message':'welcome'})

def on():
    return jsonify({'state':'1'})

@app.route('/off')
def off():
    return jsonify({'state':'0'})
    
#retrive one book
app.run(port=5500)

#create a book

 