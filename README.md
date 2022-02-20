# PasteBag made with Python Flask #

PasteBag is an online text storage site.

Live demo of the project available at:

[https://pastebag.herokuapp.com/](https://pastebag.herokuapp.com/)

This project is a clone of similar more known products such as Pastebin or GitHub, just made with Python and Flask and
having much lesser features.

Main features include uploading pastes and viewing them. There is also support for user accounts, with custom avatars
and info box. Users can also delete their own pastes.

# Features #

Pastes have their creator, content, unique id, view count, syntax highlighting and created time. There is a list of
public pastes shown on main page that is sorted by view count.

### Anonymous user: ###

- [x] create pastes
- [x] 2 publicity levels for pastes: public and private
- [x] see public pastes listed on main page
- [x] private pastes have unique id on them that is shown for the creator, this can be then be shared for anybody
- [x] access private pastes if it has access to the unique id
- [x] create "burn after reading" pastes, that get destroyed after viewing them
- [x] send message to admins
- [x] syntax highlight pastes that contain code
- [x] download pastes with button
- [x] copy pastes with button

### Logged user: ###

- [x] create the account
- [x] possibility to log in
- [x] view own pastes
- [x] delete own pastes
- [x] have profile picture on profile page, editable
- [x] have profile "info box" on profile page, editable
- [x] same features as anonymous user

### Admin user: ###

- [x] "admin panel"
- [x] list of public and private pastes
- [x] can delete any paste
- [x] view forms sent to admins
- [x] delete forms sent to admins
- [x] same features as logged and anonymous user

# How to? #

To run this project you will need Python and PostgreSQL.

Start by cloning this project. Enter root and create file called ```.env``` and paste the following there:

```
DATABASE_URL=your postgres address
SECRET_KEY=your secret key
```

then do the following commands:

```
python3 -m venv venv
source venv/bin/activate
```

install requirements with:

```pip install -r requirements.txt```

add correct tables to postgres with:

```psql < schema.sql```

and run with:

```flask run```

### Create admin ###

To create admin go to the site in browser and create user like you normally would

then in psql do:

```UPDATE users SET admin = true WHERE username = 'your username';```

then log off and log in and voilà!