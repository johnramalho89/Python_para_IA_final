def anagrama(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)

#aamr #aalm
print(anagrama("amar","lama"))
print(anagrama("tabby", "batty"))