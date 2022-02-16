function check(form) {
    try {
        if (form.paste.value.length === 0) {
            alert("Paste cannot be empty!");
            return false;
        }
    } catch (ignored) {
    }
    if (form.username.value.length === 0) {
        alert("Username cannot be empty!");
        return false;
    }
    if (form.password.value.length === 0) {
        alert("Password cannot be empty!");
        return false;
    }
    return true;
}

function deleteConfirm() {
    return confirm("Do you really want to delete this paste?");
}
