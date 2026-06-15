async function getWorkouts() {
    // reference to the div in the HTML page
    const workoutList = document.getElementById("workout-list")

    // '/workouts/' points at the prefix:'/workouts' + the suffix:'/', defined inside workouts.py 
    fetch("/workouts/")
        .then(response => response.json())
        .then(data => {
            workoutList.replaceChildren();
            for (let i = 0; i < data.length; i++) {
                const li = document.createElement("li");
                li.textContent = data[i].exercise;
                workoutList.append(li);
            }
        })
}