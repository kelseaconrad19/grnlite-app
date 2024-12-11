document.addEventListener("DOMContentLoaded", () => {
    const notifications = [
        "You have new feedback on your manuscript 'The Lost World'.",
        "Your manuscript 'Unraveled Mysteries' has been reviewed by 2 beta readers.",
        "A new beta reader has bid for your manuscript 'The Last Stand'.",
        "Your NDA has been signed by the last beta reader."
    ];

    const notificationsList = document.getElementById("notifications-list");

    notifications.forEach((notification) => {
        const listItem = document.createElement("li");
        listItem.textContent = notification;
        notificationsList.appendChild(listItem);
    });
});

// Add more author-specific functionalities if needed
