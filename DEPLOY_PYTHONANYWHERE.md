# Deploying to PythonAnywhere

This project is already pre-configured to deploy seamlessly on PythonAnywhere. Follow these steps to host your portfolio site.

---

### Step 1: Upload your code to PythonAnywhere
The easiest way is to use Git. 

1. Create a repository on GitHub (e.g. `portfolio`) and push your local code there.
2. Log in to your [PythonAnywhere dashboard](https://www.pythonanywhere.com/).
3. Open a **Bash Console** and clone the repository:
   ```bash
   git clone https://github.com/your-github-username/your-repo-name.git portfolio
   ```
   *(Note: This creates the folder at `/home/yourusername/portfolio`)*

---

### Step 2: Create a Virtual Environment & Install Dependencies
Still in the Bash Console, run:
```bash
cd portfolio
mkvirtualenv --python=python3.10 portfolio-venv
pip install -r requirements.txt
```
*(If `mkvirtualenv` is not available, you can use `python3 -m venv portfolio-venv` and activate it manually via `source portfolio-venv/bin/activate`)*

---

### Step 3: Initialize the Database
Initialize your SQLite database and the default admin user:
```bash
export FLASK_APP=app.py
flask init-db
```
This will output:
`Database initialized. Login with username 'admin' and password 'admin123'.`

---

### Step 4: Configure the Web App
1. Go to the **Web** tab in PythonAnywhere.
2. Click **Add a new web app**.
3. Choose **Manual Configuration** (Do NOT choose Flask directly, manual configuration is much cleaner).
4. Select **Python 3.10** (matching your virtual environment version).
5. Set the paths under the **Code** section:
   - **Source code**: `/home/yourusername/portfolio`
   - **Working directory**: `/home/yourusername/portfolio`
6. Under the **Virtualenv** section:
   - Enter your virtual environment path: `/home/yourusername/.virtualenvs/portfolio-venv` *(or the custom path if you used venv)*

---

### Step 5: Configure the WSGI File
1. Under the **Code** section of the Web tab, click the link for your **WSGI configuration file** (e.g., `/var/www/yourusername_pythonanywhere_com_wsgi.py`).
2. Delete **everything** currently in that file.
3. Paste the contents of `pythonanywhere_wsgi.py` from this project:
   ```python
   import sys

   # Set this to the path where you uploaded the project
   project_home = '/home/yourusername/portfolio'

   if project_home not in sys.path:
       sys.path.insert(0, project_home)

   # Import the Flask app object as "application"
   from app import app as application
   ```
4. **Make sure to change `yourusername` in the path to match your actual PythonAnywhere username!**
5. Save the file.

---

### Step 6: Map Static Files (Highly Recommended)
Serving CSS, JavaScript, and user-uploaded media files directly via the web server makes the site load much faster.
In the **Web** tab, scroll down to the **Static files** section and add the following mapping:

| URL | Directory |
| --- | --- |
| `/static/` | `/home/yourusername/portfolio/static` |

---

### Step 7: Reload & Test
Go to the top of the **Web** tab and click the green **Reload** button. 
Your portfolio is now live at:
`https://yourusername.pythonanywhere.com/`

**Don't forget to:**
1. Navigate to `https://yourusername.pythonanywhere.com/admin/login`
2. Log in using `admin` / `admin123`.
3. Go to **Account** and change the default password immediately.
