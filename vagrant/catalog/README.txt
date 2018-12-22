1. Objective:
    An application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

2. How to start?
   - Install Vagrant(2.2.0) and VirtualBox(5.2.22).
   - Clone the Catalog-App.
   - Launch the Vagrant VM (vagrant up & vagrant ssh).
   - Change directory (cd /vagrant/catalog).
   - Run the database file (python database_setup.py).
   - Run the python file which contain the data for filling the database(python categories.py).
   - Run the application file (python project.py).

3. Describing files:
   - database_setup.py :
     Database file that contains 3 tables:
     1. Users(contain user id and name).
     2. Category (conatain category id and name).
     3. CategoryItem (conatain item id, name and description).

   - categories.py :
     Python file which contain the data for filling the database.

   - client_secrets.json :
     JSON file for login authorization to the website resources using third party (Google Accounts).

   - project.py:
     Apllication file.

   - template folder :
     Contains the html files.

   - static folder :
     Contains the CSS and images files.


4. Login through third party:
   Create an email in gmail and Googl+.


5. JSON pages:
   - /catalog.JSON/
