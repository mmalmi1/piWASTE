DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS reviews;

CREATE TABLE products (
  product_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  price REAL NOT NULL,
  description TEXT NOT NULL,
  image TEXT,
  stock INTEGER DEFAULT 0
);

CREATE TABLE users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  access_level INTEGER NOT NULL
);

CREATE TABLE reviews (
  review_id INTEGER PRIMARY KEY AUTOINCREMENT,
  text TEXT UNIQUE NOT NULL,
  user_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (user_id),
  FOREIGN KEY (product_id) REFERENCES products (product_id)
);

INSERT INTO products (name, price, description, image, stock) VALUES ('Teddy', 10.15, 'Little broken teddy trying to find new home. Might need some additional cleaning. Otherwise in perfect condition', 'assets/broken_teddy1.png', 10);
INSERT INTO products (name, price, description, image, stock) VALUES ('Guitar', 50.15, 'Guitar in perfect condition. Start your rockstar career today and buy this perfect guitar', 'assets/guitar.png', 1);

INSERT INTO users VALUES (1, 'admin', 'admin', 2)
