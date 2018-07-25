person={'name':'stephania','address':'seoul', 'email':'kaithie@naver.com'}
print(person)
print(person['name'])
print(person['email'])

person['name']='kaithie'
print(person.items())
for key, value in person.items():
    print("\nKey:"+key)
    print("Value:"+value)

for key, value in person.items():
    print('\nKey\\ "'+key+'"')
    print('Value\\ "'+value+'"')   