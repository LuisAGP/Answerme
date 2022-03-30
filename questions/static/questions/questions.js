let quill;

window.onload = function(e){
    
    try{

        const options  = [
            ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
            ['blockquote', 'code-block'],
          
            [{ 'header': 1 }, { 'header': 2 }],               // custom button values
            [{ 'list': 'ordered'}, { 'list': 'bullet' }],
            [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
            [{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent
            [{ 'direction': 'rtl' }],                         // text direction
          
            [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
          
            [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
            [{ 'font': [] }],
            [{ 'align': [] }],
          
            ['clean']                                         // remove formatting button
        ];


        if(document.getElementById("editor")){

            quill = new Quill('#editor', {
                modules: {
                  syntax: true,     // Include syntax module
                  toolbar: options  // Include button in toolbar
                },
                theme: 'snow'
            });

        }

    }catch(e){
        console.error(e);
    }

    obtenerQuestions();

}




/**
 * Function to get All que questions
 * @author Luis GP
 * @returns {Boolean}
 */
function obtenerQuestions(){

    try{

        ajax({
            url: "questions/getQuestions/",
            success: function(data){

                let questions = document.getElementById("questions-content");

                for(let item of data){

                    let div = document.createElement('div');
                    div.className = "questions-list";

                    //selected-label

                    div.innerHTML +=
                    `<div class="question-item">
                        <h2 class="question-item-title">${item.title}</h2>
                        <hr>
                        <div class="question-item-info"><span>Views: ${item.views}</span><span>Updated at: ${item.updated_at}</span></div>
                    </div>`;

                    questions.append(div);

                }

            },
            error: function(error){
                console.error(error);
            }
        });

    }catch(e){
        console.error(e);
    }

    return false;

}



/**
 * Function to save questions
 * @author Luis GP
 * @return {Boolean}
 */
function saveQuestion(event){

    event.preventDefault();

    try{

        let formData = new FormData(document.getElementById('newQuestion-form'))
        formData.append('description', quill.container.innerHTML)

        ajax({
            url: 'questions/saveQuestion/',
            data: formData,
            success: function(data){
                if(data.code = 200){
                    window.location = "http://localhost:8100/questions/";
                }else{
                    console.log(data.message);
                }
            },
            error: function(error){
                console.error(error);
            }
        });

    }catch(e){
        console.error(e);
    }

    return false;

}




/**
 * Function to get a list of Labels
 * @author Luis Godínez
 * @param {String} value 
 * @return {Boolean}
 */
function getLabels(value){

    try{

        document.getElementById("newQuestion-labels_list").style.display = "";

        ajax({
            url: 'questions/getLabels/',
            data: {
                label: value
            },
            success: function(data){
                let div = document.getElementById('newQuestion-labels_list');
                div.innerHTML = "";

                for(let item of data){
                    let p = document.createElement('p');
                    p.innerHTML = item.name
                    p.onclick = function(){ addLabel(item); }
                    div.append(p);
                }
            },
            error: function(error){
                console.log(error)
            }
        });

    }catch(e){
        console.error(e);
    }

    return false;
    
}





/**
 * Function to hide select
 * @author Luis GP
 * @return {Boolean}
 */
function hideSelect(idSelect, input){

    input.value = "";
    let timer = setTimeout(() => {
        clearTimeout(timer)
        document.getElementById(idSelect).style.display = "none";
    }, 100);
     
}




/**
 * Function to add new label to the form
 * @author Luis GP
 * @return {Boolean}
 */
function addLabel(label){

    try{

        let container = document.getElementById("newQuestion-selected_labels");
        let div       = document.createElement('div');
        let input     = document.createElement('input');

        div.className = "selected-label";
        div.innerHTML = `<a onclick="removeLabel(this)"></a><span>${label.name}</span>`;

        input.name = "labels[]";
        input.value = label.id_label;
        input.type = "hidden";


        div.append(input);
        container.append(div);


    }catch(e){
        console.error(e)
    }

}




/**
 * Function to remove a label from form
 * @author Luis GP
 * @param {DOM Element} a 
 * @return {Boolean}
 */
function removeLabel(a){
    a.parentNode.remove();
    return false;
}