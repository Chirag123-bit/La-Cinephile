var seat_selected = document.getElementById("mseats");
var seat = ""
let ticketPrice = 0
const count = document.getElementById('count')

$(document).ready(function () {
    let id = document.getElementById("movie_id_holder").innerText //get value of movie_hall table
    id = parseInt(id)
    $.ajax({
        type: "GET", // Call a JSON request for selected hall
        url: `/hall/seats/${id}`, //URL to hit on
        success: function (response) {
            const seatData = response.data //Store response data
            seatData.map(item => {
                console.log(item.seat)
                seat += " " + item.seat
                document.getElementById(item.seat).classList.add("occupied") //add occupied to every seat from json response
            })
            seat_selected.innerHTML = seat

        },
        error: function (error) { //print that error
            console.log(error)
        }

    })

    $.ajax({ // Call a JSON request for selected movie
        type: "GET",
        url: `/hall/price/${id}`, //URL to hit on
        success: function (response) {
            const priceData = response.data //Store response data
            priceData.map(item => {
                ticketPrice = item.price;
                discountId.setAttribute('value', item.cat);
            })

        },
        error: function (error) { //print that error
            console.log(error)
        }

    })

})