# review_app

## Narrative / outline
The review app is an application to record customer's reviews of events.  Customers may create / edit events and then leave reviews for those events. Once a review is left it may not be modified.  The application here is 'bare bones' and only contains enough code to demonstrate basic principles of object oriented design, flask and templates.  This template serves as a 'boilerplate' for individual student projects to be based off.

### Example of logins table

User type | Email | Password 
------------ | ------------- | --------------
Admin | a@a.com | 1234
Employee | b@a.com | 12345
Customer | c@a.com | 12345

### Extending the flaskTemplate
In this branch of the flaskTemple project I extend the template to build a 3 table application.  During the process I will demonstrate many of the tasks you will need to complete to finish your project.

### MySQL
- userfavorite loactions
```
SELECT * ..... JOIN....
```
 
### Changes / additions for this branch
* Demonstrate how to add tables / class defs
* Add 2 new tables - events and attendance
* Clone customer screens for the event screens
* Demonstrate how to do data binding to create a dropdown / list of items from another table.  
	* This is important anytime you have a foreign key.
* Add more complex verifyNew() code
* Add verifyChange() method
* Discuss methods for debugging including debug file logs
* create a user/customer 'type' attribute which only allows access to certain screens.

## Schema

![relational schema](/docs/schema_main.JPG)
