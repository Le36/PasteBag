Prism.plugins.toolbar.registerButton("view-raw", function (t) {
    var e = t.element.parentNode;
    if (e && /pre/i.test(e.nodeName) && e.hasAttribute("data-src")) {
        var n = e.getAttribute("data-src"), a = document.createElement("a");
        return a.textContent = "View raw", a.href = n, a
    }
});