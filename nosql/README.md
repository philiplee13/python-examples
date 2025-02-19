# nosql stuff

## helpful stuff

docs: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.API.html
https://www.youtube.com/watch?v=HaEPXoXVf2k
https://youtype.github.io/types_boto3_docs/types_boto3_dynamodb/usage/
https://github.com/alexdebrie/awesome-dynamodb
videos to watch

- https://www.youtube.com/watch?v=PVUofrFiS_A

## general notes

- think about your access patterns
  - how will the end user try to fetch data
- primary key vs. composite key (allows query operation (get all and list))
  - secondary index
    - read only access patterns
    - data from main table is copied into secondary index
    - means new partition key + sort key
- unlike relational dbs, nosql don't support joins
  - so if you have multiple tables for example, you might run into an n + 1 problem quickly
  - so it's better to have a denormalized table so you can use the primary key / secondary index to get your data in an efficient manner
