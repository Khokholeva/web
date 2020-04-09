from requests import get

print(get('http://localhost:5000/api/jobs').json())
print(get('http://localhost:5000/api/jobs/1').json())
print(get('http://localhost:5000/api/jobs/11').json())
print(get('http://localhost:5000/api/jobs/ff').json())