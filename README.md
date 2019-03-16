The home page is viewable by Admins, users, and guests. Guests and admins can not post, only registered users can.
Guest users can create an account, and sign in. At that point, they can start creating posts. All levels can view public posts.
Users can invite other users to view their private posts by view their post details, clicking share and then entering their 
username. A user that's invited to share a private post can not share that post with somebody else unless they are the owner. Only
accounts that are marked as 'Admin' or 'Staff' can view the admin page (localhost:8000/admin).

The home page will show the 10 most recent public pastes, sorted by most recent at the top. By clicking 'Post Details', a user
can view all of their posts, delete their posts, and they have the ability to share their post with another user.

There is also an option to delete an account in the nav bar. On the backend, this disables the user, and changes their name to
deactivated user (to not mess with foreign key linking). By running sslserver the web app has a self signed certificate and
runs on HTTPS. XSS, SQLi, and CSRF security measures are implemented throughout the source code.
