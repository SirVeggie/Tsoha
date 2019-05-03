# User stories
## Current roles
* Guest
* User
* Admin

## Current features
### Features available to everyone
**Anyone can view the home page**
```sql
Related SQL query:
-
```

**Anyone can see the amount of contributing users**
```sql
Related SQL query:
SELECT COUNT(DISTINCT account.id) FROM account LEFT JOIN script ON account.id = script.author_id LEFT JOIN comment ON account.id = comment.author_id WHERE account.id = script.author_id OR account.id = comment.author_id;
```

**Anyone can see the top contributor**
```sql
Related SQL query:
SELECT account.username, COUNT(script.id) FROM account, script WHERE account.id = script.author_id GROUP BY username ORDER BY COUNT(script.id) DESC;
```

**Anyone can see the amount of scripts the top contributor has posted**
```
Related SQL query:
Uses the same query as above.
```

**Anyone can list all scripts**
```sql
Related SQL query:
SELECT * FROM script;
```

**Anyone can view individual scripts**
```sql
Related SQL query:
SELECT * FROM script WHERE script.id = (script_id);
```

**Anyone can browse scripts' comments**
```sql
Related SQL query:
SELECT * FROM comment WHERE comment.scipt_id = (script_id);
```

**Anyone can create an account**
```sql
Related SQL query:
INSERT INTO account(username,password) VALUES ( (form_username),(form_password) );
```

### Features for those who have an account
**User can log in**
```sql
Related SQL query:
SELECT * FROM account WHERE account.username = (username) AND account.password = (password);
```

**User can log out**
```sql
Related SQL query:
-
```

**User can view their own user info page**
```sql
Related SQL queries:
User - SELECT * FROM account WHERE account.id = (current_user.id);
User's scripts - SELECT * FROM script WHERE script.author_id = (current_user.id);
User's favourites - SELECT script.* FROM script, favourite WHERE script.id = favourite.script_id AND favourite.user_id = (current_user.id);
User's comments - SELECT * FROM comment WHERE comment.author_id = (current_user.id);
```

**User can view other user's less detailed user info page**
```sql
Related SQL query:
SELECT * FROM account WHERE account.id = (user_id);
```

**User can create a new script**
```sql
Related SQL query:
INSERT INTO script(name,language,content,author_id) VALUES ( (form_name),(form_language),(form_content),(current_user.id) );
```

**User can edit their own created scripts**
```sql
Related SQL query:
UPDATE script SET name=(form_name), content=(form_content) WHERE script.id = (script_id);
```

**User can delete their own created scripts**
```sql
Related SQL query:
REMOVE FROM script WHERE script.id = (script_id);
```

**User can comment on scripts**
```sql
Related SQL query:
INSERT INTO comment(title,content,author_id,script_id) VALUES ( (form_title),(form_content),(current_user.id),(script_id) );
```

**User can delete only their own comments**
```sql
Related SQL query:
DELETE FROM comment WHERE comment.id = (comment_id);
```

**User can edit their own comments**
```sql
Related SQL query:
UPDATE comment SET title=(form_title), content=(form_content) WHERE comment.id = (comment_id);
```

**User can favourite scripts to find them easily**
```sql
Related SQL query:
INSERT INTO favourite(user_id,script_id) VALUES ( (current_user.id),(script_id) );
```

**User can unfavourite scripts**
```sql
Related SQL query:
DELETE FROM favourite WHERE favourite.script_id = (script_id) AND favourite.user_id = (current_user.id);
```

### Features for admins
**Admin user can delete any post**

**Admin user can delete any comment**

**Admin user can modify any comment**
```
These user stories' SQL queries are the same as User delete/modify queries.
```

## User stories that couldn't be completed
User can browse scripts by categories

User can search for scripts

User can sort scripts

User can suggest changes to someone elses script through the system
