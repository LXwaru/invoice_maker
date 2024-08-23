import { useState, useEffect } from 'react'
import axios from 'axios'


const ClassEntry = () => {
    const [teacherId, setTeacherId] = useState(0)
    const [teachers, setTeachers] = useState([])
    const [serviceId, setServiceId] = useState(0)
    const [services, setServices] = useState([])


    useEffect(() => {
        const fetchTeachers = async() => {
        try {
                const response = await axios.get('http://localhost:8000/api/teachers')
                setTeachers(response.data)
            } catch (error) {
                console.error("error fetching teachers;", error)
            }
        }
        const fetchServices = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/services')
                setServices(response.data)
            } catch (error) {
                console.error("error fetching services:", error)
            }
        }
        fetchTeachers()
        fetchServices()
    }, [])

    const handleSubmit = async (e) => {
        e.preventDefault()
        console.log('selected teacher', teacherId)
        console.log('selected service', serviceId)
        try {
            await axios.post('http://localhost:8000/api/service_items/', 
                {
                teacher_id: teacherId,
                service_id: serviceId
                }
            )
            alert('class sign in successful')
            window.location.reload()
        } catch (error) {
            console.error('class sign in failed')
        }
    }


return(
    <>
        <form className="form-control" onSubmit={handleSubmit}>
            <h3>Class Sign in</h3>
            <table className="table">
                <thead>
                    <tr>
                        <td>Select Teacher</td>
                        <td>Select Service</td>
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
                            <select className="form-select" value={serviceId} onChange={(e) => setServiceId(e.target.value)}>
                                <option value={0}>select class type</option>
                                    {services.map((s) => (
                                    <option key={s.id} value={s.id}>
                                    {s.title}
                                </option>
                                ))}
                            </select>
                        </td>
                    </tr>
                </tbody>
            </table>
            <button>submit</button>
        </form>
    </>
)
}
export default ClassEntry