const movie = document.getElementById('movie'); // Stores "Movie" element's id
const dis = document.getElementById("dis"); // Stores "dis" element's id
const hall = document.getElementById('hall'); // Stores "hall" element's id
const date = document.getElementById("date"); // Stores "date" element's id
const time = document.getElementById("time"); // Stores "time" element's id
var selectedMovie;
var selectedHall;
var selectedDate;

const hallRep = document.getElementById("hall-rep") // Stores "Hall representive" element's id
const seats = document.querySelectorAll(".row seat:not(.occupied)") // Stores "unoccupied" element's id
const count = document.getElementById('count') // Stores "seat count" element's id
const total = document.getElementById('total'); // Stores "total" element's id
let ticketPrice = 0


const mLabel = document.getElementById('mname'); // Stores selected movie's id
const hLabel = document.getElementById('hname'); // Stores selected hall's id
const mdate = document.getElementById('mdate'); // Stores selected movie-hall's id
const mtime = document.getElementById('mtime'); // Stores selected movie-hall's time
const mseats = document.getElementById('mseats'); // Stores selected movie-hall's seats

var mid = document.getElementById('mid')
var seat_selected = document.getElementById('seat_selected')
var discountId = document.getElementById('discountId')

const inprice = document.getElementById('inprice')
var selectedSeatCount = 0 ///seat counts

var selectedSeats = [] //array to store selected seats

function updateSelectedCount() {
    // function to calculate total price of selected seats
    const selectedSeats = document.querySelectorAll('.row .seat.selected')
    selectedSeatCount = selectedSeats.length;

    total.innerText = (selectedSeatCount * ticketPrice) - ticketPrice; //extra ticket's cost is deducted to correct the price
}

hallRep.addEventListener('click', (e) => {
    if (e.target.classList.contains('seat') && !e.target.classList.contains('occupied')) {
        if (e.target.classList.contains('selected')) {
            const index = selectedSeats.indexOf(e.target.id);
            e.target.classList.remove('selected')
            selectedSeats.splice(index, 1)
        } else {
            e.target.classList.add('selected')
            selectedSeats.push(e.target.id)
        }

    }

    mseats.innerText = selectedSeats
    seat_selected.setAttribute("value", selectedSeats);

    updateSelectedCount();
})


$.ajax({
    type: 'GET', // Setting Method
    url: '/hall/test/', //url for json response
    success: function (response) { //In case of success
        const hallsData = response.data // store JSON response into a variable
        hallsData.map(item => {
            const option = document.createElement('option') //create an element 'option'
            option.textContent = item.name //set its text content to name of movie(from JSON)
            option.setAttribute('value', item.id) //set its value to name of movie_id(from JSON)
            movie.appendChild(option) //add it to HTML Document
        })
    },
    error: function (error) {
        console.log(error) //Print error incase it occurs
    }
})

movie.addEventListener('change', e => { //Define case for when a movie is selected
    try {
        dis.remove() //try to remove default text "Select a movie"
        hall.removeAttribute('disabled') // Remove 'disabled' from select class, as a movie is selected and corresponding hall is required to be selected
    } catch (error) {}

    selectedMovie = e.target.value; // Store ID of selected movie
    mLabel.innerText = $("#movie option:selected").text();

    hall.innerHTML = ""; // Empty out the current hall listing
    date.innerHTML = ""; // Empty out the current date listing
    time.innerHTML = ""; // Empty out the current movie listing


    const defopn = document.createElement('option')
    defopn.textContent = "Select A Hall"
    defopn.setAttribute('id', 'dis2')
    hall.appendChild(defopn)

    let defopn2 = document.createElement('option')
    defopn2.textContent = "Select A Date"
    defopn2.setAttribute('id', 'dis3')
    date.appendChild(defopn2)

    let defopn3 = document.createElement('option')
    defopn3.textContent = "Select A Time"
    defopn3.setAttribute('id', 'dis4')
    time.appendChild(defopn3)


    $.ajax({ // Call a JSON request for selected movie
        type: "GET",
        url: `/hall/test-hall/${selectedMovie}`, //URL to hit on
        success: function (response) {
            const hallData = response.data //Store response data
            hallData.map(item => {
                const option = document.createElement('option') //create an element 'option'
                option.textContent = item.hall + " (" + item.cat + ")" //set text to hall_name(Category)
                option.setAttribute('value', item.id) //set ticket id for selection
                hall.appendChild(option) //add it to document
            })
        },
        error: function (error) { //print that error
            console.log(error)
        }

    })

})

