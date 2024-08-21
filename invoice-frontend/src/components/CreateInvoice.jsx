import { useState, useEffect } from 'react'
import axios from 'axios'
import  DatePicker  from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';


const CreateInvoice = () => {
    const [ teachers, setTeachers ] = useState([])
    const [ teacherId, setTeacherId ] = useState(0)
    const [ startDate, setStartDate ] = useState(new Date())


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
        } catch (error) {
            console.error('invoice creation failure', error.response ? error.response.data : error.message)
        }
    }
    return (
        <>
            <hr />
            <div className="container-md">                
                <form onSubmit={handleSubmit}>
                    <h3>Teacher</h3>
                    <select className="form-select" value={teacherId} onChange={(e) => setTeacherId(e.target.value)}>
                        <option value={0}>select teacher</option>
                        {teachers.map((t) => (
                            <option key={t.id} value={t.id}>
                                {t.full_name}
                            </option>
                        ))}
                    </select>
                    <h3>Choose a date</h3>
                    <DatePicker className="form-select"selected={startDate} onChange={(date) => setStartDate(date)} />
                    <br />
                    <button type='submit'>submit</button>
                </form>
            </div>
        </>
    )

}
export default CreateInvoice