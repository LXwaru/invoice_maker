import { useState } from 'react'
import axios from 'axios'

const CreateTeacher = () => {
    const [ name, setName ] = useState('')

    const handleSubmit = () => {
        if (name === '') {
            alert('enter a name')
            return
        }

        const payload = {
            "full_name": name
        }
        try {
            axios.post('http://localhost:8000/api/teachers/', payload)
            alert("teacher is now registered")
            window.location.reload()
        } catch (error) {
            console.error("could not create teacher", error)
        }
    }
    
    const handleNameChange = (e) => {
        setName(e.target.value)
    }

    return (
        <>
            <form className="form-control-lg" onSubmit={handleSubmit}>
                <h3>Register a New Teacher</h3>
                <input onChange={handleNameChange} id="teacherCreate" placeholder="enter teacher's name"></input>
                <button>submit</button>
            </form>
        
        </>
    )
}
export default CreateTeacher