import { NavLink } from "react-router-dom"

const Footer = () => {
    return (
        <div className='nav'>
            <ul className="nav fixed-bottom justify-content-center">
                <li className="nav-item">
                    <NavLink className="nav-link" to="/deleteclient">DELETE CLIENT ACCOUNT</NavLink>
                </li>
                <li className="nav-item">
                    <NavLink className="nav-link" to="/createinvoice">UPDATE / DELETE SERVICE</NavLink>      
                </li>
            </ul>
        </div>
    )
}
export default Footer