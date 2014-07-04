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


function addQuestion()
{
    var parent = document.getElementById("upload");
	// 如何维护一个全局的no?
    var no = document.getElementsByClassName("question").length;
	
    var question = document.createElement("div");
    question.setAttribute("class", "question");
	
    var select = document.getElementById('select');
    var index = select.selectedIndex;
	var selected = select.options[index];
	var p = document.createElement("p");
    p.textContent = (no + 1) + '.' + selected.text;
	question.id = selected.value;
	
    var delQue = document.createElement("button");
    delQue.setAttribute("class", "delItem");
	delQue.setAttribute("onclick", "deleteQuestion(this)");
    delQue.textContent = "删除本题";
    
    var describe = document.createElement("input");
    describe.setAttribute("type", "text");

    var inc = document.createElement("input");
	inc.setAttribute("type", "button");
    inc.setAttribute("class", "addItem");
	inc.setAttribute("onclick", "addItem(this)");
    inc.setAttribute("value", "增加选项");

    var del = document.createElement("input");
	del.setAttribute("type", "button");
    del.setAttribute("class", "delItem");
	del.setAttribute("onclick", "deleteItem(this)");
    del.setAttribute("value", "删除选项");

    question.appendChild(p);
	question.appendChild(describe);
    question.appendChild(delQue);
    question.appendChild(inc);
    question.appendChild(del);
	appendNewLine(question);
	
	var submit = document.getElementById("addQuestion");
	
    //parent.appendChild(question);
	parent.insertBefore(question, submit);
}

function deleteQuestion(obj) {
    var parent = document.getElementById("upload");
	parent.removeChild(obj.parentNode);
}

function addItem(obj) {
	var parent = obj.parentNode;
	var no = parent.getElementsByClassName("item").length;
	var type = parent.id;
	
	var item = document.createElement("div");
	var choose = document.createElement("input");
	var label = document.createElement("label");
	var text = document.createElement("input");
	item.setAttribute("class", "item");
	choose.setAttribute("type", "checkbox");
	choose.setAttribute("class", "checkbox");
	label.textContent = (no + 1) + '.';
	text.setAttribute("type", "text");
	item.appendChild(choose);
	item.appendChild(label);
	item.appendChild(text);
	parent.appendChild(item);
}

function deleteItem(obj) {
	var parent = obj.parentNode;
	var items = parent.getElementsByClassName("item");
	//alert(""+items.length);
	for (var i=items.length-1; i>=0; --i) {
		var checkBoxs = items[i].getElementsByClassName("checkbox");
		if (checkBoxs[0].checked) {
			items[i].remove();
		}
	}
	items = parent.getElementsByClassName("item");
	for (var i=0; i<items.length; ++i) {
		var label = items[i].getElementsByTagName("label")[0];
		label.textContent = (i + 1) + '.';
	}	
}

function appendNewLine(obj) {
	obj.appendChild(document.createElement("br"));
}

function Valid() {
	return true;
}