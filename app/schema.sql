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
INSERT INTO products (name, price, description, image, stock) VALUES ('Phone', 299.94, 'PHone, main screen is bit broken. Nothing nice man like you cant fix', 'assets/broken_phone1.png', 4);
INSERT INTO products (name, price, description, image, stock) VALUES ('Doll', 5.20, 'Heard your nephew is having birthday in couple of weeks!', 'assets/doll.png', 25);
INSERT INTO products (name, price, description, image, stock) VALUES ('Sign', 599.99, 'Someone from lappeen Ranta was carrying this around, I scared them so they threw it away', 'assets/sign.png', 1);
INSERT INTO products (name, price, description, image, stock) VALUES ('Fish Tank', 2.20, 'Fish tank which might need little bit flextape!', 'assets/fishtank.png', 7);
INSERT INTO products (name, price, description, image, stock) VALUES ('Halloween Mask', 15.20, 'Was searching for stuff when guy came at me.. Hit him hard in the face and this fall off', 'assets/halloween_mask.png', 1);
INSERT INTO products (name, price, description, image, stock) VALUES ('Happy Robot', 100.99, 'Very happy robot! Not here to destroy the world or anything', 'assets/happy_robot1.png', 5);
INSERT INTO products (name, price, description, image, stock) VALUES ('Mystery Bag', 50.99, 'Something very sus inside! Smells funny, definatly worth it to by', 'assets/mystery_bag.png', 5);
INSERT INTO products (name, price, description, image, stock) VALUES ('Suitcase', 1000.99, '4 Digit code! Could not break it but hackerman like you definatly can', 'assets/mystery_suitcase.png', 5);
INSERT INTO products (name, price, description, image, stock) VALUES ('Painting', 599.99, 'Not picasso, but really cool', 'assets/painting.png', 1);
INSERT INTO products (name, price, description, image, stock) VALUES ('Rocket', 1040.99, 'Planning to escape? Visited Tesla HQs dumpster one day, found this.', 'assets/rocket.png', 1);
INSERT INTO products (name, price, description, image, stock) VALUES ('Scuba Suita', 299.99, 'Wanna go explore under water areas? Then this is totally for you.', 'assets/scubasuitpng.png', 1);
INSERT INTO products (name, price, description, image, stock) VALUES ('60 kmh limit sign', 199.99, 'Not sure if these is legal to own, but perfect souvenir.', 'assets/sign_2.png', 1);
INSERT INTO products (name, price, description, image, stock) VALUES ('Tire', 9.99, 'Interresting tire.', 'assets/tire.png', 1);
INSERT INTO products (name, price, description, image, stock) VALUES ('Plant', 19.99, 'Looks like xmas tree!', 'assets/plant.png', 1);
INSERT INTO products (name, price, description, image, stock) VALUES ('Pan', 49.99, 'Maby Teflon, maby now. Gets your stuff cooked anyways', 'assets/pan.png', 1);
INSERT INTO products (name, price, description, image, stock) VALUES ('Whale', 49.99, 'From deep seas! Makes perfect fit with fish tank', 'assets/whale.png', 1);


INSERT INTO users (username, password, access_level, name, email) VALUES ('admin', 'admin', 2, 'admin', 'admin@admin.ad');
INSERT INTO users (username, password, access_level, name, email, phone, address) VALUES
                  ('jaksu', '1234', 1, 'Jakke Jäyhä', 'jakkej@mail.com', '322', 'Tie 1');

INSERT INTO reviews (text, user_id, product_id) VALUES ('Test review', 1, 1);
INSERT INTO reviews (text, user_id, product_id) VALUES ('Another test review', 2, 1);

