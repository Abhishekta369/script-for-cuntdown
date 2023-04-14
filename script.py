
        // Set the end date (May 5, 2023)
        const endDate = new Date('May 5, 2023 00:00:00').getTime();
    
        // Update the count every second
        const x = setInterval(() => {
    
          // Get the current date and time
          const now = new Date().getTime();
    
          // Calculate the time remaining until the end date
          const timeRemaining = endDate - now;
    
          // Calculate the days, hours, minutes, and seconds remaining
          const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
          const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
          const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
          const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);
    
          // Display the countdown in the HTML element with ID "countdown"
          document.getElementById('countdown').innerHTML = ` ${days}D ${hours}H ${minutes}M ${seconds}S`;
    
          // If the countdown is over, stop updating the count
          if (timeRemaining < 0) {
            clearInterval(x);
            document.getElementById('countdown').innerHTML = "EXPIRED";
          }
        }, 1000); // 1000 milliseconds = 1 second
