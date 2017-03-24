

function faster() {
    console.log("faster");
    $.get("/faster")
}

function slower() {
    console.log("slower");
    $.get("/slower")
}
