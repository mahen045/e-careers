const appointments = []
let currentAppointmentIndex = null

const today = new Date();
let year = today.getFullYear();
let month = (today.getMonth() + 1).toString().padStart(2, '0');
let day = today.getDate().toString().padStart(2, '0');
const minDate = `${year}-${month}-${day}`;
document.getElementById('date').min = minDate


document.getElementById('doctorForm').addEventListener('submit', (e) => {
    e.preventDefault()

    let name = document.getElementById('name').value
    let doctor = document.getElementById('doctor').value

    let dateString = document.getElementById('date').value
    let date = new Date(dateString)
    const options = {day: '2-digit', month: '2-digit', year: 'numeric'}
    date = date.toLocaleDateString('en-GB', options)

    let time = document.getElementById('time').value
    let ailment = document.getElementById('ailment').value
    let notes = document.getElementById('notes').value

    if (currentAppointmentIndex !== null) {
        appointments[currentAppointmentIndex] = { name, doctor, date, time, ailment, notes }
        currentAppointmentIndex = null 
    } else {
        appointments.push({ name, doctor, date, time, ailment, notes })

    }

    renderAppointments()
    document.getElementById('doctorForm').reset()
})

function renderAppointments() {
    let apptContainer = document.getElementById('upcoming')
    apptContainer.innerHTML = ''
    appointments.forEach((appointment, index) => {
        let appt = document.createElement('div')
        appt.className = 'card mb-3'
        appt.innerHTML = `
            <div class="card-body">
                <h3 class='card-title'> Appointment with ${appointment.doctor} on ${appointment.date} at ${appointment.time}</h3>
                <p class='card-text fs-5'>Condition: ${appointment.ailment}</p>
                <p class='card-text fs-5'>Additional info for Doctor: ${appointment.notes}</p>
                <button class="btn btn-secondary" onclick="editAppointment(${index})">Edit</button>
                <button class="btn btn-danger" onclick="deleteAppointment(${index})">Delete</button>

            </div>
        `

        apptContainer.appendChild(appt)
    })
}

function editAppointment(index) {
    currentAppointmentIndex = index
    document.getElementById('name').value = appointments[index].name
    document.getElementById('doctor').value = appointments[index].doctor
    document.getElementById('date').value = appointments[index].date
    document.getElementById('time').value = appointments[index].time
    document.getElementById('ailment').value = appointments[index].ailment
    document.getElementById('notes').value = appointments[index].notes
}

function deleteAppointment(index) {
    appointments.splice(index, 1)
    renderAppointments()
}