CREATE TABLE likes (
	id SERIAL PRIMARY KEY,
	superior_id INT REFERENCES users(id) NOT NULL,
	interior_id INT REFERENCES users(id) NOT NULL,
	is_executed boolean NOT NULL DEFAULT FALSE,
	mutual boolean
)