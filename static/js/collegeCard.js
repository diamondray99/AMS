let j = 0;
let a = document.getElementById("college_menu1");
let b = document.getElementById("college_menu2");
let c = document.getElementById("college_menu3");
function college_expand()  {
    if(j===0){
        document.getElementById("college").style.color = "yellow";
        // document.getElementById("my_menu1").style.transform= 'scale(2)';
        // document.getElementById("my_menu2").style.transform= 'scale(2)';
        // document.getElementById("my_menu3").style.transform= 'scale(2)';

        a.style.transform = 'translateY(-100px)';
        b.style.transform = 'translate(-100px, -20px)';
        c.style.transform = 'translate(100px, -20px)';

        a.style.zIndex = "0";
        b.style.zIndex = "0";
        c.style.zIndex = "0";


        j = 1;
    }
    else {
        document.getElementById("college").style.color = "white"

        // document.getElementById("my_menu1").style.transform= 'scale(0.5)';
        // document.getElementById("my_menu2").style.transform= 'scale(0.5)';
        // document.getElementById("my_menu3").style.transform= 'scale(0.5)';

        a.style.transform = 'translateY(0)';
        b.style.transform = 'translate(0)';
        c.style.transform = 'translate(0)';

        a.style.zIndex = "-1";
        b.style.zIndex = "-1";
        c.style.zIndex = "-1";

        j=0;
    }
}
