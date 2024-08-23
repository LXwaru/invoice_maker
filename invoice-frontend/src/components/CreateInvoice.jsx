import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom' 
import axios from 'axios'
import  DatePicker  from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';


const CreateInvoice = () => {
    const [ teachers, setTeachers ] = useState([])
    const [ teacherId, setTeacherId ] = useState(0)
    const [ startDate, setStartDate ] = useState(new Date())
    const navigate = useNavigate()


    useEffect(() => {
        const fetchTeachers = async() => {
            try {
                const response = await axios.get('http://localhost:8000/api/teachers')
                setTeachers(response.data)
            } catch (error) {
                console.error("error fetching teachers;", error)
            }
        }
        fetchTeachers()
    }, [])

    const handleSubmit = async (e) => {
        e.preventDefault()

        const start = new Date(startDate)
        const end = new Date(startDate)


        start.setHours(0, 0, 0, 0)
        end.setHours(23, 59, 59, 999)

        if (!teacherId) {
            alert("no teacher selected")
            return
        }

        const startDateUTC = start.toISOString()
        const endDateUTC = end.toISOString()

        const payload = {
            teacher_id: teacherId,
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
    return (
        <>
            <form className="form-control" onSubmit={handleSubmit}>
                <h3>Create Invoice</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <td>Select a teacher</td>
                            <td>Choose The Date</td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                            <select className="form-select" value={teacherId} onChange={(e) => setTeacherId(e.target.value)}>
                                <option value={0}>select teacher</option>
                                {teachers.map((t) => (
                                    <option key={t.id} value={t.id}>
                                    {t.full_name}
                                </option>
                                ))}
                                </select>
                            </td>
                            <td>
                                <DatePicker className="form-select"selected={startDate} onChange={(date) => setStartDate(date)} />
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