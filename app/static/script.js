async function getWorkouts() {
    // reference to the div in the HTML page
    const workoutList = document.getElementById("workout-list")

    // '/workouts/' points at the prefix:'/workouts' + the suffix:'/', defined inside workouts.py 
    fetch("/workouts/")
        .then(response => response.json())
        .then(data => {
            for (let i = 0; i < data.length; i++) {
                const p = document.createElement("p");
                p.textContent = data[i].exercise;
                workoutList.append(p);
            }
        })
}