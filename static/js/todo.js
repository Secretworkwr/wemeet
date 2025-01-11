let tasks = [];
const addtask = ()=> {
     const taskinput =document.getElementById("taskinput");
     const text = taskinput.value.trim();

     if(text){
        tasks.push({text:text, completed: false});
        taskinput.value = "";
        updatetasklist();
        updatestats();
        }
};

const toggletaskcomplete = (index) =>{
    tasks[index].completed = !tasks[index].completed;
    updatetasklist();
    updatestats();
}

const deletetask = (index) => {
    tasks.splice(index,1);
    updatetasklist();
    updatestats();
};

const edittask = (index) =>{
    const taskinput = document.getElementById('taskinput');
    taskinput.value = tasks[index].text;
     
    tasks.splice(index,1);
    updatetasklist();
};

const updatestats = ()=>{
    const complettasks = tasks.filter(task=>task.completed).length
    const totaltasks = tasks.length
    const progress =(complettasks/totaltasks)*100
    const progressbar = document.getElementById('progress')

    progressbar.style.widows = `${progress}%`
}

const updatetasklist = () => {
    const tasklist = document.getElementById('task-list');
    tasklist.innerHTML="";

    tasks.forEach((task, index) =>{
        const listitem = document.createElement("li");

        listitem.innerHTML = `
        <div class="taskitem">
            <div class="task ${task.completed ? "completed":""}">
                <input type="checkbox" class="checkbox" ${
                    task.completed ? "checked":""
                }/>
                <p>${task.text}</p>
            </div>
            <div class="icons">
                <img src="images/edit.png" onClick="edittask(${index})">
                <img src="images/bin.png" onClick="deletetask(${index})"/>
            </div>
        </div>
        `;
        listitem.addEventListener("change",() => toggletaskcomplete(index));
        tasklist.append(listitem);
    });
}

document.getElementById("newtask").addEventListener("click", function(e){
    e.preventDefault()

    addtask();
});










