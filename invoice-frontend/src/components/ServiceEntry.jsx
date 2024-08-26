import { useState, useEffect } from 'react'
import axios from 'axios'


const ServiceEntry = () => {
    const [clientId, setClientId] = useState(0)
    const [clients, setClients] = useState([])
    const [serviceId, setServiceId] = useState(0)
    const [services, setServices] = useState([])


    useEffect(() => {
        const fetchClients = async() => {
        try {
                const response = await axios.get('http://localhost:8000/api/clients')
                setClients(response.data)
            } catch (error) {
                console.error("error fetching clients;", error)
            }
        }
        const fetchServices = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/services')
                setServices(response.data)
            } catch (error) {
                console.error("error fetching services:", error)
            }
        }
        fetchClients()
        fetchServices()
    }, [])

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (!clientId || !serviceId) {
            alert("please select a client AND a service")
            return
        }
        try {
            await axios.post('http://localhost:8000/api/service_items/', 
                {
                client_id: clientId,
                service_id: serviceId
                }
            )
            alert('class sign in successful')
            window.location.reload()
        } catch (error) {
            console.error('class sign in failed', error)
        }
    }


return(
    <>
        <form className="form-control" onSubmit={handleSubmit}>
            <h3>Service Sign in</h3>
            <table className="table">
                <thead>
                    <tr>
                        <td>Select client</td>
                        <td>Select Service</td>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            <select className="form-select" value={clientId} onChange={(e) => setClientId(e.target.value)}>
                                <option value={0}>select client</option>
                                    {clients.map((client) => (
                                    <option key={client.id} value={client.id}>
                                    {client.full_name}
                                </option>
                                ))}
                            </select>
                        </td>
                        <td>
                            <select className="form-select" value={serviceId} onChange={(e) => setServiceId(e.target.value)}>
                                <option value={0}>select class type</option>
                                    {services.map((s) => (
                                    <option key={s.id} value={s.id}>
                                    {s.title}
                                </option>
                                ))}
                            </select>
                        </td>
                    </tr>
                </tbody>
            </table>
            <button>submit</button>
        </form>
    </>
)
}
export default ServiceEntry