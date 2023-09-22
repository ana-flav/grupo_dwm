function login() { 
	var username = document.getElementById("username").value; 
	var password = document.getElementById("password").value; 
	let login_adm ="admin"
	let password_adm = "admin"

	 if((username == login_adm) && (password == password_adm)){ 
	   window.location.href = "https://ww2.uft.edu.br//"
	 } else{
		alert("Username e/ou password incorreto(s)." );
	 }
}
