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
const csrftoken = getCookie('csrftoken');



async function buttonOnClick(event) {
    event.preventDefault();
    let url = event.target.dataset.url;
    let A = document.getElementById('A');
    let B = document.getElementById('B');
    let request = new Request(url, {
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            body: JSON.stringify({
                'A': A.value,
                'B': B.value
            })
        }
    );
    let response = await fetch(request);
    let value = await response.json();
    let div = document.getElementById('result');
    if (response.ok) {
        div.style.color = 'green';
        div.innerText = value.result;
    } else {
        div.style.color = 'red';
        div.innerText = value.error;
    }

}