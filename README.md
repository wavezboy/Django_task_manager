# Django_task_manager

# # Step 1: Install virtualenv

# Open a new terminal or command prompt and run the following command to install virtualenv using pip:

# pip install virtualenv

# Step 2: Verify Installation

# After the installation is complete, you can verify that virtualenv is installed by running:

#

# virtualenv --version

# If the installation was successful, this command should display the version number of virtualenv.

# Step 3: Create a Virtual Environment

# Now, you can create a virtual environment in your project directory. Navigate to your project directory using the terminal:

# cd path\to\your\project

# Then, create a virtual environment:

# virtualenv myprojectenv

# Step 4: Activate the Virtual Environment

# On Windows, activate the virtual environment by running:

# .\myprojectenv\Scripts\activate

# After activation, you should see the virtual environment name in your terminal prompt.

# Create a new Django project

django-admin startproject task_manager_project

# Navigate into the project directory

cd task_manager_project

# Create a new Django app

python manage.py startapp task_manager_app

<!-- Step 3: Configure Database Settings -->

In your project's settings.py file, configure the database settings. By default, SQLite is used, but you can use other databases like PostgreSQL, MySQL, or others.

# task_manager_project/settings.py

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / "db.sqlite3",
}
}
