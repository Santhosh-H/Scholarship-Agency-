function validateForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var num = document.getElementById("num").value;
    var password = document.getElementById("password").value;
    if (name == "") {
        alert("Please enter a Username.");
        return false;
    }
    if (email == "") {
        alert("Please enter a email.");
        return false;
    }
    if (num == "") {
        alert("Please enter a Phone no.");
        return false;
    }
    if (password == "") {
        alert("Please enter a password.");
        return false;
    }
  }