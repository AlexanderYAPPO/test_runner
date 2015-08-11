tests = [
    {"name": "create-tenant", "rps": 10, "times": 100, "type_name": "rps"},
    {"name": "keystone", "type_name": "rps"},
    {"name": "create-user"},
    {"name": "create-and-list-services", "concurrency": 2, "times": 100, "type_name": "constant"}
]