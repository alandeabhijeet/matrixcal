from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def step1():
    if request.method == 'POST':
        num_matrices = int(request.form['num_matrices'])
        return render_template('step2.html', num_matrices=num_matrices)
    return render_template('step1.html')

@app.route('/step2', methods=['POST'])
def step2():
    num_matrices = int(request.form['num_matrices'])
    matrices = []
    
    for i in range(num_matrices):
        rows = int(request.form[f'rows_{i}'])
        cols = int(request.form[f'cols_{i}'])
        matrix = []
        
        for r in range(rows):
            row = [int(request.form.get(f'matrix_{i}_{r}_{c}', 0)) for c in range(cols)]
            matrix.append(row)
        
        matrices.append(np.array(matrix))
    
    operation = request.form['operation']
    result = ""
    
    if num_matrices == 1:
        matrix = matrices[0]
        if operation == 'det':
            result = f"Determinant: {np.linalg.det(matrix)}"
        elif operation == 'rank':
            result = f"Rank: {np.linalg.matrix_rank(matrix)}"
    elif num_matrices == 2:
        matrix1, matrix2 = matrices
        if operation == 'add':
            result = f"Addition Result:\n{matrix1 + matrix2}"
        elif operation == 'subtract':
            result = f"Subtraction Result:\n{matrix1 - matrix2}"
        elif operation == 'multiply':
            result = f"Multiplication Result:\n{np.dot(matrix1, matrix2)}"
    
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
