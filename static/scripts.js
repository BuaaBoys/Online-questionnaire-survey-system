function checkValid(){
    var questElement = document.quest.elements;
    for(var i=0; i<questElement.length-1;i++){
	if(trim(questElement[i].value)==""){
	    questElement[i].focus();
	    questElement[i].style.background = "red";
	    alert("请填写完整！");
	    questElement[i].style.background = "white";
	    return false;
	    break;
	}
    }
    return true;
}

function trim(str){
    return str.replace(/^\s\s*/,'').replace(/\s\s*$/,'');
}


function add_question()
{
    var parent = document.getElementById("upload");
    
    var question = document.createElement("div");
    question.setAttribute("class", "question");

    var select = document.getElementById('select');
    var p = document.createElement("p");
    var index = select.selectedIndex;
    var text = select.options[index].text;
    p.textContent = text;
    p.id = text;

    var delQue = document.createElement("button");
    delQue.setAttribute("class", "delItem");
    delQue.textContent = "delete Question";
    
    var inp = document.createElement("input");
    inp.setAttribute("type", "text");

    var inc = document.createElement("button");
    inc.setAttribute("class", "addItem");
    inc.textContent = "add Item";

    var del = document.createElement("button");
    del.setAttribute("class", "delItem");
    del.textContent = "delete Item";

    question.appendChild(p);
    question.appendChild(delQue);
    question.appendChild(inp);
    question.appendChild(inc);
    question.appendChild(del);

    parent.appendChild(question);
}

function delete_question() {
    
}
