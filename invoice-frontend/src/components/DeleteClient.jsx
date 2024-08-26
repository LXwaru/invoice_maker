import { useState, useEffect } from 'react'
import axios from 'axios'

const DeleteClient = () => {
    const [ clients, setClients ] = useState([])
    const [ clientId, setClientId ] = useState(0)

    useEffect(() => {
        const fetchClientData = async () => {
            try {
                //get client list
                const clientResponse = await axios.get('http://localhost:8000/api/clients')
                console.log(clientResponse.data)
                const clientData = clientResponse.data

                setClients(clientData)
            } catch (error) {
                console.error('could not delete client')
            }
        } 
        fetchClientData()
    }, [])

    const handleSubmit = () => {
        try {
            axios.delete(`http://localhost:8000/api/client/${clientId}/`)
            alert('client successfully deleted')

        } catch (error) {
            alert('did not work')
        }
    }

    const handleIdChange = (e) => {
        setClientId(e.target.value)
    }

    return (
        <>
            <form className="form-control" onSubmit={handleSubmit}>

                <select className="form-select">
                        <option value={0}>client id lookup</option>
                        {clients.map((t) => (
                            <option key={t.id}>
                                {t.full_name}: id# {t.id}
                            </option>
                        ))}
                </select>
                <input type="Number" onChange={handleIdChange} id="deleteById" placeholder="input id number"></input>
                <button>click to delete client account</button>
            </form>
        </>
    )
} 
export default DeleteClient