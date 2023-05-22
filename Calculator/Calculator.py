from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])

def calculate():
    expression = request.form['expression']
    result = subprocess.check_output(['python', 'calculator.py', expression])
    return jsonify({'result': result.decode('utf-8').strip('\n')})

if __name__ == '__main__':
    app.run()

# function to calculate SGPA
def calculate_sgpa(points, credit_points):
    total_credit_points = sum(credit_points)
    weighted_sum = sum([points[i] * credit_points[i] for i in range(len(points))])
    sgpa = weighted_sum / total_credit_points
    return sgpa

# function to calculate CGPA
def calculate_cgpa(sgpa_list):
    total_sgpa = sum(sgpa_list)
    cgpa = total_sgpa / len(sgpa_list)
    return cgpa

# example usage
points = [8, 8, 8, 8, 8, 9, 9, 9]  # list of grades obtained in each subject
credit_points = [3, 3, 3, 3, 3, 3, 3, 2]  # list of corresponding credit points of each subject
sgpa = calculate_sgpa(points, credit_points)
print("SGPA:", round(sgpa, 2))

sgpa_list = [8.98, 8.97, 9.02, 9.04, 7.48, 8.35]  # list of SGPA obtained in each semester
cgpa = calculate_cgpa(sgpa_list)
print("CGPA:", round(cgpa, 2))
