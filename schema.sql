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
    paste_id TEXT UNIQUE,
    paste    TEXT,
    username TEXT,
    title    TEXT,
    private  BOOLEAN,
    burn     BOOLEAN,
    syntax   TEXT,
    time     TIMESTAMP
);

CREATE TABLE paste_views
(
    id       SERIAL PRIMARY KEY,
    paste_id TEXT UNIQUE REFERENCES pastes (paste_id) ON DELETE CASCADE,
    views    INTEGER
);

CREATE TABLE profile
(
    id       SERIAL PRIMARY KEY,
    username TEXT UNIQUE REFERENCES users (username),
    about    TEXT
);

CREATE TABLE picture
(
    id       SERIAL PRIMARY KEY,
    username TEXT UNIQUE REFERENCES users (username),
    data     BYTEA
);

CREATE TABLE contact
(
    id      SERIAL PRIMARY KEY,
    email   TEXT,
    message TEXT
);