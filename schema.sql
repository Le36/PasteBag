CREATE TABLE users
(
    id       SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin    BOOLEAN
);

CREATE TABLE pastes
(
    id       SERIAL PRIMARY KEY,
    pasteId  TEXT,
    paste    TEXT,
    username TEXT
)