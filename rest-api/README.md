## Restful API

- docker for psql connection
- CRUD api and models
- fastapi, pydantic, etc
- unit tests and integration tests

### To run the app

- make sure `venv` is activated
- for `dev`
  - `fastapi dev app/main.py`
- curl -X GET http://localhost:8000/users/ | jq
- curl -X POST -d '{"name": "test_name_create", "age": "100"}' -H "Content-Type: application/json" http://localhost:8000/users/ | jq
- curl -X DELETE http://localhost:8000/users/2
- curl -X PUT http://localhost:8000/users/3 -d '{"name": "test-update", "age": "1000"}' -H "Content-Type: application/json"

### Notes

- for fastapi, if you return a list, dict, pydantic model, database model, etc
  fastapi will automatically use `jsonable_encoder()` to encode it for you - docs: https://fastapi.tiangolo.com/tutorial/encoder/
- but we can return a `Response` directly
  - docs: https://fastapi.tiangolo.com/advanced/response-directly/#returning-a-custom-response
