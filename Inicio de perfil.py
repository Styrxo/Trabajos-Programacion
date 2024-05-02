user = input("Ingrese su usuario: ")
contra = input("Ingrese la contraseña: ")

if user == "pedro" and contra == "1234":
    print(f'Bienvenido {user}')
elif user == "angel" and contra == "a1b2c3":
    print(f'Bienvenido {user}')
else:
    print("Error al iniciar sesión")