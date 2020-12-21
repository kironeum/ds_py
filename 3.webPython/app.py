from flask import Flask, render_template, request
import hashlib

# экземпляр класса Flask
app = Flask(__name__)

def hashing(pwd, num_char):
    """
    Функция шифрования
    """
    # 2. кодирование
    byte_str = pwd.encode()

    # 3. шифрование
    hash_str = hashlib.sha256(byte_str)

    # 4. преобразование в строку hex-числа (шестнадцатиричного числа) 
    if num_char == '-':
        hex_str = hash_str.hexdigest()
    else:
        hex_str = hash_str.hexdigest()[:int(num_char)]
    
    return hex_str

 
# декоратор маршрутизации 
@app.route('/')
def index_page():
    """
    функция логики страницы
    Index page
    """
    return render_template("index.html")

@app.route('/product', methods=['get', 'post'])
def product_page():
    """
    функция логики страницы
    Product page
    """
    message = ''
    if request.method == 'POST':
        site_name = request.form.get('site')
        password = request.form.get('pwd')
        num_char = request.form.get('num')

        message = hashing(site_name + password, 10)

    return render_template("product.html", message=message)

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


#  СТИЛИЗОВАТЬ home PAGE 