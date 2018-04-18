# hash_test.py



import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

print("--------------------------------------------------------------------")

original_data = "1234 ABCDEFGHIJ Example Description Here src_path weight retail"
original_hash = hashlib.sha512(original_data.encode()).hexdigest()

print("Original: {}".format(original_data))
print("Hash: {}".format(original_hash))

print("--------------------------------------------------------------------")

test_data = "1234 ABCDEFGHIJ Example Description Here src_path weight retail"
test_hash = hashlib.sha512(test_data.encode()).hexdigest()

print("Test: {}".format(test_data))
print("Hash: {}".format(test_hash))

if original_hash == test_hash:
    print("The new hash matches the original hash")
else:
    print("The new hash does not match the original hash")
    print("Updating to use the new hash")
    original_hash = test_hash

print("--------------------------------------------------------------------")

test_data = "1234 ABCDEFGHIJ Example Description Here src_path 0.2 retail"
test_hash = hashlib.sha512(test_data.encode()).hexdigest()

print("Test: {}".format(test_data))
print("Hash: {}".format(test_hash))

if original_hash == test_hash:
    print("The new hash matches the original hash")
else:
    print("The new hash does not match the original hash")
    print("Updating to use the new hash")
    original_hash = test_hash

print("--------------------------------------------------------------------")

test_data = "p@55w0rd"
test_hash = hashlib.md5(test_data.encode()).hexdigest()
print("Hash: {}".format(test_hash))