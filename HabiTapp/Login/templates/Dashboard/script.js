var Click = false;

function DayFunc() {

    if(Click) {

        btn.style.backgroundColor = 'white';
        btn.style.color = "26252F";
        btn.style.border = "solid";
        Click = !Click;
    }
    else {

        btn.style.backgroundColor = '26252F';
        btn.style.color = "white";
        btn.style.border = "none";
        Click = !Click;
    }
}