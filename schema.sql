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
    pasteId  TEXT UNIQUE,
    paste    TEXT,
    username TEXT,
    views    INTEGER,
    title    TEXT,
    private  BOOLEAN,
    burn     BOOLEAN,
    syntax   TEXT
);

CREATE TABLE contact
(
    id      SERIAL PRIMARY KEY,
    email   TEXT,
    message TEXT
)