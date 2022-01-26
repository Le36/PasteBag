# PasteBag made with Python Flask #

PasteBag is an online text storage site.

[https://pastebag.herokuapp.com/](https://pastebag.herokuapp.com/)

This project will be a clone of similar more known products such as Pastebin or GitHub,
just made with Python and Flask and having much lesser features.

Main features include uploading pastes and viewing them. There will also be support for user accounts,
to have possibility to edit or delete created pastes.

# Features #

Pastes have their creator, content, unique id and view count. There is a list of public pastes shown on
main page that is sorted by view count.

### Anonymous user: ###
- [x] create pastes
- [ ] 2 publicity levels for pastes: public and private
- [x] see public pastes listed on main page
- [x] private pastes have unique id on them that is shown for the creator, this can be then 
be shared for anybody
- [x] access private pastes if it has access to the unique id

### Logged user: ###
- [x] create the account
- [x] possibility to log in
- [x] view own pastes
- [ ] delete or edit own pastes
- [x] same features as anonymous user

### Admin user: ###
- [ ] list of public and private pastes
- [ ] can delete or edit any paste
- [ ] same features as logged and anonymous user