hall.addEventListener('change', e => {
    try {
        document.getElementById("dis2").remove()
        date.removeAttribute('disabled') // Remove 'disabled' from select class, as a movie is selected and corresponding hall is required to be selected
    } catch (error) {}



    hLabel.innerText = $("#hall option:selected").text();

    selectedHall = e.target.value; // Store ID of selected movie and Hall
    date.innerHTML = ""; // Empty out the current date listing
    time.innerHTML = ""; // Empty out the current time listing

    let defopn = document.createElement('option')
    defopn.textContent = "Select A Date"
    defopn.setAttribute('id', 'dis3')
    date.appendChild(defopn)

    let defopn3 = document.createElement('option')
    defopn3.textContent = "Select A Time"
    defopn3.setAttribute('id', 'dis4')
    time.appendChild(defopn3)



    $.ajax({ // Call a JSON request for selected movie
        type: "GET",
        url: `/hall/day/${selectedMovie}/${selectedHall}`, //URL to hit on
        success: function (response) {
            const hallData = response.data //Store response data
            hallData.map(item => {
                const option = document.createElement('option') //create an element 'option'
                option.textContent = item.date + " (" + item.day + ")" //set text to day
                option.setAttribute('value', item.date) //set ticket id for selection
                date.appendChild(option) //add it to document
            })
        },
        error: function (error) { //print that error
            console.log(error)
        }

    })

})

date.addEventListener('change', e => {
    try {
        document.getElementById('dis3').remove()
        time.removeAttribute('disabled')
    } catch (error) {}


    mdate.innerText = $("#date option:selected").text();

    selectedDate = e.target.value; // Store ID of selected Date
    time.innerHTML = ""; // Empty out the current date listing
    let defopn = document.createElement('option')
    defopn.textContent = "Select A Time"
    defopn.setAttribute('id', 'dis4')
    time.appendChild(defopn)

    $.ajax({ // Call a JSON request for selected movie
        type: "GET",
        url: `/hall/time/${selectedMovie}/${selectedHall}/${selectedDate}`, //URL to hit on
        success: function (response) {
            const hallData = response.data //Store response data
            hallData.map(item => {
                const option = document.createElement('option') //create an element 'option'
                option.textContent = item.time //set text to day
                option.setAttribute('value', item.id) //set ticket id for selection
                time.appendChild(option) //add it to document
            })
        },
        error: function (error) { //print that error
            console.log(error)
        }

    })
})


time.addEventListener('change', e => {
    try {
        document.getElementById('dis4').remove()
    } catch (error) {}

    mtime.innerText = $("#time option:selected").text();

    id = e.target.value; //get value of movie_hall table
    mid.setAttribute('value', id);

    $.ajax({ // Call a JSON request for selected movie
        type: "GET",
        url: `/hall/price/${id}`, //URL to hit on
        success: function (response) {
            const priceData = response.data //Store response data
            priceData.map(item => {
                ticketPrice = item.price;
                discountId.setAttribute('value', item.cat);
                inprice.setAttribute('value', ticketPrice);
                populateSeats(id);
            })

        },
        error: function (error) { //print that error
            console.log(error)
        }

    })

});

function populateSeats(id) {
    $.ajax({
        type: "GET", // Call a JSON request for selected hall
        url: `/hall/seats/${id}`, //URL to hit on
        success: function (response) {
            const seatData = response.data //Store response data
            seatData.map(item => {
                document.getElementById(item.seat).classList.add("occupied") //add occupied to every seat from json response
            })

        },
        error: function (error) { //print that error
            console.log(error)
        }

    })

}