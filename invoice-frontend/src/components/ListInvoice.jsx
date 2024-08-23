import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom';
import axios from 'axios'

const ListInvoices = () => {
    const [ invoices, setInvoices ] = useState([])
    const [ teachers, setTeachers ] = useState([])


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
        const fetchTeachers = async () => {
            const response = await axios.get('http://localhost:8000/api/teachers/')
            console.log("teachers:", response.data)
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
                        <td>Amount Due</td>
                        {/* <td>is paid?</td> */}
                    </tr>
                </thead>
                <tbody>
                {invoices.length === 0 ? (
                    <tr>
                        <td colSpan="4">Loading Invoices...</td>
                    </tr>
                ) : (

                invoices.map((invoice) => (
                    <tr key = {invoice.id}>
                        <td>{new Date(invoice.start_date).toLocaleDateString()}</td>
                        <td>{getTeacherName(invoice.teacher_id)}</td> 
                        <td>${invoice.amount_due.toFixed(2)}</td>
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