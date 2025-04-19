# 🧑‍💼 Employee Training Tracker

A backend-powered Django application to manage employees, training programs, and enrollments. Designed to streamline internal training workflows for HR/admin teams.

---

## 🔧 Features

- 📋 **Employee Management** — Add and manage employee records with department tags  
- 🎓 **Training Programs** — Create and list various training programs  
- 🔁 **Enrollments** — Assign programs to employees with training status tracking  
- 🧠 **Filtering** — Filter enrollments by status or department for better insights  
- 🛠️ **Admin Panel** — Full Django admin access for quick backend control  
- 🌑 **Styled UI** — Clean dark theme using a modern color palette (optional)

---

## ⚙️ Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default) — can switch to PostgreSQL/MySQL
- **Frontend:** Django templates with Bootstrap & custom CSS

---

## 🚀 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/your-username/employee-training-tracker.git
cd employee-training-tracker
```

2. **Create virtual environment & activate**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations & create superuser**

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. **Run the server**

```bash
python manage.py runserver
```

Now visit:  
🌐 [`http://127.0.0.1:8000`](http://127.0.0.1:8000) — App  
🔐 [`http://127.0.0.1:8000/admin`](http://127.0.0.1:8000/admin) — Admin

---

## 👷 Developer

**Kshitij Kotecha**  
Built with backend-first mindset, minimal UI, and clarity in logic.

---