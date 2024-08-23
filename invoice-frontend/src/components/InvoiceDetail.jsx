import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

const InvoiceDetail = () => {
    
    const [ invoice, setInvoice ] = useState({})
    const [ teachers, setTeachers ] = useState([])
    const [ services, setServices ] = useState([])
    const {id} = useParams()
    const [ loading, setLoading ] = useState(true)

    useEffect(() => {
        const fetchInvoice = async () => {
            try {
                //fetching invoice data
                const invoiceResponse = await axios.get(`http://localhost:8000/api/invoice/${id}/`)
                const invoiceData = invoiceResponse.data

                //fetching teacher data
                const teacherResponse = await axios.get(`http://localhost:8000/api/teachers/`)
                const teacherData = teacherResponse.data

                //fetching service data
                const serviceResponse = await axios.get('http://localhost:8000/api/services/')
                const serviceData = serviceResponse.data

                //setting state
                setInvoice(invoiceData)
                setTeachers(teacherData)
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

    const getTeacherName = (teacherId) => {
        const teacher = teachers.find(t => t.id === teacherId)
        return teacher ? teacher.full_name: 'Unknown Teacher'
    }

    const getServiceTitle = (serviceId) => {
        const service = services.find(s => s.id === serviceId);
        return service ? service.title : 'Unknown Service';
    };

    return (
        <>
        <div className="container-sm" width="200px">
            <h2>Invoice Details</h2>
            <h4>Teacher Name: {getTeacherName(invoice.teacher_id)}</h4>
            <h5>Amount Due: ${invoice.amount_due.toFixed(2)}</h5>
            <h5>Paid: {invoice.paid ? 'Yes' : 'No' } </h5>
            <h5>Services:</h5>
                {invoice.service_items.map((item) => (
                    <p key={item.id} className="border">{getServiceTitle(item.service_id)}</p>
                ))}
        </div>
        </>
    )

}
export default InvoiceDetail