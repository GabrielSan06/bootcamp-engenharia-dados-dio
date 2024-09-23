linguagens = ["python", "js", "c", "java", "php"]

print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))

print(sorted(linguagens))