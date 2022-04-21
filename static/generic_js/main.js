
let urlBase = window.location.origin + "/";

/**
 * Function to get CSRF token from cookie
 * @author Django
 * @param {String} name 
 * @returns {String}
 */
function getCookie(name) {

    let cookieValue = null;

    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;

}




/**
 * Generic Ajax function
 * @author Luis GP
 * @return {Boolean}
 */
function ajax(json){

    try{

        let data = null;

        if(json.data && json.data instanceof FormData){
            data = json.data;
        }else if(json.data){
            data = new FormData();
            Object.keys(json.data).forEach((key) => {
                data.append(key, json.data[key]);
            });
        }

        fetch(urlBase + json.url, {
            method: json.method ? json.method : 'POST',
            body: data,
            credentials: json.credentials ? json.credentials : 'include',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                ...json.headers
            }
        })
        .then( response => response.json() )
        .then( data => {
            json.success(data)
        })
        .catch(err => {
            json.error(err)
        })

    }catch(e){
        console.log(e)
    }

    return false;

}





/**
 * Function to open a question
 * @author Luis GP
 * @param {Integer} idQuestion
 * @return {Boolean}
 */
function openQuestion(idQuestion){

    try{

        let url = `${urlBase}questions/questionDetails/${idQuestion}`;
        window.location = url;

    }catch(e){
        console.error(e);
    }

    return false;

}