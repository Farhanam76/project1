from flask import Flask, render_template, url_for, send_from_directory, redirect, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy

from form import Checkout, Payment

app = Flask(__name__)
# cart = []
app.config['SECRET_KEY'] ='547de724e07da73af3b7ec37cb0d0221'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Holiday5@localhost:3306/bookstore"

db = SQLAlchemy(app)

class Books(db.Model):
    ISBN = db.Column(db.BIGINT, primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(30), nullable = False)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    firstname = db.Column(db.String(50), nullable = False)
    lastname = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50))
    book = db.relationship('Books', backref='bookbr')


display = [{ 'title':' The bookish nook',
            'bio':" ' A book can make you visit the same world twice but now with a different perspective'",
            'content' : "Step into a world of literary wonders at 'The Bookish Nook.' Where every page holds a new adventure, and every corner is filled with the magic of words. Discover your next favorite story in the warmth of our cozy nook, where books come to life and readers find their sanctuary."

}]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', display=display)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title = 'Contact us')

@app.route("/products", methods= ['GET'])
def products():
    books = Books.query.all()
    return render_template('products.html', title ='Products listing', books = books) 
    # serialized_books = [{"name": book.name, "author": book.author} for book in books]
    # return serialized_books
    
@app.route("/category")
def category():
    return render_template('category.html', title= 'Category')


@app.route("/cart")
def cart():
    
    return render_template('cart.html', title = 'Cart',)




@app.route("/checkout", methods=['GET', 'POST'])
def checkout():
    
    form = Checkout()
    if form.validate_on_submit():  
        new_customer = Customer(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data
            
        )
        
        db.session.add(new_customer)
        db.session.commit()
       
        return redirect(url_for('payment'))
   
    return render_template('checkout.html', title =' Checking out', form=form)


@app.route("/payment")
def payment():
    form = Payment()
    return render_template('payment.html', title = 'Payment method', form=form)

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

@app.route("/products/book1")
def book1():
    books = Books.query.all()
    book1 = next((book for book in books if book.name == "All the Light We Cannot See"), None)
    return render_template('book1.html', title = 'book1', book=book1)
@app.route("/products/book2")
def book2():
    return render_template('book2.html', title = 'book2')
@app.route("/products/book3")
def book3():
    return render_template('book3.html', title = 'book3')
@app.route("/products/book4")
def book4():
    return render_template('book4.html', title = 'book4')
@app.route("/products/book5")
def book5():
    return render_template('book5.html', title = 'book5')
@app.route("/products/book6")
def book6():
    return render_template('book6.html', title = 'book6')
@app.route("/products/book7")
def book7():
    return render_template('book7.html', title = 'book7')
@app.route("/products/book8")
def book8():
    return render_template('book8.html', title = 'book8')
@app.route("/products/book9")
def book9():
    return render_template('book9.html', title = 'book9')
@app.route("/products/book10")
def book10():
    return render_template('book10.html', title = 'book10')


if __name__ == '__main__':
    with app.app_context():
       
        db.create_all()
    
    
    app.run(debug=True)

