
# main.py
from app import app

if __name__ == "__main__":
    # Development server (not for production)
    app.run(host="0.0.0.0", port=8000)
