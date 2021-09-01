const movie = document.getElementById('movie');

$.ajax({
    type: 'GET',
    url: '/hall/hall-json/',
    success: function (response) {
        console.log(response.data)
        const hallsData = response.data
        hallsData.map(item => {
            const option = document.createElement('option')
            option.textContent = item.h_Name
            option.setAttribute('value', item.id)
            movie.appendChild(option)
        })
    },
    error: function (error) {
        console.log(error)
    }
})