import { useState, useEffect } from 'react'
import axios from 'axios'

const ListInvoices = () => {
    const [ invoices, setInvoices ] = useState([])
    const [ teachers, setTeachers ] = useState([])

    useEffect(() => {

        const fetchInvoices = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/invoices/')
                console.log(response.data)
                setInvoices(response.data)
            } catch (error) {
                console.error('could not fetch invoice', error)
            } 
        }
        fetchInvoices()
    }, [])

    useEffect(() => {
        const fetchTeachers = async () => {
            const response = await axios.get('http://localhost:8000/api/teachers/')
            console.log(response.data)
            setTeachers(response.data)

        }
        fetchTeachers()
    }, [])

    const getTeacherName = (teacherId) => {
        const teacher = teachers.find(t => t.id === teacherId)
        return teacher ? teacher.full_name: 'Unknown Teacher'
    }

    return (
            <>
            <hr />
            <h3>Invoice List</h3>
            <table className="table">
                <thead>
                    <tr>
                        <td>Date</td>
                        <td>Teacher Name</td>
                        <td>Services</td>
                        <td>Amount Due</td>
                        <td>Paid</td>
                    </tr>
                </thead>
                <tbody>
                {invoices.map((invoice) => (
                    <tr key = {invoice.id}>
                        <td>{new Date(invoice.start_date).toLocaleDateString()}</td>
                        <td>{getTeacherName(invoice.teacher_id)}</td> 
                        <td>
                                    {invoice.service_items && invoice.service_items.length > 0 ? (
                                        <ul>
                                            {invoice.service_items.map((item, index) => (
                                                <li key={index}>{item.service.title}</li> 
                                            ))}
                                        </ul>
                                    ) : (
                                        <span>No services</span>
                                    )}
                        </td>
                        <td>${invoice.amount_due.toFixed(2)}</td>
                        <td>{invoice.paid ? "Yes" : "No"}</td>
                    </tr>
                ))}
                </tbody>
            </table>
        </>
    )
}
export default ListInvoices