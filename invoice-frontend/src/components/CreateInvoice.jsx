import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom' 
import axios from 'axios'
import  DatePicker  from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';


const CreateInvoice = () => {
    const [ loading, setLoading ] = useState(true)
    const [ clients, setClients ] = useState([])
    const [ serviceItems, setServiceItems ] = useState([])
    const [ nameFilter, setNameFilter ] = useState([])
    const [ dateFilter, setDateFilter ] = useState([])
    const [ startDate, setStartDate ] = useState('')
    const [ endDate, setEndDate ] = useState('')
    const [ services, setServices ] = useState([])
    const [ invoices, setInvoices ] = useState([])
    const [ clientId, setClientId ] = useState(0)
    const [ targetDateRange, setTargetDateRange ] = useState(null)
    const today = new Date()
    const navigate = useNavigate()

    const isToday = (date) => {
        if (!date) return false
        const selectedDate = new Date(date)
        return (
            selectedDate.getFullYear() === today.getFullYear() &&
            selectedDate.getMonth() === today.getMonth() &&
            selectedDate.getDate() === today.getDate()
        )
    }

    const isButtonDisabled = clientId === 0 || 
    isToday(targetDateRange) || 
    targetDateRange === null ||
    dateFilter.length === 0
    console.log(dateFilter)

    useEffect(() => {
        const fetchData = async() => {
            setLoading(true)
            try {
                const clientResponse = await axios.get('http://localhost:8000/api/clients')
                const clientData = clientResponse.data
                
                const serviceItemResponse = await axios.get('http://localhost:8000/api/service_items')
                const serviceItemData = serviceItemResponse.data

                const serviceResponse = await axios.get('http://localhost:8000/api/services')
                const serviceData = serviceResponse.data

                setClients(clientData)
                setServiceItems(serviceItemData)
                setServices(serviceData)

            } catch (error) {
                console.error("error fetching data;", error)
            } finally {
                setLoading(false)
            }
        } 
        fetchData()
    }, [])

    useEffect(() => {
        const filterServiceItems = () => {
            const clientFilter = serviceItems.filter(item => item.client_id === Number(clientId))
    
            if (startDate && endDate) {
                const dateRangeFilter = clientFilter.filter(item => item.date_time >= startDate && item.date_time <= endDate)
                setDateFilter(dateRangeFilter)
            } else {
                // setDateFilter(clientFilter)

            }
        }
        filterServiceItems()
    }, [clientId, serviceItems, startDate, endDate])
    
    const handleNameFilterChange = (e) => {
        e.preventDefault()
        setClientId(Number(e.target.value))
    }

    const handleDateFilter = (selectedDate) => {
        setTargetDateRange(selectedDate)

        if (selectedDate) {

            const start = new Date(selectedDate)
            const end = new Date(selectedDate)
            start.setHours(0, 0, 0, 0)
            end.setHours(23, 59, 59, 999)
            const startDateUTC = new Date(start.getTime() - (start.getTimezoneOffset() * 60000)).toISOString().split('T')[0] + "T00:00:00.000Z";
            const endDateUTC = new Date(end.getTime() - (end.getTimezoneOffset() * 60000)).toISOString().split('T')[0] + "T23:59:59.999Z";
            setStartDate(startDateUTC)
            setEndDate(endDateUTC)
        } else {
            console.error("selected data is undefined or null")
        }
    }

    const getServiceTitle = (serviceId) => {
        const service = services.find(s => s.id === serviceId);
        return service ? service.title : 'Unknown Service';
    };

    const getServicePrice = (serviceId) => {
        const service = services.find(s => s.id === serviceId)
        return service ? service.price : 'Unknown Price'
    }

    const handleSubmit = () => {
        const payload = {
            "client_id": clientId,
            "start_date": startDate,
            "end_date": endDate
        }
        try {
            axios.post('http://localhost:8000/api/invoices/', payload)
            alert('invoice register successful')
            navigate('/listinvoice')

        } catch (error) {
            console.error("could register invoice", error)
        }
    }

    return (
        <>
            {loading ? (
                <div>Loading...</div>
            ) : (
                <>
                <form className='form-control' onSubmit={handleSubmit}>
                <h3>Create Invoice</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <td>Select a client</td>
                            <td>Choose The Date</td>
                            <td></td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                            <select className="form-select" value={clientId} onChange={handleNameFilterChange}>
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
                                selected={targetDateRange} 
                                onChange={handleDateFilter}
                                maxDate={today}
                                // excludeDates={[today]}
                                placeholderText="Select a Date" />
                            </td>
                            <td>
                                <button
                                        className="btn btn-success"
                                        disabled={isButtonDisabled}
                                        >register invoice
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table className="table">
                    <thead>
                        <tr>
                            <td>Sale ID</td>
                            <td>Services</td>
                            <td>Price</td>
                        </tr>
                    </thead>
                    <tbody>

                            {dateFilter.map((item) => (
                        <tr key = {item.id}>
                                <td>{item.id}</td>
                                <td>{getServiceTitle(item.service_id)}</td>
                                <td>{getServicePrice(item.service_id)}</td>

                        </tr>
                            ))}
                    </tbody>
                </table>
                </form>

            </>
            )}
        </>
    )

}
export default CreateInvoice