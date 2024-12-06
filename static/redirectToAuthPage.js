function redirectToAuthPage(page) {
    // Determine the correct URL based on the selected user type
    var url = './Templates/' + page + '.html';

    // Redirect to the appropriate page
    window.location.href = url;
 
}