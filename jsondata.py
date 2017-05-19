jsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(jsonData)
print(json.dumps(jsonDataAsPythonValue))
