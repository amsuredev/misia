CREATE TABLE user_images(
	id SERIAL PRIMARY KEY,
	user_id INT REFERENCES users(id) NOT NULL,
	image_id INT REFERENCES images(id) NOT NULL
)