## Question: The operation principle of spark sql

* SparkSQL will first Parse the SQL statement to form a Tree, and then use Rule to bind and optimize the Tree, and adopt different operations for different types of nodes through pattern matching.
