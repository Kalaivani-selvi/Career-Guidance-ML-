# Career Compass [Navigating Future] Project

Welcome to the Career Guidance Project! This project aims to provide personalized career guidance and support to individuals at various stages of their professional journey. By leveraging advanced AI algorithms and open-source data integration, our platform offers tailored recommendations, learning resources, and industry insights to empower users in making informed career decisions.

## Features

- **Login and Register**: Secure authentication system for users to create accounts and log in.
- **Profile**: Personalized user profiles.
- **Career Predictor**: AI-driven career prediction tool to suggest suitable career paths based on user skills.
- **Chatbot**: Interactive chatbot feature to provide real-time assistance and answer user queries.
- **Resume Template**: Tools and templates to assist users in creating professional resumes tailored to their career goals.
- **Question and Answer**:
  - **Round 1 (Communication)**: Assess communication skills through interactive questions and answers.
  - **Round 2 (Aptitude)**: Evaluate aptitude and problem-solving abilities through a series of questions.
  - **Round 3 (Behavioral)**: Analyze behavioral traits and characteristics with specialized questions.
  - **Round 4 (HR)**: Prepare for HR interviews with questions tailored to common interview scenarios.
- **Feedback**: Provide feedback and suggestions to help improve the platform and user experience.

## Installation and Usage

### Prerequisites

- [python,MySql]

### Installation

1. Clone the repository:
  - `git clone [https://github.com/Kalaivani-selvi/Career-Guidance-ML-.git]`
  - `cd Career-Guidance-ML-`

Clone the repository:
<div>
  <code id="cloneCommand">git clone https://github.com/your-username/CareerGuidanceProject.git</code>
  <button onclick="copyCommand('cloneCommand')">Copy</button>
</div>

Change to the project directory:
<div>
  <code id="cdCommand">cd CareerGuidanceProject</code>
  <button onclick="copyCommand('cdCommand')">Copy</button>
</div>

<script>
  function copyCommand(elementId) {
  /* Get the text from the code element */
  const command = document.getElementById(elementId).innerText;

  /* Create a textarea to store the command and select it */
  const textarea = document.createElement('textarea');
  textarea.value = command;
  document.body.appendChild(textarea);
  textarea.select();

  /* Copy the command to the clipboard */
  document.execCommand('copy');

  /* Remove the textarea */
  document.body.removeChild(textarea);

  /* Provide visual feedback */
  alert('Command copied to clipboard: ' + command);
}

</script>
