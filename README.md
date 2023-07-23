# OpentableReservation

This Python script automates the process of making a reservation at a restaurant on OpenTable. It uses the Selenium library to interact with the web page, setting the party size, reservation time, and reservation date.

Features
Open OpenTable Website: Opens the OpenTable website for a specific restaurant in an incognito Chrome browser window.

Set Party Size: Sets the party size for the reservation.

Set Reservation Time: Sets the reservation time.

Set Reservation Date: Tries to set the reservation date.

Usage
The script is meant to be run as a standalone Python program. It is currently hard-coded to make a reservation for 4 people at 8:00 PM at the restaurant "villa-francesca" on OpenTable. The party size, reservation time, and restaurant can be adjusted by changing the appropriate variables in the script.

Before running the script, make sure that the Selenium library is installed, and the Chrome WebDriver is properly set up.

Installation
The script requires Python 3 and the Selenium library. You can install Selenium using pip:

bash
Copy code
pip install selenium
You also need the Chrome WebDriver for Selenium. Please follow the official guide to set it up.

Contribution
Contributions are welcome! Please feel free to submit a Pull Request.
