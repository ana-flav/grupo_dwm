from django.shortcuts import render
from django.http import JsonResponse


from .models import Users

import bcrypt

def cadastro(request):
    return render(request , "registre.html")


def createUser(request):
    user = Users()    

    data = request.POST
    cpf_validate  = Users(cpf = data['cpf']).validateCpf()
    email_validate  = Users(email = data['email']).validateEmail()
    name_validate  = Users(name = data['name']).validateName() 
    password_validate = Users(password = data['password']).validatePassword()
    data_de_nascimento_validate = Users(data_de_nascimento = data['data_de_nascimento']).validateDate()

    if  cpf_validate != None:
        return JsonResponse({'error' : cpf_validate})
    else:
        user.cpf = data['cpf']
        
    if email_validate != None:
        return JsonResponse({'error' : email_validate})
    else:
        user.email = data['email']

    if  name_validate!= None:
        return JsonResponse({'error' : name_validate})
    else:
        user.name = data['name']


    if password_validate  != None:
        return JsonResponse({'error' : password_validate})
    else:
         
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(data['password'].encode(), salt)
        user.password = hash
        

    if data_de_nascimento_validate != None:
        return JsonResponse({'error' : data_de_nascimento_validate})
    else:
        user.data_de_nascimento = data['data_de_nascimento']
            
    user.save()
    return render(request, "registre.html")