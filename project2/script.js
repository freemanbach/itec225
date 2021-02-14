
// Dont delete these variables :: default variables
const quoteContainer = document.getElementById('quote-container');
const quoteText = document.getElementById('quote');
const authorText = document.getElementById('author');
const newQuoteBtn = document.getElementById('new-quote');
const loader = document.getElementById('loader');


// Show and enable Loading Spinner
function loading() {
  // Set the following to either true/false to show spinner
  // when loading Quotes
  loader.hidden = ;
  quoteContainer.hidden = ;
}

// UnShow and  disable Remove Loading Spinner
function complete() {
  if (!loader.hidden) {
    // Set quoteContainer to true or false
	 
    // set loader to either true or false
  
  }
}

// Get Quote From Forismatic API
async function getQuote() {

  // Showing loading screen
	

  // We need to use a Proxy URL to make our API call in order to avoid a weird yet specific error
  const proxyUrl = 'https://cors-anywhere.herokuapp.com/';
  const apiUrl = 'https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json';

  try {
      // retrieve response from fetch JS function
      const response = await fetch(/*  Need something here  */);
      const data = await response.json();


    // Check if Author field is available, if not replace it with 'Not Available'
    if (data.quoteAuthor '') {
        authorText.innerText = '';
    } 
    // If there is a Owner/Author, set the data of the Quote to authorText
    else {
	  // Write somethign here
    
    }

    // Dynamically reduce font size for long quotes
    if (data.quoteText.length > 120) {
      quoteText.classList.add('long-quote');
    } 
     else {
      quoteText.classList.remove('long-quote');
    }

    quoteText.innerText = data.quoteText;

    // Stop Loading, Show Quote: write code here
  
  } catch (error) {
        getQuote();
  }
}

// activate the newQuoteButton with a Event Listeners with click event and  function getQuote


// Load the getQuote Function
