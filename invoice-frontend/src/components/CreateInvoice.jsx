import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom' 
import axios from 'axios'
import  DatePicker  from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';


const CreateInvoice = () => {
    const [ clients, setClients ] = useState([])
    const [ invoices, setInvoices ] = useState([])
    const [ clientId, setClientId ] = useState(0)
    const [ startDate, setStartDate ] = useState(null)
    const today = new Date()
    const navigate = useNavigate()


    useEffect(() => {
        const fetchData = async() => {
            try {
                const clientResponse = await axios.get('http://localhost:8000/api/clients')
                const clientData = clientResponse.data
                const invoiceResponse = await axios.get('http://localhost:8000/api/invoices')
                const invoiceData = invoiceResponse.data
                console.log(clientData, "client data")
                console.log(invoiceData, "invoice data")
                setClients(clientData)
                setInvoices(invoiceData)
            } catch (error) {
                console.error("error fetching data;", error)
            }
        }
        fetchData()
    }, [])
    console.log(invoices, "invoices")

const handleSubmit = async (e) => {
        e.preventDefault()

        const start = new Date(startDate)
        const end = new Date(startDate)


        start.setHours(0, 0, 0, 0)
        end.setHours(23, 59, 59, 999)

        if (!clientId) {
            alert("no client selected")
            return
        }

        const startDateUTC = start.toISOString()
        const endDateUTC = end.toISOString()

        if (clientId in invoices.map(invoice => invoice.client_id) && startDateUTC in invoices.map(invoice => invoice.start(date_time))) {
            const invoiceIdToUpdate = invoice.id 
            
            // fetch invoice data for specific object that matches the conditional
            const payload = {
                "client_id": clientId,
                "service_id": invoices.service_id,
                "id": invoices.service_items.id,
                "date_time": startDateUTC

            }
            // make a payload object for the PUT function
            // make the api PUT call

        } else {
            const payload = {
                client_id: clientId,
                start_date: startDateUTC,
                end_date: endDateUTC
            }
            console.log(payload, "payload")
    
            try {
                await axios.post('http://localhost:8000/api/invoices/', payload)
                alert('invoice created successfully')
                navigate('/listinvoice')
            } catch (error) {
                console.error('invoice creation failure', error.response ? error.response.data : error.message)
            }
        }


        
            
        
    }
    return (
        <>
            <form className="form-control" onSubmit={handleSubmit}>
                <h3>Create Invoice</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <td>Select a client</td>
                            <td>Choose The Date</td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                            <select className="form-select" value={clientId} onChange={(e) => setClientId(e.target.value)}>
                                <option value={0}>select client</option>
                                {clients.map((t) => (
                                    <option key={t.id} value={t.id}>
                                    {t.full_name}
                                </option>
                                ))}
                                </select>
                            </td>
                            <td>
                                <DatePicker
                                className="form-select"
                                selected={startDate} 
                                onChange={(date) => setStartDate(date)}
                                maxDate={today}
                                // excludeDates={[today]}
                                placeholderText="Select a Date" />
                            </td>
                        </tr>
                    </tbody>
                </table>
                <button type='submit'>submit</button>
            </form>

        </>
    )

}
export default CreateInvoice