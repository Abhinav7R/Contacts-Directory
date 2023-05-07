function promptForKey() {
    var key = prompt("Enter the appaji key to proceed:");
    if (key === "appaji_key") {
      // Key is correct, proceed with the next action
      // ...
    } else {
      // Key is incorrect, show an error message
      alert("Invalid key. Please try again.");
      window.location.href = "/faculty";
    }
  }
  // Call the promptForKey() function to start the prompt
  promptForKey();