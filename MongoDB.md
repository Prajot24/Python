# MongoDb

`use lib`  used to create database

`db`  - used to check current database

`db.createCollection('Books')` - used to create collection

`show collections`  - used to show collections in database

**Insert Document in Collection**

`db.Books.insertOne({name:"java",page:270,price:900})` - used to insert element

`db.Books.insertMany([{name:"C++",page:670,price:800},{name:"python",page:760,price:350}])` - to insert many document in collections

`db.Books.find()` - used to show documents in collections

**Update Document**

`db.Books.updateOne({_id: ObjectId('65d5c62cdea8069b458f1392')},{$set:{name:"Complete Java One Book",price:300,pages:1000}})` - used to update existing document

[Update Operator](https://www.mongodb.com/docs/manual/reference/operator/update/)

Delete Document

we can use deleteOne(),remove(),deleteMany() to remove object

`db.Books.deleteOne({_id: ObjectId('65d5c703dea8069b458f1394')})` - used to delete

[Delete Document](https://www.mongodb.com/docs/mongodb-shell/crud/delete/)

---

---

`db.Books.find().limit(2)`  - used to set limit o showing function

`db.Books.find().sort({price:1})` - {1 is for Asce and -1 is for Dsce}

`db.Books.find({price:{$eq:900}})`- Matches values that are equal to a specified value.

`db.Books.find({price:{$eq:350}})` - Matches values that are greater than a specified value.

`db.Books.find({price:{$not:{$gt:500}}})` - Price Not Greater than 500

[Read More](https://www.mongodb.com/docs/manual/reference/operator/query/)