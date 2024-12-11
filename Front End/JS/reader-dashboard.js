document.addEventListener("DOMContentLoaded", () => {
    const notifications = [
        "You’ve been invited to review: 'The Next Bestseller'.",
        "Feedback reminder: 'A Tale of Two Worlds'.",
        "New resource added: 'Writing Tips Guide'."
    ];

    const notificationsList = document.getElementById("notifications-list");

    notifications.forEach((notification) => {
        const listItem = document.createElement("li");
        listItem.textContent = notification;
        notificationsList.appendChild(listItem);
    });
});

// Add more reader-specific functionalities if needed
