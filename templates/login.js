function validateForm() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if (email == "") {
        alert("Please enter a email.");
        return false;
    }
    if (password == "") {
        alert("Please enter a password.");
        return false;
    }
  }