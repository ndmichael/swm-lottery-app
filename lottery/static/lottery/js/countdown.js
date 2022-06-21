function addHours(numOfHours, date = new Date()) {
    date.setTime(date.getTime() + numOfHours * 60 * 60 * 1000);
    return date;
}

function hour() {
    var ahead = addHours(1).getTime()
    setInterval(() => {
        var now = new Date().getTime();
        var distance = ahead - now
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));

        document.getElementById("hr-min").innerHTML = minutes
        document.getElementById("hr-sec").innerHTML = seconds

    }, 1000);
}
hour()

function threeHour() {
    var ahead = addHours(3).getTime()

    setInterval(() => {
        var now = new Date().getTime();
        distance = ahead - now
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        document.getElementById("hr3-hr").innerHTML = hours
        document.getElementById("hr3-min").innerHTML = minutes
        document.getElementById("hr3-sec").innerHTML = seconds

    }, 1000);
}
threeHour()

function threeDays() {
    var ahead = addHours(72).getTime()

    setInterval(() => {
        var now = new Date().getTime();
        distance = ahead - now
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        document.getElementById("3day").innerHTML = days
        document.getElementById("3day-hr").innerHTML = hours
        document.getElementById("3day-min").innerHTML = minutes

    }, 1000);
}

threeDays()

function sevenDays() {
    var ahead = addHours(168).getTime()

    setInterval(() => {
        var now = new Date().getTime();
        distance = ahead - now
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        document.getElementById("7days").innerHTML = days
        document.getElementById("7days-hr").innerHTML = + hours
        document.getElementById("7days-min").innerHTML = minutes


    }, 1000);
}

sevenDays()

