const icon = document.querySelector(".menu");
const nav = document.querySelector(".navlogo nav");
icon.addEventListener("click", ()=>{
    nav.style.transform = "translateX(0)"
})

// CLOSES NAVIGATION
const close_m = document.querySelector(".close");
const nave = document.querySelector("header nav");
close_m.addEventListener("click", ()=>{
    nave.style.transform = "translateX(-150%)";
})

const validateForm = ()=>{
    //
    const inputs = document.querySelectorAll("input");
    inputs.forEach((input) => input.classList.remove("invalid"));
    const errors = document.querySelectorAll(".error");
    errors.forEach((error)=> error.textContent = "");
    const messages = document.querySelectorAll("textarea");
    messages.forEach((message) => message.classList.remove("invalid"));

     const email = document.querySelector(".emai");
    const emailee = document.querySelector(".emai").value;
    const email_err = document.querySelector(".email-err");
    const val = document.querySelector(".valid")
    if(email.value == ""){
        email_err.textContent = "This field is required";
        email.classList.add("invalid")
        // return false;
    }
    
    else if(!email.value.includes('@'),!email.value.includes('.com')){
        val.textContent = "Please enter a valid email address"
        email.classList.add("invalid")  
        // return false;
    }
    const message = document.querySelector("#message");
    const mess = document.querySelector("#message").value;
    const message_err = document.querySelector(".message-err");
    const elnths = document.querySelector(".length")
    const number = document.querySelector(".num")
    if (message.value == ""){
        message_err.textContent = "This field is required";
        message.classList.add("invalid");
       // return false;
    } 
    else if(!isNaN(mess)){
        number.textContent = "Please enter an understandable message";
        message.classList.add("invalid");
    }
    //  else if(!isNaN(mess).length >=1 ){
    //     number.textContent = "Please enter an understandable message";
    //     message.classList.add("invalid");
    // }
    
    else if (mess.length >= 1 && mess.length < 30){
        elnths.textContent = "Please let your message to be more detailed";
        message.classList.add("invalid");
    }
   
}
// const success = document.querySelector(".sucsess")
 const forms = document.querySelector('#form');
    forms.addEventListener('submit', (event)=>{
    event.preventDefault();
    validateForm();
    // });

const active = document.querySelectorAll('.error');
    let hasActiveErrors = false;

    active.forEach((elements)=>{
        if(elements.textContent.trim() !== ""){
            hasActiveErrors = true;
        }
    });

   
    // if(!hasActiveErrors){
    //     // forms.classList.add('sucsess')
    //     success.style.display = 'block'
    //     forms.reset();
    // }
    // success.scrollIntoView({
    //     behavior: 'smooth',
    //     block: 'end'
    // })
    // setTimeout(()=>{
    //     success.style.display = 'none'
        
    // },7000)
   
    });    