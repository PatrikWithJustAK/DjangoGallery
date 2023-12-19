
let csrf_token = document.getElementById("csrf")
    function addEventHandlers(){
        const btnlist = document.getElementsByClassName('deletebutton'); 
        for (let i = 0; i < btnlist.length; i++) { // loop through each button in the array
            btnlist[i].addEventListener("click", function handleDelete(e){ 
                let artpiece_id = e.target.parentNode.parentNode.id
                deleteArtPiece(artpiece_id)
                e.target.parentNode.parentNode.style.display = 'none'
            })
    }
}
    
    addEventHandlers()

    async function deleteArtPiece(id){
        const deleteurl= "http://patrikgammon.com:8000/gallery/deleteart/"
        let artid = id 
        console.log(artid)
        var CSRF_TOKEN = document.getElementById("csrf").innerText

        let requesturl = deleteurl.concat(artid)
        await fetch(requesturl, 
            {
            method: "DELETE",
            headers:{
                'X-CSRFTOKEN': CSRF_TOKEN,
                "Content-Type": "application/json"
                }
    }) 
}
