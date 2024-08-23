import { useState } from 'react'
import axios from 'axios'

const CreateService = () => {
    const [ title, setTitle ] = useState('')
    const [ price, setPrice ] = useState(0)

    const handleSubmit = () => {
        if (title === '' || price === 0) {
            alert('please complete the form')
            return
        }

        const payload = {
            'title': title,
            'price': price
        }
        try {
            axios.post('http://localhost:8000/api/services/', payload)
            alert('new service is now registered')
        } catch (error) {
            console.error("could not register new service", error)
        }
    }
    const handleTitleChange = (e) => {
        console.log(e.target.value)
        setTitle(e.target.value)
    }

    const handlePriceChange = (e) => {
        console.log(e.target.value)
        setPrice(e.target.value)
    }

    return (
        <>
            <form className="form-control-gl" onSubmit={handleSubmit}>
                <h3>Register a New Service</h3>
                <table className='table'>
                    <thead>
                        <tr>
                            <td>Service Title</td>
                            <td>Price - USD</td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <input 
                                    onChange={handleTitleChange} 
                                    id="titleCreate" 
                                    placeholder="enter service title"> 
                                </input>
                            </td>
                            <td>
                                <input 
                                    onChange={handlePriceChange} 
                                    id="priceCreate" 
                                    placeholder="enter price">
                                </input>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <button>submit</button>
            </form>
        </>
    )


}
export default CreateService