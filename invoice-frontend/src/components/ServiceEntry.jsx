import { useState, useEffect } from 'react'
import axios from 'axios'


const ServiceEntry = () => {
    const [clientId, setClientId] = useState(0)
    const [clients, setClients] = useState([])
    const [employees, setEmployees ] = useState([])
    const [employeeId, setEmployeeId ] = useState(0)
    const [services, setServices] = useState([])
    const [serviceId, setServiceId] = useState(0)


    useEffect(() => {
        const fetchData = async() => {
        try {
                //fetching employees
                const employeeResponse = await axios.get('http://localhost:8000/api/employees/')
                const employeeData = employeeResponse.data
                const activeEmployees = employeeData.filter(employee => employee.is_active === true)
                console.log(activeEmployees, 'active employees')
                
                //fetching clients
                const clientResponse = await axios.get('http://localhost:8000/api/clients/')
                const clientData = clientResponse.data

                //fetching services
                const serviceResponse = await axios.get('http://localhost:8000/api/services/')
                const serviceData = serviceResponse.data
            
                setEmployees(activeEmployees)
                setClients(clientData)
                setServices(serviceData)
                console.log(employees, 'employees')
                console.log(clients, 'clients')
                console.log(services, 'services')
            } catch (error) {
                console.error("error fetching data;", error)
            }
        }
        fetchData()
    }, [clientId, employeeId, serviceId])

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (!clientId || !serviceId || !employeeId) {
            alert("please select a client, an employee, AND a service")
            return
        }
        try {

            const payload = {
                "employee_id": employeeId,
                "client_id": clientId,
                "service_id": serviceId
            }
            await axios.post('http://localhost:8000/api/service_items/', payload)
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
                        <td>Select Client</td>
                        <td>Select Employee</td>
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
                            <select className="form-select" value={employeeId} onChange={(e) => setEmployeeId(e.target.value)}>
                                <option value={0}>select employee</option>
                                    {employees.map((employee) => (
                                    <option key={employee.id} value={employee.id}>
                                    {employee.full_name}
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