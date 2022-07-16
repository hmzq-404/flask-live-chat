field_constraints = {
    "User": {
        "username": {"min": 3, "max": 16},
        "password": {"min": 8, "max": 16},
        "password_hash": {"max": 256},
    },
    "Message": {"body": {"min": 1, "max": 1024}},
    "Room": {"name": {"min": 3, "max": 64}, "description": {"min": 0, "max": 4096}},
}


user_constraints = field_constraints["User"]
message_constraints = field_constraints["Message"]
room_constraints = field_constraints["Room"]
