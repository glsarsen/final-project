const queryString = window.location.search;
// console.log("window.location.search: ", queryString);
const urlParams = new URLSearchParams(queryString);
const search_text = urlParams.get('search')
// console.log("field search: ", search_text);
links = document.querySelectorAll("ul#sort-links a")
// console.log(links)

for(link of links)
{
    link.href = link.href + "&search=" + search_text;
    // console.log(link.href)
}

