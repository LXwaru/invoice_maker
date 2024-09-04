import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom';
import axios from 'axios'

const ListInvoices = () => {
    const [ invoices, setInvoices ] = useState([])
    const [ clients, setClients ] = useState([])


    useEffect(() => {

        const fetchInvoices = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/invoices/')
                console.log("invoices:", response.data)
                setInvoices(response.data)
            } catch (error) {
                console.error('could not fetch invoice', error)
            } 
        }
        fetchInvoices()
    }, [])

    useEffect(() => {
        const fetchClients = async () => {
            const response = await axios.get('http://localhost:8000/api/clients/')
            console.log("clients:", response.data)
            setClients(response.data)

        }
        fetchClients()
    }, [])
    

    const getClientName = (clientId) => {
        const client = clients.find(t => t.id === clientId)
        return client ? client.full_name: 'Unknown client'
    }
    
    const displayDate = (dateString) => {
        const date = new Date(dateString)
        return date.toLocaleDateString()
    }

    return (
        <>
            <div className='container-fluid'>
            <h3>Invoice List</h3>
                    {invoices.length === 0 ? (

                            <p colSpan="4">No Invoices To List</p>

                    ) : (

                    invoices.map((invoice) => (
                        <div className='container-fluid' key={invoice.id}>
                            <hr />
                            <ul className='list-group'>
                                <li className='list-group-item'><strong>{displayDate(invoice.end_date)}</strong> <em>- invoice id: {invoice.id}</em></li>
                                <li className='list-group-item'><strong>{getClientName(invoice.client_id)}</strong><em> - ${invoice.amount_due.toFixed(2)}</em> - <Link to={`/invoicedetail/${invoice.id}`}>See Invoice Details</Link></li>
                            </ul>
                        </div>
                    ))
                    )}

            </div>
    </>
);
};


export default ListInvoices