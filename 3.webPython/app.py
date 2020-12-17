from flask import Flask, render_template

# экземпляр класса Flask
app = Flask(__name__)

# декоратор маршрутизации 
@app.route('/')
def index_page():
    """
    функция логики страницы
    Index page
    """
    return render_template("index.html")

@app.route('/product')
def product_page():
    """
    функция логики страницы
    Product page
    """
    return render_template("product.html")

@app.route('/contact')
def contact_page():
    """
    функция логики страницы
    Contact page
    """
    return render_template("contact.html")

# конструкция запуска приложения 
if __name__ == "__main__":
    app.run(debug=True)

