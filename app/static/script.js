async function getWorkouts() {
    fetch("/workouts/")
        .then(response => response.json())
        .then(data => console.log(data))
}