Following things must be taken into accout while building the features.

- When an user registers, if it's a successful registration, the user should automatically login to it's session.
- Login can be done either by username, or email id (it must be the same field in frontend). Backend should be able to handle it automatically.

###### Homepage should behave like below

- If user is logged in, it should load home page
- If user is not logged in, it should redirect to login page

###### Login and Register page should behave like below

- If user is not logged in, it should load the requested page (based on login or register)
- If user is logged in, it should redirect to home page
- Upon successful registration or login, the user should be redirected to the home page

###### Logout button click should behave like below

- If user is logged in, it should remove the user from session.
  - If successful, it should redirect to login page.
  - Else, it should give a browser alert saying "logout failed".
- If user is not logged in, it should return following json response with 400 status code.

```json
{
  "message": "No user in session"
}
```
