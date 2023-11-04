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


