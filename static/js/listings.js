// listings.js

// Use fetch or Axios to get data from the backend
fetch("{% url 'get_listings' %}")
  .then(response => response.json())
  .then(data => {
    // Process the data and update the HTML to display listings
    const listingsContainer = document.getElementById("listings-container");

    if (data.listings && data.listings.length > 0) {
      // Clear existing content
      listingsContainer.innerHTML = "";

      // Loop through the listings and create HTML elements
      data.listings.forEach(listing => {
        const listingCard = document.createElement("div");
        listingCard.className = "col-md-6 col-lg-4 mb-4";

        listingCard.innerHTML = `
          <div class="card listing-preview">
            <!-- Your existing HTML structure here -->
          </div>
        `;

        listingsContainer.appendChild(listingCard);
      });
    } else {
      // No listings available
      listingsContainer.innerHTML = "<div class='col-md-12'><p>No Listings Available</p></div>";
    }
  })
  .catch(error => console.error('Error fetching data:', error));
