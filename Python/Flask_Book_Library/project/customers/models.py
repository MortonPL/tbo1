from project import db, app
import re


# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, name, city, age):
        if not re.match("[\\w.,'-]+", name):
            raise ValueError("Customer name can only contain alphanumeric characters, dot, coma, apostrophe and hyphen.")
        if not name or len(name) > 64:
            raise ValueError("Customer name must be between 1 and 64 characters long.")

        if not re.match("[\\w.,'-]+", city):
            raise ValueError("City name can only contain alphanumeric characters, dot, coma, apostrophe and hyphen.")
        if not city or len(city) > 64:
            raise ValueError("City name must be between 1 and 64 characters long.")

        self.name = name
        self.city = city
        self.age = age

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age})"


with app.app_context():
    db.create_all()
