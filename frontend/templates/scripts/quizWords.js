let quizWords = []
        let currentIndex = 0


        async function fetchQuizWords() {
            try {
                const response = await fetch('http://localhost:8000/learn_words');
                quizWords = await response.json();
                if (quizWords.length > 0) {
                    displayWord();
                } else {
                    document.getElementById("quizContainer").innerHTML = "No words available";
                }
            } catch (error) {
                console.error('Error fetching words:', error);
                document.getElementById("quizContainer").innerHTML = "Failed to load Quiz 😥";
            }
        }

        function displayWord(){
            if (currentIndex < quizWords.length){
                const wordItem = quizWords[currentIndex]
                document.getElementById("quizContainer").innerHTML = 
                `
                <div class="quiz-item">
                        <p">What's that word?</p>
                        <p>${wordItem.definition}</p>
                        <input type="text" id="answerInput">
                        <button class = "quiz-submit" onclick="checkWord()">Submit Answer</button>
                        <p id="feedback"></p>
                    </div>
                `;
            }else{
                document.getElementById("quizContainer").innerHTML = "Quiz Completed!!!"
            }
                
        }


        function checkWord(){
            const Answer = document.getElementById("answerInput").value
            const wordItem = quizWords[currentIndex]
            if (Answer == wordItem.word){
                document.getElementById("feedback").innerHTML = "Word correct!!"
                currentIndex++
                setTimeout(displayWord, 1000)
            }else{
                document.getElementById("feedback").innerHTML = "Wrong answer"
            }
        }

        fetchQuizWords()