import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

const InvoiceDetail = () => {
    
    const [ invoice, setInvoice ] = useState({})
    const [ clients, setClients ] = useState([])
    const [ services, setServices ] = useState([])
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

                //setting state
                setInvoice(invoiceData)
                setClients(clientData)
                setServices(serviceData)
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

    return (
        <>
        <div className="container-sm" width="200px">
            <h2>Invoice Details</h2>
            <h4>Client Name: {getClientName(invoice.client_id)}</h4>
            <h5>Amount Due: ${invoice.amount_due.toFixed(2)}</h5>
            <h5>Paid: {invoice.paid ? 'Yes' : 'No' } </h5>
            <h5>Services:</h5>
            <ol>
                {invoice.service_items.map((item) => (
                    <li key={item.id}>{getServiceTitle(item.service_id)}: {formatDateTime(item.date_time)}</li>
                ))}
            </ol>
        </div>
        </>
    )

}
export default InvoiceDetail