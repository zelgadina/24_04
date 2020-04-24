unc_users = ['pavel', 'petr', 'semen']

con_users = []

while unc_users:
    cur_user = unc_users.pop()
    print(cur_user)
    con_users.append(cur_user)

print(unc_users)
print(con_users)