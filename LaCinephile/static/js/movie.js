function addRatings(rating, id) {
    console.log("Hello")
    content = document.getElementById(id);
    console.log(content)
    for (var i = 0; i < 10; i++) {
		    if (i < rating) {
			    content.innerHTML += "<span class=star>★</span>";
		    } else {
		    	content.innerHTML += '<span class="star nonrate">★</span>';
	    	}
		}
}

