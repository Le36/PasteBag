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

function contactConfirm() {
    return confirm("Do you really want to send this message?");
}

function checkContact(form) {
    if (form.email.value.length === 0) {
        alert("Contact information cannot be empty!");
        return false;
    }
    if (form.message.value.length === 0) {
        alert("Message cannot be empty!");
        return false;
    }
    return contactConfirm();
}
