# realestate
## Initialize
First, create your Python environment and install the required libraries with the following command:
```bash
pip install -r requirements.txt
```
Then prepare your database using the following commands:
```bash
Python manager.py makemigrations
Python manager.py migrates
```
And also create an admin user using the following command:
```bash
Python manager.py createsuperuser
```
Now we start the program:
```bash
python manager.py runserver
```
The site starts on port ```8000```.
Now add the cities and provinces by Django admin ```(localhost:8000/admin)```.
## Description
on the main page of the site, you can register or login (if logged in).
If you are logged in, you can see your logout or profile section.
On the main page, see the list of all the houses added by users.
In the profile section, you can change the personal information you have registered.
In the sidebar section of the profile, you can see the apartment sections, houses that you are the manager of.
In the add apartment section, add the house and enter the information of that house. from this action, The desired house is displayed in my apartments.
You can also provide the above information in Change apartments section.
In offers, you can see the offers sent to a shared house by other users. Can you accept that if one of them is accepted, the other offers for that house will be removed from the list, then the intended user will be registered as a tenant.
In the rented apartments section, you can see the houses that are rented.
In the list on the main page, if the user chooses a house that is not for him, he can make an offer.
#### Add Apartment
![Add Apartment](https://github.com/proshir/realestate/assets/19504971/3169a6ad-7961-44f4-b95f-4411926906f8)
#### Apartment List
![Apartment List](https://github.com/proshir/realestate/assets/19504971/65ebd232-af7a-4a07-bf16-5fde0202191e)
#### Register
![Register](https://github.com/proshir/realestate/assets/19504971/77fa9932-1800-48bc-9f12-859a3f6ef9a7)
#### Apartment Detail
![Apartment Detail](https://github.com/proshir/realestate/assets/19504971/294a3eb9-98db-4937-8d59-b11a852b5fb5)

## Diagrams
![sequence diagram](https://github.com/proshir/realestate/assets/19504971/81e60c40-74b0-48f8-adcd-6f92197cd9a6)
### Class Diagram
![class diagram](https://github.com/proshir/realestate/assets/19504971/16500519-0d1e-4302-be30-e6fedc456742)
