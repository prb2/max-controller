
function slider1(user) {
    var value = $("#slider1")[0].value;
    $.get("/slider1/" + user, { "value" : value });
}

function slider2(user) {
    var value = $("#slider2")[0].value;
    $.get("/slider2/" + user, { "value" : value });
}

function slider3(user) {
    var value = $("#slider3")[0].value;
    $.get("/slider3/" + user, { "value" : value });
}

function increment(user) {
    $.get("/increment/" + user);
}

function decrement(user) {
    $.get("/decrement/" + user);
}

function randomFloat(user) {
    $.get("/random_float/" + user);
}

function randomInt(user) {
    $.get("/random_int/" + user);
}

function reset_all_data() {
    if (confirm("Are you sure?")) {
        $.get("/reset/j");
        $.get("/reset/p");
        $.get("/reset/s");
        alert("Cleared all data.")
    }
}
