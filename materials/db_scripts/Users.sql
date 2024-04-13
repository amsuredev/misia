CREATE TABLE users (
	id SERIAL PRIMARY KEY,
    chat_id character varying NOT NULL,
	first_name character varying NOT NULL,
	age integer NOT NULL,
	sex character varying NOT NULL,
	sex_preference character varying NOT NULL,
	profile_message character varying,
	town character varying NOT NULL,
	country character varying,
    active boolean NOT NULL
)