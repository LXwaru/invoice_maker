import { useState } from 'react'
import axios from 'axios'

const CreateClient = () => {
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
            axios.post('http://localhost:8000/api/clients/', payload)
            alert("client is now registered")
            window.location.reload()
        } catch (error) {
            console.error("could not create client", error)
        }
    }
    
    const handleNameChange = (e) => {
        setName(e.target.value)
    }

    return (
        <>
            <form className="form-control-lg" onSubmit={handleSubmit}>
                <h3>Register a New Client</h3>
                <input onChange={handleNameChange} id="clientCreate" placeholder="enter client's name"></input>
                <button>submit</button>
            </form>
        
        </>
    )
}
export default CreateClient