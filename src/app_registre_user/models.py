from django.db import models
from django.core.exceptions import ValidationError


from validate_docbr import CPF
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password

from datetime import date

class Users(models.Model):
    id = models.AutoField(primary_key= True , unique=True)
    cpf = models.CharField(max_length=14 ,blank=False , unique=True)
    email = models.CharField(max_length=255 , blank=False , unique=True)
    name = models.CharField(max_length=255 ,blank=False)
    password = models.CharField(max_length=255 ,blank=False)
    data_de_nascimento = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    
    def validateCpf(self):
        try: 
            CPF().validate(self.cpf)
            
        except ValidationError as error:
            return error.messages
    
    def validateEmail(self):
        try:
            validate_email(self.email)
            
        except ValidationError as error:
            return error.messages

    def validateName(self):
        if not self.name.replace(' ', '').isalpha():
            return 'nome invalido'
    
    def validatePassword(self):
        try:
            validate_password(self.password)
            
        except ValidationError as error:
            return error.messages
    def validateDate(self):
        
        try:
            data_de_nascimento = date.fromisoformat(self.data_de_nascimento)

            
            age = date.today().year - data_de_nascimento.year - ((date.today().month, date.today().day) < (data_de_nascimento.month, data_de_nascimento.day))
            if age < 18:
                return 'usuário deve ter no mínimo  18 anos de idade'
            elif  age > 150:
                return 'data invalida'
        except ValueError:
            return  'Data de nascimento inválida. Use o formato AAAA-MM-DD'


   
