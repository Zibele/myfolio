

let skillBtnGroup = document.querySelectorAll('#skillBtn');
console.log(skillBtnGroup.length);

skillBtnGroup.forEach( (btn) => {

    btn.addEventListener( "click", () => {
            toggleSkills(btn.value);
        });

    });


function toggleSkills(category){
    
    let categories = document.querySelectorAll('#skills > div')
    
    categories.forEach( (c) => {

        c.id == category ? c.className ="skillbox-flex" : c.className = "skillbox-hidden";
     
    }); 
    

};





