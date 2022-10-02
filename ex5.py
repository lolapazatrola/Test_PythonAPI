import json

json_text = '{"test_first_key": "test_first_variable", "test_second_key": "test_second_variable"}'
obj = json.loads(json_text)
print(obj['test_second_key'])