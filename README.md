## Setup Instructions
# 1. Clone the repository:
```bash
git clone https://github.com/yourusername/task_management_api.git
cd task_management_api

# 2.Creating and activating virual environment
python -m venv venv
source venv/bin/activate  

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run server
python manage.py runserver

# 5. Make migrations
python manage.py makemigrations
python manage.py migrate



