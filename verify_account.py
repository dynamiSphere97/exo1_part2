def verify_account(username, password):
    if username == "admin":
        if password == "admin":
            reponse = True
        else:
            reponse = False
    else:
        reponse = False
    return reponse