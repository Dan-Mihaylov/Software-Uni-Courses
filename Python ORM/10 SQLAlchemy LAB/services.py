from models import User, Order
from main import Session


# To add a user you call the constructor class Session() and then can use the method .add, with an instance of
# the user you want to add to the db.
def add_user(username: str, email: str):

    with Session() as session:
        new_user = User(username=username, email=email)
        session.add(new_user)
        session.commit()
        return f"User: {new_user.username} | {new_user.email} Added successfully."


# 01 Add user with your username and email

# user_name = input("Enter Username: ")
# mail = input("Enter email: ")
# add_user(user_name, mail)

# 02 retrieve info
def get_all_users():

    with Session() as session:
        all_users = session.query(User).all()
        result = []
        for user in all_users:
            result.append(f"Username: {user.username}\nE-mail: {user.email}")
        return "\n---------------\n".join(result)


# print(get_all_users())


# 03 Update info
# First you need to get the object you want to update and then update it and commit to the db.

def update_username(old_username: str, new_username: str):

    with Session() as session:
        found_user = session.query(User).filter_by(username=old_username).first()

        if found_user:
            found_user.username = new_username
            session.commit()
            return f"Username: {old_username} changed to {new_username}"
        else:
            return f"Username: {old_username} does not exist in database"


# print(update_username("panter_pete", "peter_pan"))

# When you use the query(User).filter_by(username='some').first() it will return the user it has found
# If you use the filter_by().all() it will return a list with User objects that you can access with a for-cycle

# with Session() as session:
#     found_user = session.query(User).filter_by(username='peter_pan').first()
#     print(found_user)


# 04 Delete records

def delete_user(username: str):

    with Session() as session:
        found_user = session.query(User).filter_by(username=username).first()

        if found_user:
            session.delete(found_user)
            session.commit()
            return f" {found_user.username} deleted"
        else:
            return f"No such user in database."


# print(delete_user("peter_pan"))

# Create data to insert into DB
users_to_insert = [
    ("john_doe", "john_doe@example.com"),
    ("sarah_smith", "sarah.smith@gmail.com"),
    ("mike_jones", "mike.jones@company.com"),
    ("emma_wilson", "emma.wilson@domain.net"),
    ("david_brown", "david.brown@email.org"),
]

# # Insert the data into DB
# for user_info in users_to_insert:
#     print(add_user(*user_info))

# 05 Transactions
"""
Transactions are used to group together a block of code, that needs to either be successfully executed as a whole,
or fail as a whole.
"""


def delete_all_users():
    session = Session()     # Create an instance of the session.

    try:

        session.begin()     # always begin the session
        session.query(User).delete()    # Try to delete all objects in the User model
        session.commit()
        return "All users have been deleted."

    except Exception as error:
        session.rollback()      # If an exception occurs you rollback the changes and nothing gets saved in the db.
        return str(error)

    finally:
        session.close()     # The finally "block" always gets executed and is used to close the session.


# print(delete_all_users())


# 06 Add Orders
def add_orders():

    with Session() as session:
        all_users = session.query(User).all()
        all_orders = []

        for user in all_users:
            all_orders.append(Order(user_id=user.id))

        session.add_all(tuple(all_orders))
        session.commit()
        return "All orders added I guess..."


# print(add_orders())

# 06.2
# Retrive order information, through relationships with user.
def retrieve_orders_info():

    with Session() as session:

        all_orders = session.query(Order).order_by(Order.user_id.desc()).all()

        if not all_orders:
            print("No orders yet.")

        else:
            for order in all_orders:
                user = order.user
                print(f"Order number {order.id} | Is completed: {order.is_completed} | Username: {user.username}")


retrieve_orders_info()
