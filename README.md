# JSON Store

## API

### Headers

You must pass the following required headers with all requests:

1. __x-key__: \<your-api-key>
2. __content-type__: 'application/json'

### Endponts

#### 1. POST /store/

__Accepts__ : valid JSON object  
__Response__: URL to fetch POSTed JSON (format: http://\<host>/store/\<object-key>)

#### 2. GET /store/\<object-key>

__Response__: JSON object which matches the requested key

## How to test ?

1. Test Runner: `coverage run manage.py test`
2. Test Report: `coverage report`
