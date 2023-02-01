//checks if all the reqs. have been met, and informs the user accordingly
//not much to comment here, lol
const form = document.querySelector("form");
const errorMessage = document.querySelector("#error-message");
const successMessage = document.querySelector("#success-message");
form.addEventListener("submit", e => {
  e.preventDefault();

  errorMessage.innerHTML = "";
  successMessage.innerHTML = "";

  const name = form.elements.name.value;
  const website = form.elements.website.value;
  const comment = form.elements.comment.value;
  form.elements.comment.value = comment.replace(/\n/g, " ");
  let commentlen = form.elements.comment.value;

  if (!name || !website || !comment) {
    errorMessage.innerHTML = "all fields are required, see if you've missed something!";
    return;
  }

  if (!website.startsWith("https://") && !website.startsWith("http://")) {
    errorMessage.innerHTML = "the website must start with https:// or http://";
    return;
  }
  if (commentlen.length > 60) {
    errorMessage.innerHTML = "please keep it under 60 characters!";
    return;
  }
  form.submit(); 
  successMessage.innerHTML = "thank you for signing my guestbook!";
});
