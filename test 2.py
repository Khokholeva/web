from requests import get, post

# корректный
print(post('http://localhost:5000/api/jobs',
           json={'job': 'аывпвп', 'work_size': 12,
                 'team_leader': 2, 'start_date': '21',
                 'end_date': '32', 'collaborators': '3', 'is_finished': True}).json())
#  некорректный - не все ключи
print(post('http://localhost:5000/api/jobs',
           json={'job': 'hh', 'work_size': 11,
                 'team_leader': 2, 'start_date': '21',
                 'end_date': '32'}).json())
#  некорректный - не все ключи
print(post('http://localhost:5000/api/jobs',
           json={'job': 'аывпвп', 'work_size': 12,
                 'team_leader': 2,
                 'end_date': '32', 'collaborators': '3', 'is_finished': True}).json())
# некорректный - совпадает id
print(post('http://localhost:5000/api/jobs',
           json={'id': 1, 'job': 'hh', 'work_size': 11,
                 'team_leader': 2, 'start_date': '21',
                 'end_date': '32', 'collaborators': '4, 3', 'is_finished': True}).json())

print(get('http://localhost:5000/api/jobs').json())