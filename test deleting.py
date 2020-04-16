from requests import get, delete

print(get('http://localhost:5000/api/jobs').json())
# проверь чтобы в дб была работа с индексом 1 и не было 99999
print(delete('http://localhost:5000/api/jobs/1').json())
print(delete('http://localhost:5000/api/jobs/99999').json())
print(delete('http://localhost:5000/api/jobs/ff').json())

print(get('http://localhost:5000/api/jobs').json())
