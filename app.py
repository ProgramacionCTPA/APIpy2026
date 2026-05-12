#paquetes o librerías
from flask import Flask, render_template, redirect
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

#archivos que enlazan el backend a las vistas
from routes.movie_routes import movie_bp
from routes.auth_routes import auth_bp
from routes.cart_routes import cart_bp

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "supersecretkey_supersecretkey_123456"

jwt = JWTManager(app)

app.register_blueprint(movie_bp, url_prefix="/api/movies")
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(cart_bp, url_prefix="/api/cart")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
