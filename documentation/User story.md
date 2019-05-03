# User stories
## Current roles
* Guest
* User
* Admin

## Current features
### Features available to everyone
**Anyone can view the home page**

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

```

**Anyone can view individual scripts**
```sql
Related SQL query:

```

**Anyone can browse scripts' comments**
```sql
Related SQL query:

```

**Anyone can create an account**
```sql
Related SQL query:

```

### Features for those who have an account
**User can log in**
```sql
Related SQL query:

```

**User can log out**
```sql
Related SQL query:

```

**User can view their own user info page**
```sql
Related SQL query:

```

**User can view other user's less detailed user info page**
```sql
Related SQL query:

```

**User can create a new script**
```sql
Related SQL query:

```

**User can modify their own created scripts**
```sql
Related SQL query:

```

**User can delete their own created scripts**
```sql
Related SQL query:

```

**User can comment on scripts**
```sql
Related SQL query:

```

**User can delete only their own comments**
```sql
Related SQL query:

```

**User can edit their own comments**
```sql
Related SQL query:

```

**User can favourite scripts to find them easily**
```sql
Related SQL query:

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
