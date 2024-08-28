import { useState, useEffect } from 'react'
import axios from 'axios'

const DisableClient = () => {
    const [ clients, setClients ] = useState([])
    const [ clientId, setClientId ] = useState(0)

    useEffect(() => {
        const fetchClientData = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/clients')
                const responseData= response.data
                const activeClients = responseData.filter(client => client.is_active === true)
                console.log(activeClients)

                setClients(activeClients)
            } catch (error) {
                console.error('could not delete client')
            }
        } 
        fetchClientData()
    }, [])

    const handleSubmit = (e) => {
        e.preventDefault()
        try {
            axios.put(`http://localhost:8000/api/client/${clientId}/`)
            alert('client successfully disabled')
            window.location.reload()
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
                <input type="Number" onChange={handleIdChange} id="disableById" placeholder="input id number"></input>
                <button>click to disable client account</button>
            </form>
        </>
    )
} 
export default DisableClient