
        function login() {
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;

            let login_adm ="admin"
            let password_adm = "admin"
               
            if( (username == login_adm) && (password == password_adm)){
                    alert("Login bem-sucedido para " + username);
                    
            }
            else{
                    alert(" username e/ou password incorreto " );
                    
                    }
                }