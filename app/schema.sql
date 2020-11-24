DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS purchase_history;

CREATE TABLE products (
  product_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  price REAL NOT NULL,
  description TEXT NOT NULL,
  image TEXT,
  stock INTEGER DEFAULT 0,
  visible INTEGER DEFAULT 1
);

CREATE TABLE users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  access_level INTEGER NOT NULL,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  phone TEXT,
  address TEXT
);

CREATE TABLE reviews (
  review_id INTEGER PRIMARY KEY AUTOINCREMENT,
  text TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (user_id),
  FOREIGN KEY (product_id) REFERENCES products (product_id),
  UNIQUE(user_id, product_id)
);


CREATE TABLE purchase_history (
  user_id INTEGER PRIMARY KEY,
  shopping_cart TEXT NOT NULL,
  timestamp TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (user_id)
);


INSERT INTO products (name, price, description, image, stock) VALUES ('Teddy', 10.15, 'Little broken teddy trying to find new home. Might need some additional cleaning. Otherwise in perfect condition', 'assets/broken_teddy1.png', 10);
INSERT INTO products (name, price, description, image, stock) VALUES ('Guitar', 50.15, 'Guitar in perfect condition. Start your rockstar career today and buy this perfect guitar', 'assets/guitar.png', 1);

INSERT INTO users (username, password, access_level, name, email) VALUES ('admin', 'admin', 2, 'admin', 'admin@admin.ad');
INSERT INTO users (username, password, access_level, name, email, phone, address) VALUES
                  ('jaksu', '1234', 1, 'Jakke Jäyhä', 'jakkej@mail.com', '322', 'Tie 1');

INSERT INTO reviews (text, user_id, product_id) VALUES ('Test review', 1, 1);
INSERT INTO reviews (text, user_id, product_id) VALUES ('Another test review', 2, 1);
