import sys
sys.path.insert(0, '')

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from model import load_model

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    load_model.setup()
    return render_template('index.html')

@app.route('/decompile')
def decompile():
    asm_code = request.args.get('asm_code')
    print(asm_code)
    c_output = load_model.translate_asm(asm_code)
    # c_output = c_output.replace('; ', ';\n').replace('{ ', '{\n').replace('} ', '}\n').replace('#', '\n#').replace('include<math.h> ', 'include<math.h>\n').strip()

    print(c_output)
    return jsonify(c_output)

if __name__ == '__main__':
    app.debug = True
    app.run()

