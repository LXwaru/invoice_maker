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
    

    return (
            <>
            <h3>Invoice List</h3>
            <table className="table">
                <thead>
                    <tr>
                        <td>Date</td>
                        <td>client Name</td>
                        <td>Amount Due</td>
                        <td></td>
                    </tr>
                </thead>
                <tbody>
                {invoices.length === 0 ? (
                    <tr>
                        <td colSpan="4">No Invoices To List</td>
                    </tr>
                ) : (

                invoices.map((invoice) => (
                    <tr key = {invoice.id}>
                        <td>{new Date(invoice.start_date).toLocaleDateString()}</td>
                        <td>{getClientName(invoice.client_id)}</td> 
                        <td className="money" >${invoice.amount_due.toFixed(2)}</td>
                        <td> <Link to={`/invoicedetail/${invoice.id}`}>See Invoice Details</Link></td>
                    </tr>
                ))
                )}
                </tbody>
            </table>
        </>
    );
};

export default ListInvoices