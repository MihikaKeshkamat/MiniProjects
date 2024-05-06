let userScore = 0;
let compScore = 0; 
const userScorePara = document.querySelector("#user-score");
const compScorePara = document.querySelector("#comp-score");

const choices = document.querySelectorAll(".choice");
const msg = document.querySelector("#msg");
const genCompChoice = () =>
{   
    const options=["rock","paper","scissors"];
    const randIdx =Math.floor(Math.random()*3); //since we want to generate index 0-3 and mathrandom generates a number btwn 0-1 so multiply it with 3 to get a number betwn 0-2
    return options[randIdx];
    //rock,paper,scissors 
}; 

const drawGame = () => {
    console.log("game was draw");
    msg.innerText = "Game was Draw";
    msg.style.backgroundColor="#081b31";
}; 

const showWinner = (userWin, userChoice, compChoice) =>{
    if (userWin){
        userScore++;
        userScorePara.innerText = userScore;
        msg.innerText = `You Win! Your ${userChoice} beats ${compChoice}` ;
        msg.style.backgroundColor="green";
    } else {
        compScore++;
        compScorePara.innerText = compScore;
        msg.innerText = `You Lose! ${compChoice} beats your ${userChoice}` ;
        msg.style.backgroundColor="red";
        
    }
}


const playGame=(userChoice)=>{
    console.log("user Choice = ", userChoice);
    //generate computer choice 
    const compChoice = genCompChoice();
    console.log("comp choice =", compChoice);
    
    if (userChoice === compChoice){
        drawGame();
    } else{
        let userWin = true;  //consider user to win and set condition as true
        if (userChoice==="rock"){ 
            //comp will either play scissors,paper(if comp played rock the game would already be draw according to first if condition)
            userWin = compChoice==="paper" ? false : true; //if comp chooses paper first, user will return false else if comp chooses scissors user returns true 
        } else if (userChoice === "paper"){
            //rock,scissors 
            userWin = compChoice==="scissors" ? false : true;
        } else {
            //user has scissor, comp has rock or paper 
            userWin = compChoice ==="rock" ? false : true;
        } 
        showWinner(userWin, userChoice, compChoice);
    }


};

choices.forEach((choice)=>{
    console.log(choice); 

    choice.addEventListener("click",()=>
    {
        const userChoice=choice.getAttribute("id");
        console.log("choice was clicked", userChoice); 
        playGame(userChoice);
    });
});