from flask import Flask, render_template, request

app = Flask(__name__)

issues = [
    {'id': 1, 'description': 'Broken light ', 'assigned_staff': None},
    {'id': 2, 'description': 'Leaky pipe in the toilet', 'assigned_staff': None},
    {'id': 3, 'description': 'Broken door', 'assigned_staff': None}
]

staff = [
    "John Smith",
    "Abhishek Naidoo",
    "Chris Johnson",

]


@app.route('/', methods=['GET', 'POST'])
def assign_staff():
    if request.method == 'POST':

        issue_id = int(request.form.get('issue_id'))
        staff_name = request.form.get('staff_name')

        for issue in issues:
            if issue['id'] == issue_id:
                issue['assigned_staff'] = staff_name
                break

    return render_template('assign_staff.html', issues=issues)


if __name__ == '__main__':
    app.run(debug=True)
