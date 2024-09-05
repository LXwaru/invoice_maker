import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

const InvoiceDetail = () => {
    
    const [ invoice, setInvoice ] = useState({})
    const [ clients, setClients ] = useState([])
    const [ services, setServices ] = useState([])
    const [ employees, setEmployees ] = useState([])
    const {id} = useParams()
    const [ loading, setLoading ] = useState(true)

    useEffect(() => {
        const fetchInvoice = async () => {
            try {
                //fetching invoice data
                const invoiceResponse = await axios.get(`http://localhost:8000/api/invoice/${id}/`)
                const invoiceData = invoiceResponse.data

                //fetching client data
                const clientResponse = await axios.get(`http://localhost:8000/api/clients/`)
                const clientData = clientResponse.data

                //fetching service data
                const serviceResponse = await axios.get('http://localhost:8000/api/services/')
                const serviceData = serviceResponse.data

                //fetching employee data
                const employeeResponse = await axios.get('http://localhost:8000/api/employees/')
                const employeeData = employeeResponse.data

                //setting state
                setInvoice(invoiceData)
                setClients(clientData)
                setServices(serviceData)
                setEmployees(employeeData)
                setLoading(false)
            } catch (error) {
                console.error('Error fetching invoice:', error)
                setLoading(false)
            }
        }
        fetchInvoice(id)
    }, [id])

    if(loading) {
        return <div>Loading...</div>
    }

    if(!invoice) {
        return <div>Invoice not found.</div>
    }

    const getClientName = (clientId) => {
        const client = clients.find(t => t.id === clientId)
        return client ? client.full_name: 'Unknown client'
    }

    const getServiceTitle = (serviceId) => {
        const service = services.find(s => s.id === serviceId);
        return service ? service.title : 'Unknown Service';
    };

    const formatDateTime = (dateString) => {
        const date = new Date(dateString)
        const formattedDate = date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long', 
            day: 'numeric',
        })
        const formattedTime = date.toLocaleTimeString('en-US', {
            hour: 'numeric',
            minute: 'numeric',
            hour12: true,
        })
        return `${formattedDate} - ${formattedTime}`
    }

    const getEmployeeName = (employeeId) => {
        const employee = employees.find(employee => employee.id === employeeId)
        return employee ? employee.full_name: 'Unknown employee'
    }

    return (
        <>
        <div className="container-sm" width="200px">
            <h2>Invoice Details</h2>
            <h4>Client Name: {getClientName(invoice.client_id)}</h4>
            <h5>Amount Due: ${invoice.amount_due.toFixed(2)}</h5>
            <h5>Paid: {invoice.paid ? 'Yes' : 'No' } </h5>
            <h5>Services:</h5>
            <table className='table'>
                <thead>
                    <tr>
                        <td>Service title</td>
                        <td>Date/Time for services rendered</td>
                        <td>Service provided by:</td>
                    </tr>
                </thead>
                <tbody>
                    {invoice.service_items.map((item) => (
                    <tr key={item.id}>
                        <td>
                            {getServiceTitle(item.service_id)}     
                        </td>
                        <td>
                            {formatDateTime(item.date_time)}
                        </td>
                        <td>
                            {getEmployeeName(item.employee_id)}
                        </td>
                    </tr>
                    ))}
                
                </tbody>
            </table>
        </div>
        </>
    )

}
export default InvoiceDetail