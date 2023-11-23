CREATE TABLE limb_test (
    id SERIAL PRIMARY KEY,
    img BYTEA NOT NULL,
    info VARCHAR(32) NOT NULL
); 

CREATE TABLE limb_train (
    id SERIAL PRIMARY KEY,
    img BYTEA NOT NULL,
    info VARCHAR(32) NOT NULL
);

CREATE TABLE perelimb_test (
    id SERIAL PRIMARY KEY,
    img BYTEA NOT NULL,
    info VARCHAR(32) NOT NULL
);

CREATE TABLE perelimb_train (
    id SERIAL PRIMARY KEY,
    img BYTEA NOT NULL,
    info VARCHAR(32) NOT NULL
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    login VARCHAR(32) NOT NULL,
    password VARCHAR(32) NOT NULL
);

CREATE TABLE limb (
    id SERIAL PRIMARY KEY,
    img BYTEA NOT NULL,
    info VARCHAR(32)         
);

CREATE TABLE perelimb (
    id SERIAL PRIMARY KEY,
    img BYTEA NOT NULL,
    info VARCHAR(32)         
);

CREATE TABLE limb (
    id SERIAL PRIMARY KEY,
    img BYTEA NOT NULL,
    info VARCHAR(32)         
);

CREATE TABLE perelimb (
    id SERIAL PRIMARY KEY,
    img BYTEA NOT NULL,
    info VARCHAR(32)         
);





