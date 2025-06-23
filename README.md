# 🧠 Suicidal Risk Detection

This is a full-stack web application designed to detect suicidal risk in user-submitted text. It is built using **React** and **Django**. The backend uses a trained machine learning model to analyze text and return risk predictions.

## ⚙️ Setup Instructions

1. **Install the dependencies in a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate    # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. **Create your environment file**:

Copy the `.env.example` to `.env` and provide the values:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

3. **Prepare the backend**:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

4. **Run the development server**:

```bash
python manage.py runserver
```

Once the development server is running, you can access the application in your browser at the URL shown in the terminal.

---

## 📜 License

This project is released under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it — with attribution.

---

## 👤 Author

Developed by [Francisco Jesús Montero Martínez](https://github.com/framonmar7)  
For suggestions, improvements, or collaboration, feel free to reach out.
