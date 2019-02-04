import json
import requests
offset = 432530405

method = requests.get('https://api.telegram.org/bot755600779:AAEeoNRbvz0g21cKielyp_HueK09wyaaxuQ/getUpdates?timeout=100&offset={}'.format(str(offset + 1)))
print(str(method.status_code))