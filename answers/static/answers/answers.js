/**
 * This function save a new Answer
 * @author Luis GP
 * @return {Boolean}
 */
 function saveAnswer(){

    try {
        
        let idQuestion = document.getElementById('question-id').value;
        let formData = new FormData();
        formData.append('id_question', idQuestion);
        formData.append('description', quill.container.innerHTML);

        ajax({
            url: 'answers/saveAnswer/',
            data: formData,
            success: function(data){
                if(data.code == 200){
                    quill.container.innerHTML = EMPTY_EDITOR;
                    console.log(data.message);
                    getAnswers(idQuestion);
                }else{
                    console.log(data.message);
                }
            },
            error: function(error){
                console.error(error);
            }
        });

    } catch (error) {
        console.error(e);
    }

    return false;

}





/**
 * Function to get all answers for a question
 * @author Luis GP
 * @return {Boolean}
 */
function getAnswers(idQuestion){

    try {
        
        ajax({
            url: 'answers/getAnswer/',
            data: {
                id_question: idQuestion
            },
            success: function(data){
                if(data.code == 200){
                    let answersList = document.getElementById('answers-list');
                    answersList.innerHTML = "";
                    
                    for(let i of data.answers){

                        let div = document.createElement('div');
                        let isSolution = 
                        `<svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36" viewBox="0 0 36 36">
                            <path d="m6 14 8 8L30 6v8L14 30l-8-8v-8Z"></path>
                        </svg>`;

                        div.className = "answer-item";
                        div.innerHTML += 
                        `<div class="cols-2-6">
                            <div class="votes">
                                <svg aria-hidden="true" class="svg-icon iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36">
                                    <path d="M2 25h32L18 9 2 25Z" onclick="voteUp('${ i.id_answer }')"></path>
                                </svg>
                                <h4>${ i.total_votes }</h4>
                                <svg aria-hidden="true" class="svg-icon iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36">
                                    <path d="M2 11h32L18 27 2 11Z" onclick="voteDown('${ i.id_answer }')"></path>
                                </svg>
                                ${ i.is_solution ? isSolution : '' }
                            </div>
                            <div class="answer-description">${ i.description }</div>
                        </div>
                        <p class="right m-0"><small class="m-l-1">${ i.updated_at }</small></p>
                        <p class="right m-0"><small>- ${ i.user_name }</small></p>`;

                        answersList.append(div);

                    }

                }else{
                    console.log(data.message);
                }
            },
            error: function(error){
                console.error(error);
            }
        });

    } catch (error) {
        console.error(e);
    }

    return false;

}





/**
 * Function to save a positive vote
 * @author Luis GP
 * @return {Boolean}
 */
function voteUp(idAnswer){

    try {
        
        ajax({
            url: 'answers/voteUp/',
            data: {
                id_answer: idAnswer
            },
            success: function(data){
                if(data.code == 200){
                    getAnswers(idQuestion);
                }else{
                    console.log(data.message);
                }
            },
            error: function(error){
                console.error(error);
            }
        });  

    } catch (error) {
        console.error(e);
    }
    
}






/**
 * Function to save a negative vote
 * @author Luis GP
 * @return {Boolean}
 */
 function voteDown(idAnswer){

    try {
        
        ajax({
            url: 'answers/voteDown/',
            data: {
                id_answer: idAnswer
            },
            success: function(data){
                if(data.code == 200){
                    getAnswers(idQuestion);
                }else{
                    console.log(data.message);
                }
            },
            error: function(error){
                console.error(error);
            }
        });  

    } catch (error) {
        console.error(e);
    }
    
}