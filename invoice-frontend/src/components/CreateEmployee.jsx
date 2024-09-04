import { useState } from 'react'
import axios from 'axios'


const CreateEmployee = () => {
    const [ name, setName ] = useState('')
    const [ email, setEmail ] = useState('')

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (name === '' || email === '') {
            alert('enter a name AND and email')
            return
        }

        const payload = {
            "full_name": name, 
            "email": email
        }

        try {
            await axios.post('http://localhost:8000/api/employees/', payload)
            alert("employee is now registered and activated")
            window.location.reload()
        } catch (error) {
            console.error("could not register employee", error)
        }
    }

    return (
        <>
            <form className="form-control" onSubmit={handleSubmit}>
                <h3>Register a New Employee</h3>
                <input className='form-control' onChange={(e) => setName(e.target.value)} id="clientNameCreate" placeholder="enter name" />
                <input className='form-control' onChange={(e) => setEmail(e.target.value)} id="clientEmailCreate" placeholder="enter email address" />
                <button>submit</button>
            </form>
        </>
    )
}
export default CreateEmployee