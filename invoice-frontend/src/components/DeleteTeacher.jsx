import { useState, useEffect } from 'react'
import axios from 'axios'

const DeleteTeacher = () => {
    const [ teachers, setTeachers ] = useState([])
    const [ teacherId, setTeacherId ] = useState(0)

    useEffect(() => {
        const fetchTeacherData = async () => {
            try {
                //get teacher list
                const teacherResponse = await axios.get('http://localhost:8000/api/teachers')
                console.log(teacherResponse.data)
                const teacherData = teacherResponse.data

                setTeachers(teacherData)
            } catch (error) {
                console.error('could not delete teacher')
            }
        } 
        fetchTeacherData()
    }, [])

    const handleSubmit = () => {
        try {
            axios.delete(`http://localhost:8000/api/teacher/${teacherId}/`)
            alert('teacher successfully deleted')

        } catch (error) {
            alert('did not work')
        }
    }

    const handleIdChange = (e) => {
        setTeacherId(e.target.value)
    }

    return (
        <>
            <form className="form-control" onSubmit={handleSubmit}>

                <select className="form-select">
                        <option value={0}>teacher id lookup</option>
                        {teachers.map((t) => (
                            <option key={t.id}>
                                {t.full_name}: id# {t.id}
                            </option>
                        ))}
                </select>
                <input type="Number" onChange={handleIdChange} id="deleteById" placeholder="input id number"></input>
                <button>click to delete teacher account</button>
            </form>
        </>
    )
} 
export default DeleteTeacher