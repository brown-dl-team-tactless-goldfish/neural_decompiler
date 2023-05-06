import sys
import os
import random
sys.path.insert(0, '')

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from model import load_model

app = Flask(__name__)
CORS(app)

random_asm_folder = 'data/random_asm'

@app.route('/')
def index():
    global random_asm_files

    random_asm_files = os.listdir(random_asm_folder)
    load_model.setup()

    return render_template('index.html')

@app.route('/decompile', methods = ['POST'])
def decompile():
    # asm_code = request.args.get('asm_code')
    asm_code = request.get_json()
    print('ASM: ', asm_code)

    try:
        c_output = load_model.translate_asm(asm_code)
    except Exception as e:
        print(e)
        return str(e), 400

    # need better cleaning script
    c_output = c_output.replace('<START>', '').replace('<STOP>', '').strip()
    print('C: ', c_output)

    return jsonify(c_output)

@app.route('/randomize')
def randomize():
    file_name = random.choice(random_asm_files)

    with open(f'{random_asm_folder}/{file_name}') as f:
        random_asm = f.read()

    print('done randomizing - selected', file_name)
    return jsonify(random_asm)


if __name__ == '__main__':
    app.debug = True
    app.run()

