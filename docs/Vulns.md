## SQL Injection (OWASP 1)
The login screen is vulnerable to SQL injection attacks.
A simple way to log in is to write anything in the user field and

    " or "1" = "1

in the password field.

Or, for example, `" OR 1=1;--` in the username field. And anything in the pw field.

This is possible because the user input is inserted directly into the SQL query string. See [login.py](/app/views/login.py#22)

## Broken authentication (OWASP 2 & 5)

The user is validated by checking the cookie values. `logged_in` is a simple boolean, `user_id` is the user id, and `access_level` is the access level, with 2 being the admin. None of the values are checked on the server side so the client can change them to any value they want and gain access to any user account on the server.

## Sensitive data exposure

Docs can be inspected by typing /files/docs. Hint is in base.html, which is unsecurely commented out.
