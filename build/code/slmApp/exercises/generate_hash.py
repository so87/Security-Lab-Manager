import hashlib

def gen(student, exercise, instructor):
    pre_hash_string = student.username+exercise.name+instructor.password
    hash_object = hashlib.sha256(pre_hash_string.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig