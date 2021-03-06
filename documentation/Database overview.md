```sql
CREATE TABLE account (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  username VARCHAR(144) NOT NULL,
  password VARCHAR(144) NOT NULL
  PRIMARY KEY (id)
);

CREATE TABLE script (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  name VARCHAR(144) NOT NULL,
  language VARCHAR(50) NOT NULL,
  content VARCHAR(30000),
  author_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY(author_id) REFERENCES account (id)
);

CREATE TABLE comment (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  title VARCHAR(144) NOT NULL,
  content VARCHAR(10000) NOT NULL,
  author_id INTEGER NOT NULL,
  script_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY(author_id) REFERENCES account (id),
  FOREIGN KEY(script_id) REFERENCES script (id)
);

CREATE TABLE userrole (
  id INTEGER NOT NULL,
  role VARCHAR(144) NOT NULL,
  user_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY(user_id) REFERENCES account (id)
);

CREATE TABLE favourite (
  id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  script_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY(user_id) REFERENCES account (id),
  FOREIGN KEY(script_id) REFERENCES script (id)
);
```


![Database diagram](https://github.com/SirVeggie/Tsoha/blob/master/documentation/Database%20diagram.png)
