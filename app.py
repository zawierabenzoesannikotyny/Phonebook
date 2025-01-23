from flask import render_template, request, redirect, url_for
from database import app, db

# Import modeli
from models import Contact

@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    if name and phone:
        new_contact = Contact(name=name, phone=phone)
        db.session.add(new_contact)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)