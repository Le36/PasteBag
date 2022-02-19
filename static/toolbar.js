Prism.plugins.toolbar.registerButton("view-raw", function (t) {
    let e = t.element.parentNode;
    if (e && /pre/i.test(e.nodeName)) {
        if (e.hasAttribute("data-src")) {
            let n = e.getAttribute("data-src"), a = document.createElement("a");
            return a.textContent = "View raw", a.href = n, a
        }
    }
});

Prism.plugins.toolbar.registerButton("creator", function (t) {
    let n = "/u/" + creator, a = document.createElement("a");
    if (creator === "Anonymous") {
        return a.textContent = "Author: Anonymous", a;
    }
    let trimmed = creator.substring(0, 15);
    return a.textContent = "Author: " + trimmed, a.href = n, a
});

Prism.plugins.toolbar.registerButton("total-views", {
    text: "Views: " + (views === "None" ? 0 : views)
});

Prism.plugins.toolbar.registerButton("date", {
    text: date
});