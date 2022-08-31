# PriceComparisonTool

by sambbaahh and RealkaM1

## Description
The application compares prices between specific shops and stores the information into a database.

Using a graphical user interface, the user can add products from the following shops:  

Jimms - https://www.jimms.fi  
Verkkokauppa.com - https://www.verkkokauppa.com  
Prisma - https://www.prisma.fi  
Kärkkäinen - https://www.karkkainen.com  

The app was made using Python and MySQL.


## Install and run
We created and tested the application using the following technologies:  

Python 3.10.5  
HeidiSQL 11.3.0.6295  
MariaDB 10.6  

### Python  
If your system doesn't have PIP, install it using this tutorial:  
https://www.geeksforgeeks.org/how-to-install-pip-on-windows/

After installing PIP, open the command prompt and install the following libraries using these commands:

pip install beautifulsoup4  
pip install requests  
pip install pyqt5  
pip install mysql-connector-python  
pip install matplotlib   

BeautifulSoup4 & requests are used for fetching the prices from the shops.  
PyQt5 is used for drawing the interface.  
MySQL-connector is used to access the database.  
Matplotlib is used for drawing the graph.  


### MariaDB  
Download and install MariaDB. Set the user to 'root' and the password to 'admin'.  
!! If you want to change the user or password, you need to make changes to the MySQL-codes in the 'Database.py' file. !!


### HeidiSQL  
Installing HeidiSQL is optional in the MariaDB installer. It can be used to manage the database.


## How to Use  

### How to run  

Open the command prompt and run the 'create-database' file in Python (THIS ONLY NEEDS TO BE DONE THE FIRST TIME):  
python create-database.py

This creates the database needed for the application and adds the shops. If an existing database is found, it will be dropped.

Then you can run the application by running the 'Main' file in Python:  
python Main.py

### Menu  

<img src = "https://user-images.githubusercontent.com/99816212/187749185-8e009c77-dc23-4ef6-b067-6b3c232b5479.png" width="500" height="340">

You can update the items' prices by pressing the "Refresh prices" button. It fetches the newest price for every item in the database.

### Add item  

<img src = "https://user-images.githubusercontent.com/99816212/187748695-d165f962-a8e7-4e2f-8581-fc213e5b083b.png" width="500" height="340">


### Add a new shop for existing item  

<img src = "https://user-images.githubusercontent.com/99816212/187749193-68dd240d-32cd-4df3-b043-1c5f5763d161.png" width="500" height="340">


### Overview  

<img src = "https://user-images.githubusercontent.com/99816212/187749174-b3512fd7-54ac-40db-a2f0-f9958f9a0767.png" width="500" height="340">

In the Overview window you can view data of the added items.
After choosing an item from the dropdown menu, you can see the stats and a graph of the price history by pressing the "Print data" button.
You are also able to see and visit the shops that you added to the item, or delete shops from an item.
