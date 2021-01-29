

let skillBtnGroup = document.querySelectorAll('#skillBtn');
console.log(skillBtnGroup.length);

skillBtnGroup.forEach( (btn) => {

    btn.addEventListener( "click", () => {
            toggleCategoryBtn(btn,skillBtnGroup) 
            toggleSkills(btn.value);
        });

    });

function toggleCategoryBtn(categoryBtn,categories){

    categories.forEach( (btn) => {

        btn === categoryBtn ? btn.className = "category-toggled" : btn.className="category-untoggled";
    })

}
function toggleSkills(category){
    
    let categories = document.querySelectorAll('#skills > div')
    
    categories.forEach( (c) => {

        c.id == category ? c.className ="skill-grid" : c.className = "skill-hidden";
     
    }); 
    

};






