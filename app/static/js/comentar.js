function getCookie(name) 
{
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

function favorito()
{
    var form = new FormData(document.getElementById('formFavorito'));
    fetch("/crearFavorito",{
        method: 'POST',
        body: form,
        headers: {
            "X-CSRFToken":getCookie('csrftoken'),
        },

    })
    var seleccionar_favorito = document.getElementById('seleccionar_favorito');
    

    seleccionar_favorito.style.display = 'none';
    
    document.getElementById('liston_favorito').innerHTML = `
    <svg id="eliminar_favorito" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-bookmark-fill" viewBox="0 0 16 16" onclick="eliminar_favorito()">
		<path d="M2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2z"/>
	</svg>
    `;
    
}

function eliminar_favorito()
{
    var form = new FormData(document.getElementById('formFavorito'));
    fetch("/eliminarFavorito",{
        method: 'POST',
        body: form,
        headers: {
            "X-CSRFToken":getCookie('csrftoken'),
        },

    })
    var eliminar_favorito = document.getElementById('eliminar_favorito');
    eliminar_favorito.style.display = 'none';
    document.getElementById('liston_favorito').innerHTML = `
    <svg id="seleccionar_favorito" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-bookmark" viewBox="0 0 16 16" onclick="favorito()">
		<path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/>
	</svg>
    `;
}

function comentar()
{
    var form = new FormData(document.getElementById('form_Comment'));
    fetch("/comentarPublicacion",{
        method: 'POST',
        body: form,
        headers: {
            "X-CSRFToken":getCookie('csrftoken'),
            "X-Requested-With": "XMLHttpRequest"
        },

    }).then(
        function(response) {
            return response.json();
        }

    ).then(
        function(data)
        {
            console.log(data);
            comentarios = data.comentarios;
            var comment = document.getElementById('comment_Ajax');
            comment.innerHTML ='';
            for (var i = 0; i < comentarios.length; i++) 
            {
                comment.innerHTML += `
                <div class="card mb-4">
                <div class="card-body">
                  <p>${comentarios[i].commet}</p>
                  <div class="d-flex justify-content-between">
                    <div class="d-flex flex-row align-items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person" viewBox="0 0 16 16">
                            <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4Zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10Z"/>
                        </svg>
                        <p class="small mb-0 ms-2">${comentarios[i].carnet_id}</p>
                    </div>
                  </div>
                </div>
                </div>
                `;
            }
        }
    )
    
}

