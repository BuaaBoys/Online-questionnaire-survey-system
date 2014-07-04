﻿function checkValid(){
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


function addQuestion() {
/*
	在id为upload的Form里，在添加问题的按钮的上方追加一个question div。
	
*/
    var parent = document.getElementById("upload");
    // 如何维护一个全局的no?
    var no = document.getElementsByClassName("question").length;
    
    var question = document.createElement("div");
    question.setAttribute("class", "question");
    
    var select = document.getElementById('select');
    var index = select.selectedIndex;
    var selected = select.options[index];
    var para = document.createElement("p");
    para.textContent = (no + 1) + '.' + selected.text;
	
	var type = document.createElement("input");
	type.setAttribute("type", "hidden");
	type.setAttribute("name", "type");
	type.setAttribute("value", selected.value);
	
    question.id = selected.value;
    
    var delQue = document.createElement("input");
    delQue.setAttribute("type", "button");
    delQue.setAttribute("class", "delItem");
    delQue.setAttribute("onclick", "deleteQuestion(this)");
    delQue.setAttribute("value", "删除本题");
    
    var describe = document.createElement("input");
    describe.setAttribute("type", "text");
    describe.setAttribute("name", "question");

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

	question.appendChild(type);
    question.appendChild(para);
    question.appendChild(describe);
    question.appendChild(delQue);
	if (question.id == "single" || question.id == "multiply") {
		question.appendChild(inc);
		question.appendChild(del);
		addItem(inc);
		addItem(inc);
	}
    //appendNewLine(question);
    
    var submit = document.getElementById("addQuestion");
    
    parent.insertBefore(question, submit);
}

function deleteQuestion(obj) {
/*
	寻找当前节点的父节点，然后删除该父节点。
	删除之后更新各个question div的编号。
*/
    var parent = document.getElementById("upload");
    parent.removeChild(obj.parentNode);
    var questions = document.getElementsByClassName("question");
    for (var i=0; i<questions.length; ++i) {
	var question = questions[i];
	var type = "";
	switch (question.id) {
	case "single":
	    type = "单选题";
	    break;
	case "multiply":
	    type = "多选题";
	    break;
	case "judge":
	    type = "判断题";
	    break;
	case "essay":
	    type = "简答题";
	    break;
	}
	var para = question.getElementsByTagName("p")[0];
	para.textContent = (i + 1) + '.' + type;
    }
}

function addItem(obj) {
/*
	寻找当前节点的父节点，然后在该父节点之后加上一个具有"class=item"属性的div。
	该div含有：
		1个checkbox，用以标识是否被选中（选中的行可被删除）
		1个label，用以标识选项号
		1个input text，用以填写选项内容
*/
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
	var index = document.getElementsByClassName("question").length;
    text.setAttribute("name", "items" + index);
    item.appendChild(choose);
    item.appendChild(label);
    item.appendChild(text);
    parent.appendChild(item);
}

function deleteItem(obj) {
/*
	寻找当前节点的父节点，对该父节点下的所有具有"class=item"属性的div节点进行判断：
	如果该节点的子节点中有checkbox且该checkbox被选中，那么删除该节点。
	删除之后更新各个item div的编号。
*/
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
/*
	在当前节点之后增加一个<br>
*/
    obj.appendChild(document.createElement("br"));
}

