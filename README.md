This repository is my version of the Canary project developed for UVA CS140 by group b-17. The application is a whistleblowing service where users can create communities that other users can join via invitation links. Community members can sumbit reports to "whistleblow" that can be reviewed by community admins. There is also the option to submit reports anonymously. The project is built with django and tailwind css to style the frontend views. Adding the specified api keys in src/djangoProject/.env will allow users to sign in with 
google login, and also allow the database to save its information to Amazon S3 storage. The src/djangoProject/settings.py is also configured to allow this project to be hosted by Heroku. 

In this project, I developed the functionality for users to leave and edit communities if they have the correct permissions, added various ui improvements, and also configured the github continuous integration test environment and wrote many of the tests found in src/communities/tests.py. I also developed a view for the user dashboard but due to restyling it did not make into the final version.

Current issues / future goals
  1. add more robust testing
  2. improve ability to easily navigate application
  3. add ability to reset password and verify email

