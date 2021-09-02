const movie = document.getElementById('movie');
const dis = document.getElementById("dis");
const hall = document.getElementById('hall');
const day = document.getElementById("day");



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
        day.removeAttribute('disabled') // Remove 'disabled' from select class, as a movie is selected and corresponding hall is required to be selected
        hall.removeAttribute('disabled') // Remove 'disabled' from select class, as a movie is selected and corresponding hall is required to be selected
    } catch (error) {}

    const selectedMovie = e.target.value; // Store ID of selected movie

    hall.innerHTML = ""; // Empty out the current hall listing

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

    const selectedMH = e.target.value; // Store ID of selected movie and Hall
    day.innerHTML = ""; // Empty out the current day listing

    $.ajax({ // Call a JSON request for selected movie
        type: "GET",
        url: `/hall/day/${selectedMH}`, //URL to hit on
        success: function (response) {
            const hallData = response.data //Store response data
            hallData.map(item => {
                const option = document.createElement('option') //create an element 'option'
                option.textContent = item.day //set text to day
                option.setAttribute('value', item.id) //set ticket id for selection
                day.appendChild(option) //add it to document
            })
        },
        error: function (error) { //print that error
            console.log(error)
        }

    })

})