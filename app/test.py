import urllib.request
import urllib.parse
import json

fastapi_url = 'http://localhost:8000/recommend'

post_data = {
    'gender'   : 'str',
    'age'      : 0,
    'symptoms' : [
        'str'
    ]
}

try:
    post_data['gender'] = input('[INPUT] Gender (male/female): ')
    post_data['age'] = int(input('[INPUT] Age: '))
    post_data['symptoms'].append(input('[INPUT] Symptoms (please describe): '))
    print('[INFO] Finding the right department..')

    json_str = json.dumps(post_data)
    encoded = json_str.encode('utf-8')
    req = urllib.request.Request(fastapi_url, data=encoded, method='POST')
    req.add_header('Content-Type', 'application/json; charset=UTF-8')

    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
        json_data = json.loads(data)

        department = json_data.get('recommended_department')
        print(f'[RESULT] Please go to {department} department office.')
except urllib.error.HTTPError as e:
    print(f'[ERROR] HTTP Error: {e.code} {e.reason}')
    error_detail = e.read().decode('utf-8')
    print(f'[DETAIL] {error_detail}')
except urllib.error.URLError as e:
    print(f'[ERROR] POST request: {e.reason}')
except json.JSONDecodeError:
    print('[ERROR] JSON decoding failed.')



